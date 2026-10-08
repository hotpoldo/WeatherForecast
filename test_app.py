from app import get_weather_data

def test_weather_api_status():
    
    response = get_weather_data()
    # Verifica che l'API risponda correttamente (Status Code 200)
    assert response.status_code == 200