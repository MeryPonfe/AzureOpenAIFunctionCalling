def search_hotels(location, max_price=None, features=None):  
    # Ejemplo de hoteles  
    hotels = [  
        {  
            "name": "Hotel Seattle",  
            "location": "Seattle",  
            "price": 150,  
            "features": ["free wifi", "beachfront"]  
        },  
        {  
            "name": "Hotel Bellevue",  
            "location": "San Diego",  
            "price": 100,  
            "features": ["free wifi", "pool", "beachfront"]  
        },  
        {  
            "name": "Hotel Redmond",  
            "location": "Seattle",  
            "price": 200,  
            "features": ["beachfront", "pool"]  
        }  ,  
        {  
            "name": "Hotel Hilton",  
            "location": "San diego",  
            "price": 350,  
            "features": ["parking", "pool","spa"]  
        }  
    ]  
  
    # Hotels by location 
    filtered_hotels = [hotel for hotel in hotels if hotel["location"] == location]  
  
    # Hotels by max price  
    if max_price is not None:  
        filtered_hotels = [hotel for hotel in filtered_hotels if hotel["price"] <= max_price]  
  
    # hotels by features   
    if features:  
        feature_list = features.split(", ")  
        filtered_hotels = [hotel for hotel in filtered_hotels if all(feature in hotel["features"] for feature in feature_list)]  
  
    return filtered_hotels  
  
def format_hotel_info(hotels):  
    if not hotels:  
        return "I am so sorry, I can't find any hotel with this features."
    result = ""  
    for hotel in hotels:  
        name = hotel["name"]  
        location = hotel["location"]  
        price = hotel["price"]  
        features = ", ".join(hotel["features"])  
  
        hotel_info = f"Name: {name}\nLocation: {location}\nPrice: ${price}\nFeature: {features}\n\n"  
        result += hotel_info  
    return result  