import json
from log import logout

def init_setting():
    with open("settings.json", 'r') as file_settings:
        _settings_json = file_settings.read()
    
    _settings = json.loads(_settings_json)
    logout(_settings, 0) # LOGGING
    return _settings

def select_language(lang):
    file_path = "locales/" + lang + ".json"
    
    with open(file_path, 'r') as file_lang:
        _lang_json = file_lang.read()
    
    _lang = json.loads(_lang_json)
    logout(_lang, 0) # LOGGING
    return _lang