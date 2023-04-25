import requests
import json


def send_code_and_receive_feedback(code_to_modify):
    url = "http://localhost:8000/modify-code"
    payload = {"code": code_to_modify}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        modified_code = response.json()["modified_code"]
        return modified_code
    else:
        print(f"Error: {response.status_code}")
        return None


# Ejemplo de uso
original_code = """print("Hello, World!")"""
modified_code = send_code_and_receive_feedback(original_code)

if modified_code:
    print("Código modificado:")
    print(modified_code)
