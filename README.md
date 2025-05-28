<img src="./doc/source/img/context.png" alt="logo" width="200" style="margin:auto;display:block"/>

The code provided in this git repository allows for the reproduction of the results presented in the paper "Exploring the Direct and Indirect Environmental Impacts of Mobile Health – A Case Study on Continuous Glucose Monitoring," published as part of the ICT4S 2025 conference. It primarily relies on functions developed by the [lca algebraic](https://github.com/oie-mines-paristech/lca_algebraic) library, which itself builds upon [brightway2](https://docs.brightway.dev/en/latest/).

Our warmest thanks go to the contributors of these two libraries, without whom this work would not have been possible.

Two additional custom functions are needed to read the lifecycle data contained in the life_cycle_data.xlsx file. These functions, included in the external_functions.py file, help streamline parameter creation and make it easier to locate activities.

Please note that a license for the ecoinvent database is required, as it served as the LCI data source for this study.


# Installation

(blablabla)

= TALK ABOUT FOREGROUNDS

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
