# function that calculation the weather

import math

def calculate_weather_index(temperature, humidity):
    """
    Calculate a weather index based on temperature and humidity.
    
    Args:
        temperature (float): The temperature in degrees Celsius.
        humidity (float): The humidity percentage (0-100).
        
    Returns:
        float: The calculated weather index.
    """
    if not isinstance(temperature, (int, float)) or not isinstance(humidity, (int, float)):
        raise ValueError("Temperature and humidity must be numbers.")
    
    if humidity < 0 or humidity > 100:
        raise ValueError("Humidity must be between 0 and 100.")
    
    # Example formula for weather index
    index = temperature + (0.1 * humidity) - 10
    return round(index, 2)


# Needle in a haystack problem