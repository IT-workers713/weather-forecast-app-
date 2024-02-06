import requests

api_key="f0970471ea7edc150a01ea45e4fc2298"
def get_data(place,forecast_days=None,kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    #f0970471ea7edc150a01ea45e4fc2298
    response = requests.get(url)
    data = response.json()
    filtred_data = data["list"]
    nr_values = 8*forecast_days
    filtred_data = filtred_data[:nr_values]
    return filtred_data
if __name__== "__main__":
    print(get_data(place="Tokyo",forecast_days=3,kind="Temperature"))