```mermaid
graph TD;
    A(Inicio) -->|Muestra mensaje de bienvenida| B[Menú principal];
    B -->|1. Agregar registro| C[Solicitar datos];
    C -->|Ingresar nombre, teléfono, cumpleaños y correo| D[Guardar en lista];
    D -->|Confirmar registro agregado| B;
    
    B -->|2. Buscar por teléfono| E[Solicitar número];
    E -->|Recorrer lista| F{¿Número encontrado?};
    F -->|Sí| G[Mostrar datos del contacto];
    F -->|No| H[Mostrar mensaje de error];
    G --> B;
    H --> B;
    
    B -->|3. Borrar registro| I[Solicitar número];
    I -->|Recorrer lista| J{¿Número encontrado?};
    J -->|Sí| K[Eliminar registro];
    J -->|No| L[Mostrar mensaje de error];
    K --> B;
    L --> B;
    
    B -->|4. Salir| M[Mostrar mensaje de despedida];
    M --> N(Fin);
    
    B -->|Opción inválida| O[Mostrar mensaje de error];
    O --> B;
