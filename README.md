# Script de Mantenimiento del Sistema

Este script de Python realiza tareas de mantenimiento en computadoras con sistemas operativos Windows y Ubuntu. Proporciona un menú interactivo que permite al usuario seleccionar su sistema operativo y ejecutar varias tareas de mantenimiento, como eliminar archivos temporales, limpiar el sistema y actualizar el software.

## Funcionalidades

- **Eliminación de archivos temporales**.
- **Ejecución del liberador de espacio en disco** (Windows).
- **Verificación y reparación de errores en el disco**.
- **Actualización del sistema**.
- **Limpieza de caché de paquetes y eliminación de paquetes no utilizados** (Ubuntu).

## Requisitos

- Python 3.x
- Permisos de administrador (necesarios para ejecutar algunos comandos de mantenimiento).

## Instalación

1. **Clona el repositorio**:

    ```bash
    git clone https://github.com/zirus92/Mantenimiento-del-Sistema.git
    cd Mantenimiento-del-Sistema
    ```

## Uso

1. **Ejecuta el script**:

    En Windows:
    ```bash
    python mantenimiento.py
    ```

    En Ubuntu:
    ```bash
    python3 mantenimiento.py
    ```

2. **Selecciona tu sistema operativo**:

    El script mostrará un menú interactivo donde puedes seleccionar entre Windows, Ubuntu o salir del programa.

## Detalles de las Tareas Realizadas

### Windows

- **Eliminar archivos temporales**: Elimina todos los archivos en la carpeta temporal.
- **Liberador de espacio en disco**: Ejecuta la herramienta de limpieza de disco de Windows.
- **Verificar y reparar errores en el disco**: Ejecuta la herramienta `chkdsk` para verificar y reparar errores en el disco.
- **Actualizar el sistema**: Usa PowerShell para instalar todas las actualizaciones de Windows y reiniciar automáticamente si es necesario.

    **Nota**: La desfragmentación del disco debe realizarse manualmente.

### Ubuntu

- **Actualizar la lista de paquetes**: Ejecuta `apt update` para actualizar la lista de paquetes disponibles.
- **Actualizar todos los paquetes instalados**: Ejecuta `apt upgrade` para actualizar todos los paquetes a sus versiones más recientes.
- **Eliminar paquetes no utilizados**: Ejecuta `apt autoremove` para eliminar paquetes que ya no son necesarios.
- **Limpiar la caché de paquetes**: Ejecuta `apt clean` para limpiar la caché de paquetes descargados.
- **Limpieza de archivos temporales adicionales**: Ejecuta `apt-get autoclean` para limpiar archivos temporales adicionales.

## Notas Importantes

- **Permisos de Administrador**:
  - Algunas tareas requieren permisos de administrador. Asegúrate de ejecutar el script con los permisos necesarios.

## Contribución

Las contribuciones son bienvenidas. Si tienes alguna sugerencia o mejora, por favor, abre un issue o realiza un pull request.