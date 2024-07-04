import configparser
import os

def read_config():
    # Create a ConfigParser object
    config = configparser.ConfigParser()
 
    # Read the configuration file
    ini_path = os.path.join(os.getcwd(),'config.ini')
    config.read(ini_path)
    # db_host = config.get('Database', 'host')
    # db_port = config.get('Database', 'port')
    # db_name = config.get('Database', 'database')
    # db_user = config.get('Database', 'user')
    # db_password = config.get('Database', 'passwd')
    # loop_range = config.get('General', 'loop_range')
 
    # Return a dictionary with the retrieved values
    config_values = {
        'db_name': config.get('Database', 'database'),
        'db_host': config.get('Database', 'host'),
        'db_port': config.get('Database', 'port'),
        'db_user': config.get('Database', 'user'),
        'db_password': config.get('Database', 'passwd'),
        'loop_range': config.get('General', 'loop_range'),
        'failed_login_array': config.get('General', 'failed_login_array')
    }
    return config_values
 
