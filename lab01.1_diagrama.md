```mermaid
classDiagram
    class Contacto {
        - nombre: str
        - telefono: str
        - cumpleanos: str
        - correo: str
        + __init__(nombre: str, telefono: str, cumpleanos: str, correo: str)
        + __str__() str
    }

    class Directorio {
        - contactos: List[Contacto]
        - indice_telefonos: Dict[str, Contacto]
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
