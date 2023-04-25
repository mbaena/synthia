import os
import shutil
from github_utils import get_github_repo, create_branch, commit_and_push_changes, create_pull_request,\
    is_pull_request_merged
from main import request_modified_code_from_agent

def modify_code_and_create_pull_request(file_name, functionality):
    # Configurar variables del proyecto
    repo_name = "mbaena/synthia"
    branch_name = "ia-modification"
    commit_message = "Código modificado por la IA"
    pull_request_title = "Revisión de código: Cambios propuestos por la IA"
    pull_request_body = "La IA ha propuesto cambios en el código. Por favor, revise y apruebe o rechace estos cambios."

    # Clonar el repositorio y crear una nueva rama
    repo = get_github_repo(repo_name)
    git_repo = create_branch(repo, branch_name)

    #Modificar el código utilizando la IA
    project_path = os.path.join(".", branch_name)
    with open(os.path.join(project_path, file_name), "r") as f:
        original_code = f.read()
        modified_code = request_modified_code_from_agent(original_code, functionality)

    # Guardar los cambios en la nueva rama
    with open(os.path.join(project_path, file_name), "w") as f:
        f.write(modified_code)

    # Realizar commit y push de los cambios a la rama
    commit_and_push_changes(git_repo, branch_name, commit_message)

    # Crear una solicitud de extracción
    pull_request = create_pull_request(repo, branch_name, pull_request_title, pull_request_body)

    # Limpiar el directorio del proyecto local
    shutil.rmtree(project_path)

    print(f"Solicitud de extracción creada: {pull_request.html_url}")

    # import time
    # while True:
    #     time.sleep(60)  # Espere 60 segundos antes de verificar nuevamente el estado
    #     if is_pull_request_merged(repo, pull_request):
    #         print("La solicitud de extracción ha sido fusionada.")
    #         break
    #     else:
    #         print("La solicitud de extracción aún no ha sido fusionada. Esperando...")

# Uso de la función
file_name = "main.py"
functionality = "traducir al inglés"
modify_code_and_create_pull_request(file_name, functionality)
