import requests
import json

# Define la URL de la API local de Ollama
url = "http://localhost:11434/api/generate"

# Configura el prompt para DeepSeek
prompt = "hola"

# Define los parámetros de la solicitud
payload = {
    "model": "deepseek-r1:8b",
    "prompt": prompt
}

# Envía la solicitud POST a la API de Ollama
response = requests.post(url, json=payload)

# Procesa la respuesta y muestra el resultado 
# muestra también si no es json
print(response.text)


# Procesa la respuesta
if response.status_code == 200:
    try:
        # Dividir la respuesta en líneas y procesar cada línea como JSON
        lines = response.text.splitlines()
        responses = []
        for line in lines:
            data = json.loads(line)
            if 'response' in data:
                responses.append(data['response'])
        
        # Concatenar todas las respuestas en una sola cadena
        final_response = ''.join(responses)
        print("Respuesta de DeepSeek:")
        print(final_response)
    except json.JSONDecodeError:
        print("Error: La respuesta no es un JSON válido")
else:
    print(f"Error: {response.status_code} - {response.text}")