def create_hero_document(data):
    return {
        "name": data["name"],
        "real_name": data.get("real_name"),
        "year": data["year"],
        "universe": data["universe"],  # 'DC' o 'Marvel'
        "biography": data["biography"],
        "equipment": data.get("equipment", []),
        "images": data["images"]  # Lista de URLs
    }
