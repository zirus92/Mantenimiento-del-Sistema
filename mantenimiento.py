import os

def show_banner():
    print("""
    **********************************
    *   Mantenimiento del Sistema    *
    **********************************
    """)

def display_menu():
    print("1. Windows")
    print("2. Ubuntu")
    print("0. Salir")
    choice = input("Seleccione su sistema operativo (1, 2 o 0): ")
    return choice

def windows_maintenance():
    print("Realizando tareas de mantenimiento en Windows...")
    os.system('del /q/f/s %TEMP%\\*')
    os.system('cleanmgr /sagerun:1')
    os.system('chkdsk /f')
    os.system('powershell.exe -Command "Install-WindowsUpdate -AcceptAll -AutoReboot"')
    print("""
    Tareas realizadas en Windows:
    - Archivos temporales eliminados
    - Liberador de espacio en disco ejecutado
    - Verificación y reparación de errores en el disco
    - Actualización del sistema
    
    NOTA:
    - Debe desfragmentar el disco manualmente
    """)

def ubuntu_maintenance():
    print("Realizando tareas de mantenimiento en Ubuntu...")
    os.system('sudo apt update')
    os.system('sudo apt upgrade -y')
    os.system('sudo apt autoremove -y')
    os.system('sudo apt clean')
    os.system('sudo apt-get autoclean')
    print("""
    Tareas realizadas en Ubuntu:
    - Lista de paquetes actualizada
    - Paquetes actualizados
    - Paquetes no utilizados eliminados
    - Caché de paquetes limpiada
    - Archivos temporales adicionales limpiados
    """)

def main():
    show_banner()
    choice = display_menu()
    if choice == '1':
        windows_maintenance()
    elif choice == '2':
        ubuntu_maintenance()
    elif choice == '0':
        print("Saliendo del programa...")
    else:
        print("Selección inválida. Por favor, seleccione 1, 2 o 0.")

if __name__ == "__main__":
    main()
