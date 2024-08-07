import requests
import json
import warnings
import sys
import pyperclip

#Ignora todas las advertencias, se puede eliminar a futuro
warnings.filterwarnings("ignore")

def get_datasets(url, api_key):
    headers = {"x-auth-token": api_key}
    response = requests.get(url + "/datasets", headers=headers, verify=False)
    return response.json()

def display_datasets(datasets):
    for i, dataset in enumerate(datasets, start=1):
        print(f"{i}. {dataset['name']}")
        print(f"   _id: {dataset['_id']}")
        print(f"   purpose: {dataset['purpose']}")
        print(f"   total_file_count: {dataset['total_file_count']}\n")

def main(url, api_key):
    datasets = get_datasets(url, api_key)
    
    #Verificar la cantidad de datasets obtenidos
    if len(datasets) == 0:
        print("No se encontraron datasets :(")
        return
    
    display_datasets(datasets)
    
    choice = int(input("Selecciona un número de la lista: "))
    if 1 <= choice <= len(datasets):
        selected_id = datasets[choice - 1]['_id']
        pyperclip.copy(selected_id)
        print(f"El _id '{selected_id}' ha sido copiado al portapapeles")
    else:
        print("Número inválido")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <url> <api_key>")
    else:
        url = sys.argv[1]
        api_key = sys.argv[2]
        main(url, api_key)
