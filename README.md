<img src="./source/img/context.png" alt="logo" width="800" style="margin:auto;display:block"/>

The code provided in this git repository allows for the reproduction of the results presented in the paper "Exploring the Direct and Indirect Environmental Impacts of Mobile Health – A Case Study on Continuous Glucose Monitoring," published as part of the ICT4S 2025 conference. It primarily relies on functions developed by the [lca algebraic](https://github.com/oie-mines-paristech/lca_algebraic) library, which itself builds upon [brightway2](https://docs.brightway.dev/en/latest/). Our warmest thanks go to the contributors of these two libraries, without whom this work would not have been possible.

The life-cycle data used to build the foreground systems for each scenario defined in the paper are stored in the Excel file life_cycle_data.xlsx, specifically in the sheets A0, A1, A2, A3, and B. This Excel file also includes the definitions of custom activities (absent from ecoinvent) developed to address the specific modeling needs of this case study. In addition, it identifies the ecoinvent activities that require modification, providing only the flows that need to be adjusted to improve representativeness within the context of the study.

This structure is intended to keep the data (in Excel) as separate as possible from the model assembly and computation (in the Jupyter Notebook), in order to improve manageability and enhance reproducibility and transparency.

Two additional custom functions are required to read the lifecycle data from life_cycle_data.xlsx. These functions, located in external_functions.py, help streamline parameter creation and make it easier to identify and retrieve relevant activities.

The foreground folder contains lists of activities that require different scaling factors depending on the scenario. For example, in scenario A2, flows related to the applicator must be distinguished from those associated with the CGM device.

Please note that a license for the ecoinvent database is required, as it served as the LCI data source for this study. The version used for this work is ecoinvent 3.9.1.

# Installation

To run the full code, you'll need a working Python environment with the following packages: brightway2 and lca_algebraic. For installing lca_algebraic, we recommend following the steps outlined [here](https://github.com/oie-mines-paristech/lca_algebraic).

The modeling was developed using Jupyter Notebook. If you plan to use this interface, make sure to install both the jupyter and notebook packages.

*Note: Installing lca_algebraic on its own may cause an error. In some cases, installing brightway2 first and then lca_algebraic resolves the issue.*

# The code

Once the required libraries are installed, the code is fully commented to explain the purpose of each cell. This setup allows you to selectively regenerate results, scenario by scenario.