#Print the dictionary in the format: "The zip code for [City] is [Zip]"
cities={"sultanpur":24323,
        "allahabad":74763,
        "pratapgarh":43652,
        "amethi":54257,
        "ayodhya":96545
        }
for city,zip_code in cities.items():
    print("the zip_code for", city ,"is", zip_code)