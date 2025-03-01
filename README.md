# Comparative-LCA-of-CGM-and-FPBT-devices
Comparative life cycle assessment of two glucose monitoring devices.

The CGM and FPBT devices are modeled in the Excel file "data", where foreground modeling is highlighted in yellow.

- CGM devices: Scenario A0 represents the business-as-usual model, while A1–A3 explore ecodesign alternatives.
- FPBT devices: Modeled under scenario B.

The analysis follows a cradle-to-patient's-gate approach, including:

- Environmental impact estimation in a typical case.
- Contribution (hotspot) analysis.
- Uncertainty analysis using the LCA algebraic package, built on top of Brightway 2.

Relevant code/documents are structured as follows:

- "modelling" notebook: Contains code specific to the LCA model.
- "assumptions" document: Details key modeling assumptions.
- "additional resources" folder: Includes extra scripts for inventory generation.

To run the notebook, ensure a working environment for Brightway 2 and LCA algebraic. For installation guidance, please refer to this tutorial.
