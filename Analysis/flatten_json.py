import json
import requests
import pandas as pd

def get_json():
    response = requests.get("https://api.tfl.gov.uk/BikePoint/")
    response = json.loads(response.content)
    return response


def all_columns_are_converted(data_frame):
    return json not in get_dataframe_datatypes(data_frame).values() and \
            list not in get_dataframe_datatypes(data_frame).values()

def get_dataframe_datatypes(data_frame):
    return {i : type(data_frame[i][0]) for i in list(data_frame.columns)}

def get_columns_that_need_converting(data_frame):
    datatypes = get_dataframe_datatypes(data_frame)
    return [i for i in datatypes if datatypes[i] in [list, dict]]

def parse_further_columns(data_frame, all_frames):
    for coli in data_frame.keys():
        converted_data_frame = pd.json_normalize(data_frame[[coli]])

        if not all_columns_are_converted(converted_data_frame):
            sub_columns = get_columns_that_need_converting(converted_data_frame)
            additional_dataframes = parse_further_columns(converted_data_frame[sub_columns], all_frames)
            for i in additional_dataframes:
                all_frames.append(i)
        else:
            return converted_data_frame

    return all_frames

def process_json_dict():
    final_output_tables = {}

    # file = open("ldn_api_output")
    # json_string = file.read()
    # converted_json = json.loads(json_string)
    converted_json = get_json()

    first_converted_dataframe = pd.json_normalize(converted_json)

    if not all_columns_are_converted(first_converted_dataframe):
        sub_columns = get_columns_that_need_converting(first_converted_dataframe)
        additional_dataframes = []
        for additional_column in sub_columns:
            additional_dataframe = parse_further_columns(first_converted_dataframe[additional_column], [])
            additional_dataframes.append(additional_dataframe)


    print(final_output_tables)



if __name__ == "__main__":
    process_json_dict()