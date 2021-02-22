import configparser


def write_config():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'chromedriverPath': '/home/marian/Programming/courseAutomation/chromedriver', 'outputFile': 'video.mp4'}
    config['Alfaview'] = {'username': 'Marian', 'room': 'in-02', 'alfaviewSkipUpdate': 'true'}
    config['Buttons'] = {'open_alfaview_button': 'buttons_to_find/open_button.png', 'skip_update_button': 'buttons_to_find/skip_update_button.png', 'join_room_button': 'buttons_to_find/join_room_button.png'}
    config['rooms'] = {'in-01': 'https://app.alfaview.com/#/join/hochschule-furtwangen-furtwangen-university/1854212c-ce4b-47e5-8dcd-e504a5dee940/bd0fa7ba-efa5-4bc8-8f21-b797184020cd', 'in-02': 'https://app.alfaview.com/#/join/hochschule-furtwangen-furtwangen-university/5fa8632d-b4d7-44c4-9b1b-c88960333589/7200232b-a57a-46dc-9436-ffa1f61a3d00'}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)



def get_config_string(section, name):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config[section][name]

def get_config_double(section, name):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return int(config[section][name])

def get_config_bool(section, name):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return bool(config[section][name])


write_config()
