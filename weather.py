#!/usr/bin/env python

from dotenv import load_dotenv
import os
import requests

load_dotenv()
token = os.environ.get("api-token")

url = "http://api.weatherapi.com/v1/current.json"

def main():

    while(True):
        print("\nHere are your options:\n")
        print("1: Get current weather")
        print("2: Get forecast weather")
        print("3: Get past weather")
        print("4: Exit the program")
        option = input("\nWhat do you want to do? ")
        if not option.isnumeric():
            print("\nYou have to enter a integer!\n")
            continue

        option = int(option)

        if option == 4:
            exit()

        city = input("\nEnter the name of a city: ")

        if option == 1:
            data = {
                'key': token,
                'q': city
            }
            api_call = requests.get(url, data)
            if api_call.status_code == 200:
                response = api_call.json()
                name = response['location']['name']
                region = response['location']['region']
                localtime = response['location']['localtime']
                temp_c = response['current']['temp_c']
                is_day = response['current']['is_day']
                condition_text = response['current']['condition']['text']

                print(f"\nCity: {name}, {region}")
                print(f"Localtime: {localtime}")
                print(f"Temperature in °C: {temp_c}")
                print(f"Is day: {bool(is_day)}")
                print(f"Condition: {condition_text}")

        if option == 2:
            data = {
                'key': token,
                'q': city
            }
            api_call = requests.get(url, data)
            print(api_call.json())

        if option == 3:
            data = {
                'key': token,
                'q': city
            }
            api_call = requests.get(url, data)
            print(api_call.json())



if __name__ == "__main__":
    main()
