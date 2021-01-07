import json
from core.commands_templates import Utils3Exception

SETTINGS_PATH = 'data/settings.json'

def load_data_from_json_file(file_path, 
    file_not_found_message = "",
    parse_error_message = ""):

    if not file_not_found_message:
        file_not_found_message = "Couldn't find the following file {file}".\
        format(file = file_path)

    if not parse_error_message:
        parse_error_message = "Json file is not written properly"

    try:
        with open(file_path, 'r', encoding='utf8') as read_file:
            return json.load(read_file)
    except FileNotFoundError:
        raise Utils3Exception(file_not_found_message)
    except json.decoder.JSONDecodeError:
        raise Utils3Exception(parse_error_message)


def write_json_from_dict(file_path, data): 
    with open(file_path, "w", encoding='utf8') as write_file:
        json.dump(data, write_file, indent=4, ensure_ascii=False)

def set_setting(key, value):
    settings = load_data_from_json_file(SETTINGS_PATH)
    settings[key] = value
    write_json_from_dict(SETTINGS_PATH, settings)


def get_setting(key):
    settings = load_data_from_json_file(SETTINGS_PATH)
    if key in settings:
        return settings[key]
    else:
        raise Utils3Exception(
            f"The following setting {key} couldn't be found"
        )
