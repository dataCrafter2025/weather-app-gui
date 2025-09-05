import tkinter as tk 
import requests 

def get_whether():
    city=city_entry.get() 
    api_key="72fafaf204e223c8b180561c517cdc23"
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
       response = requests.get(url)
       data = response.json()

       if data["cod"] != "404":
         weather = data["weather"][0]["description"].capitalize()
         temp = data["main"]["temp"]
         humidity = data["main"]["humidity"]
         wind_speed = data["wind"]["speed"]

         result = (
            f"Weather: {weather}\n"
            f"Temperature: {temp}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
         )

         result_label.config(text=result)
       else:
        result_label.config(text="City not found")
    except Exception as e:
     result_label.config(text=f"Error Fetching data: {e}")



root=tk.Tk()
root.title("Whether app")
root.geometry("320x250")


tk.Label(root,text="Enter City :",font=("Arial",12,"bold")).pack(pady=5)

city_entry=tk.Entry(root,font=("Aria",12))

city_entry.pack(pady=5)

tk.Button(root,text="Get Whether",font=("Arial",12,"bold"),command=get_whether,bg="lightblue").pack(pady=5)



result_label=tk.Label(root,text="" ,font=("Arial",12),justify="left")


result_label.pack(pady=10)

root.mainloop()





