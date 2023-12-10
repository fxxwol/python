from art_menu import ArtMenu
import sys
import os
from core.lab_7.services import DisplayInTableService, UserService

sys.path.append(os.getcwd())
import utils.json_handling as json_processor
import utils.colors_handling as color_processor
from utils.input_handling import get_string_input
import json
from classes.file_processor import FileProcessor


class DataDisplayMenu(ArtMenu):
    def __init__(self):
        self.history = []
        self.successful_result = False
        self.jsons = []

    def display_personal_profile(self, linkedin_url):
        try:
            self.jsons = UserService.get_personal_profile(linkedin_url)
            print("Choose an option:")
            print("1. Display data in a flattened way")
            print("2. Display data in JSON format")
            print("3. Display data in a table")
            while True:
                option = self.get_option()
                if option == "1":
                    color_processor.display_colors()
                    color_position = int(input("Enter a color position: "))
                    json_processor.display_flattened_json(self.jsons, color_position)
                    break
                elif option == "2":
                    print(json.dumps(self.jsons, indent=4))
                    break
                elif option == "3":
                    print(
                        DisplayInTableService.display_personal_profile(
                            json.dumps(self.jsons, indent=4)
                        )
                    )
                    break
                else:
                    print("Invalid option. Enter again!")
            self.history.append(
                f"Data of a personal profile where URL is {linkedin_url}:\n{json.dumps(self.jsons, indent=4)}"
            )
            self.successful_result = True
        except ValueError as e:
            print(e)
            self.successful_result = False

    def display_profiles_posts(self, linkedin_url):
        try:
            self.jsons = UserService.get_profiles_posts(linkedin_url)
            print("Choose an option:")
            print("1. Display data in a flattened way")
            print("2. Display data in JSON format")
            print("3. Display data in a table")
            while True:
                option = self.get_option()
                if option == "1":
                    color_processor.display_colors()
                    color_position = int(input("Enter a color position: "))
                    json_processor.display_flattened_json(self.jsons, color_position)
                    break
                elif option == "2":
                    print(json.dumps(self.jsons, indent=4))
                    break
                elif option == "3":
                    print(
                        DisplayInTableService.display_profiles_posts(
                            json.dumps(self.jsons, indent=4)
                        )
                    )
                    break
                else:
                    print("Invalid option. Enter again!")
            self.history.append(
                f"Data of a personal profile where URL is {linkedin_url}:\n{json.dumps(self.jsons, indent=4)}"
            )
            self.successful_result = True
        except ValueError as e:
            print(e)
            self.successful_result = False

    def save_data_to_json(self):
        if self.successful_result:
            try:
                filename = get_string_input("Enter file name:")
                file_processor = FileProcessor(filename)
                file_processor.write_into_json(self.jsons)
            except Exception as e:
                print(e)
        else:
            print("No data to save!")

    def display_history(self):
        if len(self.history) == 0:
            print("No history!")
        else:
            for counter, item in enumerate(self.history):
                print(f"{counter + 1}: {item}")

    def run(self):
        while True:
            print("Choose an option:")
            print("1. Display data of a personal profile")
            print("2. Display data of profiles posts")
            print("3. Save data in JSON format")
            print("4 - Show history")
            print("0 - Exit")

            option = self.get_option()
            if option == "1":
                linkedin_url = input("Enter LinkedIn URL: ")
                self.display_personal_profile(linkedin_url)
            elif option == "2":
                linkedin_url = input("Enter LinkedIn URL: ")
                self.display_profiles_posts(linkedin_url)
            elif option == "3":
                self.save_data_to_json()
            elif option == "4":
                self.display_history()
            elif option == "0":
                exit(0)
            else:
                print("Invalid option. Enter again!")
