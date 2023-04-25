import openai
import config

# Setting up OpenAI API keys
openai.api_key = config.OPENAI_API_KEY


def request_modified_code_from_agent(original_code, functionality):
    """
    This function makes a request to the GPT-3.5-turbo API to modify the provided code
    according to the requested functionality.

    Args:
        original_code (str): The original Python code provided by the user.
        functionality (str): The specific request to modify the code.

    Returns:
        str: The modified Python code according to the request.
    """
    system_prompt = (f"""
    User provide the Python script and an action you would like to perform on it. The script should align with the following requirements:
    The script will be written as the main file, without comments, and as efficient as possible.
    """)

    # Parameters for the GPT-3 API request
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

    # Generating modified code using GPT-3 API
    response = openai.Completion.create(**parameters)
    modified_code = response.choices[0].text
    return modified_code


def generate_modified_code(original_code):
    """
    This function is a container for request_modified_code_from_agent, providing
    an additional layer of abstraction in case any additional processing
    needs to be done in the future.

    Args:
        original_code (str): The original Python code provided by the user.

    Returns:
        str: The modified Python code according to the request.
    """
    modified_code = request_modified_code_from_agent(original_code, "translate to English")
    return modified_code


def main():
    # Loading the original code from a file
    with open("main.py", "r") as f:
        original_code = f.read()

    # Generating the modified code
    modified_code = generate_modified_code(original_code)

    # Writing the modified code to a file
    with open("modified_main.py", "w") as f:
        f.write(modified_code)


# Runs the main function if the script is called directly
if __name__ == "__main__":
    main()