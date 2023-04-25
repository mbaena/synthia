import openai
import config

# Configuración de las claves de API de OpenAI
openai.api_key = config.OPENAI_API_KEY


def request_modified_code_from_agent(original_code, functionality):
    """
    Esta función realiza una solicitud a la API de GPT-3.5-turbo para modificar el código proporcionado
    según la funcionalidad solicitada.

    Args:
        original_code (str): El código Python original proporcionado por el usuario.
        functionality (str): La solicitud específica para modificar el código.

    Returns:
        str: El código Python modificado según la solicitud.
    """
    system_prompt = (f"""
    User provide the Python script and an action you would like to perform on it. The script should align with the following requirements:
    The script will be written as the main file, without comments, and as efficient as possible.
    """)

    # Parámetros de la solicitud a la API de GPT-3
    parameters = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': f"action: \n{functionality};\n\n Python script: \n{original_code}"}
        ],
        "temperature": 0.5,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    # Generación del código modificado utilizando la API de GPT-3
    response = openai.ChatCompletion.create(**parameters)
    modified_code = response.choices[0].message.content
    return modified_code


def generate_modified_code(original_code):
    """
    Esta función es un contenedor para request_modified_code_from_agent, proporcionando
    una capa adicional de abstracción en caso de que se necesite realizar algún procesamiento
    adicional en el futuro.

    Args:
        original_code (str): El código Python original proporcionado por el usuario.

    Returns:
        str: El código Python modificado según la solicitud.
    """
    modified_code = request_modified_code_from_agent(original_code, "traducir al inglés")
    return modified_code


def main():
    # Carga del código original desde un archivo
    with open("main.py", "r") as f:
        original_code = f.read()

    # Generación del código modificado
    modified_code = generate_modified_code(original_code)

    # Escritura del código modificado a un archivo
    with open("modified_main.py", "w") as f:
        f.write(modified_code)


# Ejecuta la función principal si el script se llama directamente
if __name__ == "__main__":
    main()
