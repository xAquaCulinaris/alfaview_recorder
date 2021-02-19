import configparser


def write_config():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'username': 'Marian', 'resoultionWidth': '1920','resoultionHeight': '1080','chromedriverPath': '/home/marian/Desktop/programming/alfaview_recorder/chromedriver', 'outputFile': 'video.mp4'}
    config['Alfaview'] = {'alfaviewResolutionWidth': '1920', 'alfaviewResolutionHeight': '1080', 'alfaviewSkipUpdate': 'true'}
    config['Buttons'] = {'open_alfaview_button': 'buttons_to_find/open_button.png', 'skip_update_button': 'buttons_to_find/skip_update_button.png', 'join_room_button': 'buttons_to_find/join_room_button.png'}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)




def get_config_string(section, name):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config[section][name]

def get_config_double(section, name):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config[section][name]


def get_config_bool(section, name):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config[section][name]

write_config()
