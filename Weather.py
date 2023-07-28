import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data.")
        return None

def get_weather_by_date(data, date):
    for entry in data['list']:
        if date in entry['dt_txt']:
            return entry['main']['temp']
    return None

def get_wind_speed_by_date(data, date):
    for entry in data['list']:
        if date in entry['dt_txt']:
            return entry['wind']['speed']
    return None

def get_pressure_by_date(data, date):
    for entry in data['list']:
        if date in entry['dt_txt']:
            return entry['main']['pressure']
    return None

def main():
    data = get_weather_data()
    if not data:
        return

    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_weather_by_date(data, date)
            if temperature:
                print(f"Temperature on {date}: {temperature} K")
            else:
                print("Data not available for the given date.")

        elif choice == '2':
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed_by_date(data, date)
            if wind_speed:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Data not available for the given date.")

        elif choice == '3':
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure_by_date(data, date)
            if pressure:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not available for the given date.")

        elif choice == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
