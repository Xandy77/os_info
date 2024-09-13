import os

usuario = os.environ.get('USERNAME')

print(f"Sistema Operacional: {os.name}.")
print(f"Nome do usuário: {usuario}.")