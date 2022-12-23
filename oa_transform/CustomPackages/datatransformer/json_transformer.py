import pandas as pd

def JSONTransform(json_list: list,
                  normal_columns_json_to_parse: list,
                  pk: list) -> tuple[pd.DataFrame, pd.DataFrame]:

    combined_json = pd.DataFrame().from_records(json_list)
    main_df = combined_json[normal_columns_json_to_parse]

    return main_df, pk