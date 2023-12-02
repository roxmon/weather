#!/usr/bin/env python

# use the dotenv library to get the env variable storing the API key
from dotenv import load_dotenv
import os
import requests

# we are working with an API. Our key to have access to the data is stored in another file named ".env"
load_dotenv()
token = os.environ.get("api-token")

# URL links of the API
current_url = "http://api.weatherapi.com/v1/current.json"
forecast_url = "http://api.weatherapi.com/v1/forecast.json"

# we define the main function of the code
def main():

    # program runs indefinitely
    while(True):
        # here are some options the user can choose
        print("\nHere are your options:\n")
        print("1: Get current weather")
        print("2: Get forecast weather")
        print("3: Get past weather")
        print("4: Exit the program")

        #the user gives the number of the option he wants to execute
        option = input("\nWhat do you want to do? ")
        # check if the input is a number
        if not option.isnumeric():
            print("\nYou have to enter a integer!\n")
            continue    # the program continue / restart, the user has to choose an option

        # if the input is a number, take the integer format
        option = int(option)

        # the fourth option of the programm is to quit it, the program stops
        if option == 4:
            exit()

        # once the option is chosen, the user enter the name of the city for which he wants weather data
        city = input("\nEnter the name of a city: ")

        # if the option is to obtain data about the current weather in the city
        if option == 1:
            # construct a dictionary to store the argument of the API call
            data = {
                'key': token,
                'q': city
            }
            # run the API call and get the data
            api_call = requests.get(current_url, data)
            # check the success of the API call (code 200=success)
            if api_call.status_code == 200:
                # get the response as JSON format
                response = api_call.json()
                # take the infos we want from the data and print
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
            # the user is asked to enter the number of days they want the forecast for
            forecast_days = input("Enter the number of days for forecast (1-10): ")
            data = {
                'key': token,   # key is defined to be the API token
                'q': city,  # q is defined to be the city that was entered by the user
                'days': forecast_days   # days is defined to be the number of days the user wants the forecast for
            }
            # the API call is made to the forecast API, the parameters are defined to be the ones specified as the data above
            api_call = requests.get(forecast_url, params=data)
            # check the success of the API call (code 200=success)
            if api_call.status_code == 200:
                response = api_call.json()  # get the response as JSON format
                forecast_data = response['forecast']['forecastday'] # the forecast information is set to be forecast_data
                # for each of the days the date, the maximum and minimum temperature and a short description of the weather is retrieved
                for day in forecast_data:
                    date = day['date']
                    max_temp = day['day']['maxtemp_c']
                    min_temp = day['day']['mintemp_c']
                    condition_text = day['day']['condition']['text']
                    print(f"\nDate: {date}")
                    print(f"Max temperature in °C: {max_temp}")
                    print(f"Min temperature in °C: {min_temp}")
                    print(f"Condition: {condition_text}")
            else:
                # if it fails to retrieve the data this is also stated
                print("Failed to retrieve forecast data.")

        if option == 3:
            data = {
                'key': token,
                'q': city
            }
            api_call = requests.get(current_url, data)
            print(api_call.json())



if __name__ == "__main__":
    main()
