import ifcopenshell
import csv
import os

# ===== FOLDER WITH IFC FILES =====
folder_path = "./ifc_files"   # change this to your folder

# ===== OUTPUT CSV =====
output_csv = "combined_ifc_data.csv"

# ===== TARGET TYPES =====
target_types = [
    "IfcWall",
    "IfcSlab",
    "IfcBeam",
    "IfcColumn",
    "IfcRoof",
    "IfcDoor",
    "IfcWindow",
    "IfcPipeSegment",
    "IfcFlowSegment"
]

# ===== HELPER: GET MATERIAL =====
def get_material(element):
    if hasattr(element, "HasAssociations"):
        for rel in element.HasAssociations:
            if rel.is_a("IfcRelAssociatesMaterial"):
                mat = rel.RelatingMaterial
                try:
                    return mat.Name
                except:
                    return str(mat)
    return ""

# ===== HELPER: GET QUANTITIES =====
def get_quantities(element):
    volume = ""
    area = ""
    length = ""

    if hasattr(element, "IsDefinedBy"):
        for rel in element.IsDefinedBy:
            if rel.is_a("IfcRelDefinesByProperties"):
                prop = rel.RelatingPropertyDefinition

                if prop.is_a("IfcElementQuantity"):
                    for q in prop.Quantities:

                        if q.is_a("IfcQuantityVolume"):
                            volume = q.VolumeValue

                        elif q.is_a("IfcQuantityArea"):
                            area = q.AreaValue

                        elif q.is_a("IfcQuantityLength"):
                            length = q.LengthValue

    return volume, area, length

# ===== CREATE CSV =====
with open(output_csv, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow([
        "SourceFile",
        "Type",
        "Name",
        "Material",
        "Volume",
        "Area",
        "Length"
    ])

    # ===== LOOP ALL IFC FILES =====
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".ifc"):

            filepath = os.path.join(folder_path, filename)
            print(f"Processing: {filename}")

            try:
                model = ifcopenshell.open(filepath)
            except Exception as e:
                print(f"❌ Failed to open {filename}: {e}")
                continue

            # ===== EXTRACT ELEMENTS =====
            for t in target_types:
                elements = model.by_type(t)

                for elem in elements:
                    elem_type = elem.is_a()
                    name = elem.Name if elem.Name else elem.GlobalId

                    material = get_material(elem)
                    volume, area, length = get_quantities(elem)

                    writer.writerow([
                        filename,
                        elem_type,
                        name,
                        material,
                        volume,
                        area,
                        length
                    ])

print(f"\n✅ DONE → {output_csv}")
