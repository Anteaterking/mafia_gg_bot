import yaml
import random


# This will only work if the setup for your yaml file is structured the same way as the
# given yaml files.

def load_yaml(player_count):
    """Loads the setup for the passed player count into Python

    Parameters
    ----------
    player_count: int
        The number of players in the game

    Returns
    -------
    setup
        An dict representing the loaded yaml file
    """

    file_name = ('etc/' + str(player_count) + '.yaml')
    with open(file_name, 'r') as stream:
        setup = yaml.safe_load(stream)
        return setup


def setup_pipeline(setup_list):
    """Takes a previously loaded object and returns the values within for ease of use

    Parameters
    ----------
    setup_list: Object
        An Object of a yaml file with a specific layout

    Returns
    -------
        setup_name
            A string representing the name of the setup
        setup_link
            A string representing the link to the setups description
        setup_settings
            A list representing the options needed for the setup
        setup_codes
            A list representing the possible codes for the setup
    """

    random_setup = random.randint(0, 0)  # this is 0, 0 for now because well, I only have 1 setup for each
    current_setup = setup_list[random_setup]
    setup_name = current_setup['name']
    setup_link = current_setup['link']
    setup_settings = current_setup['settings']
    setup_codes = current_setup['codes']
    return setup_name, setup_link, setup_settings, setup_codes


def random_code(code_list):
    """Selects a random code from the possible options

    Parameters
    ----------
    code_list
        A list of the possible codes

    Returns
    -------
    selected_code
        The randomly selected code to use for this game
    """

    selected_code = code_list[random.randint(1, len(code_list))]  # selects a number from 1 - n (n = max possible setups)
    return selected_code


# planning on making an algorithm once you guys figure out an easy way to just get the value of a
# lobbies player count and then I'll have it pick a setup that is closest to that number

# SAMPLE USE IN MAIN
# from extract_setup_data import *
# name, link, settings, code_list = setup_pipeline(load_yaml(12)) # get the max player count put it here
# code = random_code(code_list)
