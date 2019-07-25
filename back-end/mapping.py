restaurant_mapping = ''' 
{
    "mappings": {
        "properties": {
            "address": {
                "type": "text"
            },
            "country": {
                "type": "text"
            },
            "cuisine": {
                "type": "text"
            },
            "email": {
                "type": "text"
            },
            "fax": {
                "type": "text"
            },
            "hours": {
                "properties": {
                    "friday": {
                        "type": "text"
                    },
                    "monday": {
                        "type": "text"
                    },
                    "saturday": {
                        "type": "text"
                    },
                    "sunday": {
                        "type": "text"
                    },
                    "thursday": {
                        "type": "text"
                    },
                    "tuesday": {
                        "type": "text"
                    },
                    "wednesday": {
                        "type": "text"
                    }
                }
            },
            "latitude": {
                "type": "float"
            },
            "locality": {
                "type": "text"
            },
            "longitude": {
                "type": "float"
            },
            "meal_breakfast": {
                "type": "boolean"
            },
            "meal_deliver": {
                "type": "boolean"
            },
            "meal_dinner": {
                "type": "boolean"
            },
            "meal_lunch": {
                "type": "boolean"
            },
            "meal_takeout": {
                "type": "boolean"
            },
            "name": {
                "type": "text"
            },
            "options_glutenfree": {
                "type": "boolean"
            },
            "options_healthy": {
                "type": "boolean"
            },
            "options_organic": {
                "type": "boolean"
            },
            "options_vegan": {
                "type": "boolean"
            },
            "options_vegetarian": {
                "type": "boolean"
            },
            "parking": {
                "type": "boolean"
            },
            "parking_free": {
                "type": "boolean"
            },
            "parking_garage": {
                "type": "boolean"
            },
            "parking_street": {
                "type": "boolean"
            },
            "price": {
                "type": "text"
            },
            "rating": {
                "type": "float"
            },
            "region": {
                "type": "text"
            },
            "restaurant_id": {
                "type": "long"
            },
            "tel": {
                "type": "text"
            },
            "website": {
                "type": "text"
            },
            "wifi": {
                "type": "boolean"
            }
        }
    }
}'''

review_mapping = ''' 
{
    "mappings": {
        "properties": {
            "restaurant_id": {
                "type": "long"
            },
            "review_date": {
                "type": "text"
            },
            "review_rating": {
                "type": "long"
            },
            "review_text": {
                "type": "text"
            },
            "review_title": {
                "type": "text"
            },
            "review_url": {
                "type": "text"
            },
            "review_website": {
                "type": "text"
            }
        }
    }
}'''
