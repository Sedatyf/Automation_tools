import os, glob
import termcolor, tqdm
import custom_tools

#Global variable
given = []
when = []
then = []

#Script
def main(feature, java):
    filepath_feature = feature
    custom_tools.check_folder(filepath_feature)
        
    filepath_steps = java
    custom_tools.check_folder(filepath_steps)

    custom_tools.parse_feature_file(filepath_feature, given, when, then)
    custom_tools.write_in_file(filepath_steps, given, when, then)
    termcolor.cprint("Tous les tests ont été traités !", "green")