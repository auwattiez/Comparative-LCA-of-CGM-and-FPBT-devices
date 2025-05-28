"""
Processes the parameters in the given DataFrame and creates them.
Also registers parameters in a parameter registry.
"""

import pandas as pd
import lca_algebraic as agb

def process_parameters(params_df, parameter_registry):

    params_df["Type"] = params_df["Type"].astype(str).str.strip().str.lower()

    for index, row in params_df.iterrows():
        param_name = row["parameter"]
        param_type = row["Type"].strip().lower()

        if pd.isna(row["EI activity name"]):
            print(f"Skipping row {index} as 'EI activity name' is NaN.")
            break

        try:
            if param_type == "float":
                param = agb.newFloatParam(
                    param_name,
                    default=row["Default"],
                    min=row.get("Min"),
                    max=row.get("Max"),
                    std=row.get("Std"),
                    distrib=getattr(agb.DistributionType, row["Distrib"].upper(), None),
                    description=row.get("Description"),
                    label=row.get("Label")
                )
            elif param_type == "bool":
                param = agb.newBoolParam(
                    param_name,
                    default=row["Default"]
                )
            elif param_type == "enum":
                values = eval(row["Values"]) if isinstance(row["Values"], str) else row["Values"]
                weights = eval(row["Weights"]) if isinstance(row["Weights"], str) else None

                if weights:
                    values = {k: v for k, v in zip(values, weights)}

                param = agb.newEnumParam(
                    param_name,
                    values=values,
                    default=row["Default"],
                    description=row.get("Description")
                )
            else:
                raise ValueError(f"Unsupported parameter type: {param_type}")

            # Register the parameter for later evaluation
            parameter_registry[param_name] = param
            print(f"Parameter created and registered: {param_name}") # for debugging only !
        except Exception as e:
            print(f"Error creating parameter '{param_name}': {e}")



"""
This function finds activities in the ecoinvent database or in the User DB.
The latter contains either (1) custom activities or (2) modified ecoinvent activities.
"""

def find_activity(ei_activity_name, location, custom_process_name, modified_activity_name, custom_db):

    if pd.notna(modified_activity_name): # Check for the modified activities first
        try:
            modified_activity = agb.findActivity(modified_activity_name, db_name=custom_db)
            # print(f"Found activity '{modified_activity_name}' in custom database '{custom_db}'.") # for debugging only
            return modified_activity
        except Exception as e:
            print(f"Failed to find activity '{modified_activity_name}' in custom database '{custom_db}': {e}")

    if pd.notna(custom_process_name): # Check for the custom activity
        try:
            custom_process = agb.findActivity(custom_process_name, db_name=custom_db)
            # print(f"Found custom process '{custom_process_name}' in custom database '{custom_db}'.") # for debugging only
            return custom_process
        except Exception as e:
            print(f"Failed to find custom process '{custom_process_name}' in custom database '{custom_db}': {e}")

    try: # Fallback to the native Ecoinvent database, if the activity is not custom or modified
        if pd.notna(location):  # If location is provided
            return agb.findTechAct(ei_activity_name, loc=location)
        else:
            return agb.findTechAct(ei_activity_name)
    except Exception as e:
        print(f"Failed to find activity '{ei_activity_name}' in Ecoinvent for location '{location}': {e}")
        return None
