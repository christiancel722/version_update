import json
import urllib.request
import os

def check_for_update(current_version):
    update_url = "URL_DEL_ARCHIVO_JSON_CON_LA_INFORMACION_DE_ACTUALIZACION"
    try:
        response = urllib.request.urlopen(update_url)
        data = json.load(response)
        latest_version = data["version"]
        if latest_version > current_version:
            return latest_version, data["download_link"]
    except Exception as e:
        print("Error al verificar actualizaciones:", e)
    return None, None

def update_program(download_link):
    try:
        response = urllib.request.urlopen(download_link)
        new_program_content = response.read()
        with open("new_program.py", "wb") as f:
            f.write(new_program_content)
        print("Programa actualizado con éxito.")
        return True
    except Exception as e:
        print("Error al actualizar el programa:", e)
        return False

if __name__ == "__main__":
    current_version = "1.0"  # Cambia esto a la versión actual de tu programa
    latest_version, download_link = check_for_update(current_version)
    
    if latest_version:
        print("Nueva versión disponible:", latest_version)
        user_input = input("¿Deseas actualizar el programa? (y/n): ")
        if user_input.lower() == "y":
            update_program(download_link)
    else:
        print("No hay actualizaciones disponibles.")
