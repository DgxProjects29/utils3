from core.commands_templates import Utils3Exception
import json
import datetime

USER_SUBJECS_PATH = 'data/dsmodule_data/utils3-ds-user-structure.json'
UTILS3_DS_STRUCTURE = 'data/dsmodule_data/utils3-ds-structure.json'
UTILS3_DS_MAPID = 'data/dsmodule_data/utils3-ds-mapid.json'

def load_data_from_json_file(file_path, 
    file_not_found_message = "",
    parse_error_message = ""):

    if not file_not_found_message:
        file_not_found_message = "We couldn't find the following file {file}".\
        format(file = file_path)

    if not parse_error_message:
        parse_error_message = "Your json file is not written properly"

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

def get_title_for_files(tags = []):
    
    current_date = datetime.datetime.now()
    title = current_date.strftime("%y%m%d%H%M%S")

    for tag in tags:
        title += "-{0}".format(tag)

    return title
