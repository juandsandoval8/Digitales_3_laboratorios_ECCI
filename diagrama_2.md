```mermaid
classDiagram
    class Contacto {
        - nombre: str
        - telefono: str
        - cumpleanos: str
        - correo: str
        + __init__(nombre: str, telefono: str, cumpleanos: str, correo: str)
        + __str__() str
        + obtener_nombre() str
        + obtener_telefono() str
        + obtener_cumpleanos() str
        + obtener_correo() str
    }

    class Directorio {
        - contactos: List~Contacto~
        - indice_telefonos: Dict~str, Contacto~
        + __init__()
        + agregar_contacto(contacto: Contacto) None
        + buscar_por_telefono(telefono: str) Contacto | str
        + eliminar_contacto(telefono: str) None
        + mostrar_contactos() None
        + guardar_datos(archivo: str = "contactos.json") None
        + cargar_datos(archivo: str = "contactos.json") None
        + validar_telefono(telefono: str) bool
        + validar_correo(correo: str) bool
    }

    class GestorArchivos {
        + guardar_en_json(datos: List~Contacto~, archivo: str) None
        + cargar_desde_json(archivo: str) List~Contacto~
    }

    Contacto "1" *-- "many" Directorio : contiene
    Directorio "1" --> "1" GestorArchivos : usa
