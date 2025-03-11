from qgis.core import QgsProject

# имя слоя   
layer_name = "poi-point"  

# получение слоя из проекта
layer = QgsProject.instance().mapLayersByName(layer_name)[0]

# задание ключевых значений атрибута 'amenity'/'type' для социальных объектов
social_amenities = {"school", "hospital", "library", "kindergarten", 
"college", "driving_school", "training", "music_school", "university",
"bus_station", "vehicle_inspection", "driver_training", "ferry_terminal",
"fuel", "atm", "payment_terminal", "bank", "money_transfer", 
"payment_centre", "clinic", "dentist", "doctors", "nursing_home", "pharmacy",
"social_facility", "veterinary", "arts_centre", "cinema", "community_centre",
"stage", "theatre", "courthouse", "fire_station", "police", "post_box", 
"post_office", "toilets", "crematorium", "grave_yard", "marketplace"}

# фильтрация объектов
filtered_features = []
for feature in layer.getFeatures():
    if(feature["amenity"]):
        attrs = feature.__geo_interface__
        
        if feature["amenity"] in social_amenities:
            attrs = feature.__geo_interface__
            
            print(feature["amenity"])
            
            # добавление социального объекта в список результатов
            filtered_features.append(feature)

# количество социальных объектов
print(f"Найдено {len(filtered_features)} социальных объектов")
