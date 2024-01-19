import folium
import pandas as pd


df = pd.read_csv("volcano.txt")
latmean = df["LAT"].mean()
lonmean = df["LON"].mean()

map6 = folium.Map(location= [latmean,lonmean], zoom_start= 7)
def range_color(elev):
    if elev in range(0,1000):
        col = "green"
    elif elev in range(1001,2000):
        col = "orange"
    elif elev in range(2001,3000):
        col = "red"
    else:
        col = "purple"
    return col

for lat,lon,name,elev in zip(df["LAT"],df["LON"],df["NAME"],df["ELEV"]):
    folium.Marker(location=[lat,lon], popup= name, icon= folium.Icon(color= range_color(elev))).add_to(map6)


print(map6.save("test6.html"))

