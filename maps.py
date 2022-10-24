import folium 

bangladesh = folium.Map(location=[23.777176, 90.399452], zoom_start = 14, control_scale=True, tiles='stamenterrain')
folium.Marker([23.7667,90.3781], popup = "Chandrima Uddan", icon=folium.Icon(color="blue", icon="info-sign")).add_to(bangladesh)

print ( bangladesh._repr_html_() ) 


#https://jtemporal.com/folium/#:~:text=O%20folium.Marker%20%28%29%20coloca%20um%20%E2%80%9Cpin%E2%80%9D%20de%20localiza%C3%A7%C3%A3o,metodo%20add_to%20%28%29.%20Chamando%20nomavente%20o%20mapa%2C%20temos%3A
