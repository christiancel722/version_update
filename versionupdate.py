import json
import urllib.request
import os
import time
import subprocess

def check_for_update(current_version):
    update_url = "https://raw.githubusercontent.com/christiancel722/version_update/main/version_update1.json"
    try:
        response = urllib.request.urlopen(update_url)
        data = json.load(response)
        latest_version = data["version"]
        if latest_version > current_version:
            return latest_version, data["download_link"]
    except Exception as e:
        print("Error al verificar actualizaciones:", e)
    return None, None

def download_update(download_link):
    try:
        response = urllib.request.urlopen(download_link)
        new_exe_content = response.read()
        
        with open("EasyChk.exe", "wb") as f:
            f.write(new_exe_content)
        
        print("Descargando actualización:")
        for i in range(1, 101):
            time.sleep(0.1)  # Simulando descarga (puedes ajustar este valor)
            print(f"\rProgreso: {i}% ", end="", flush=True)
        
        print("\nActualización descargada con éxito.")
        return True
    except Exception as e:
        print("Error al descargar la actualización:", e)
        return False

if __name__ == "__main__":
    current_version = "1.0"  # Cambia esto a la versión actual de tu programa
    latest_version, download_link = check_for_update(current_version)
    
    if latest_version:
        print("Nueva versión disponible:", latest_version)
        print("El programa se actualizará automáticamente en 2 segundos...")
        time.sleep(2)
        
        if download_update(download_link):
            print("Ejecutando la nueva versión del programa...")
            subprocess.run(["new_program.exe"])  # Ejecuta el nuevo ejecutable
            print("El programa se ha actualizado y ejecutado.")
    else:
        print("No hay actualizaciones disponibles.")
