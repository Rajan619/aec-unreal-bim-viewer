# AEC Unreal BIM Viewer (IFC-based Digital Twin Prototype)

## Overview

This project demonstrates a real-time AEC visualization system built in Unreal Engine, where IFC (Building Information Modeling) data is parsed, structured, and mapped to interactive elements for inspection and analysis.

The goal is to simulate a lightweight **digital twin workflow** — enabling users to explore structures, inspect metadata, and interact with BIM elements in real time.

---
## IFC Files
IFC files were sourced form the smaple files found here: https://github.com/buildingSMART/Sample-Test-Files
It can also be found in the directory "Sources".

## Key Features

* IFC → CSV data pipeline using Python (ifcopenshell)
* Real-time element selection using ray tracing
* Hierarchical actor resolution (mesh → IFC parent mapping)
* Interactive metadata panel:

  * Type
  * Material
  * Volume, Area, Length
  * Cost estimation
* Structure visibility toggles
* Teleportation system (multi-location navigation)
* Time-of-day lighting control
* Screenshot capture system

---

## Technical Highlights

* Built using Unreal Engine (Blueprint-driven interaction system)
* Custom data pipeline:

  * IFC parsing → CSV → Unreal DataTable
* Solved real-world issues:

  * Hidden actor selection conflicts
  * IFC hierarchy vs Unreal actor structure mismatch
  * Missing metadata handling (fallback + UI handling)

---

## Workflow

1. Parse IFC files using Python (ifcopenshell)
2. Extract element properties (type, material, quantities)
3. Convert to CSV
4. Import into Unreal as DataTable
5. Map data to actors using naming conventions
6. Enable interaction and UI display at runtime

---

## Demo

https://youtu.be/yEsG3Iu3utA

---

## Screenshots

![Overview](Images/Overview.png)
![House_Structure_Info](House_Structure_Info.png)
![Bridge_Structure_Info](Images/Bridge_Structure_info.png)

---

## Future Improvements

* BIM category filtering (walls, slabs, etc.)
* Improved material-based highlighting
* Simulation/validation layer integration

---

## Author

Ravi Rajan
Unreal Developer (Virtual Production & Real-Time Systems)
