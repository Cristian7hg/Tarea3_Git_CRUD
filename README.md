
# Tarea 3 - CRUD en Python con Git y Git Flow

Este proyecto implementa un sistema CRUD básico en consola usando Python, junto con el uso de Git Flow aplicado sobre GitHub.

Descripción del Proyecto

Es un sistema que permite:
- Crear usuarios
- Listar usuarios
- Actualizar usuarios
- Eliminar usuarios

Los datos se almacenan en un archivo JSON (`data.json`). Toda la interacción se hace desde la consola.

## Tecnologías utilizadas

- Python 3
- Git y GitHub
- Git Flow

## Estructura de archivos

```
crud_usuarios/
├── main.py            # Menú principal del sistema
├── usuarios.py        # Lógica de las operaciones CRUD
├── utils.py           # Funciones de lectura y escritura JSON
├── data.json          # Almacenamiento
└── README.md          # Documentación
```

## Uso de Git Flow

Se usaron las siguientes ramas base:
- `main`: código listo para producción
- `developer`: rama de desarrollo principal
- `qa`: para pruebas antes de integrar a producción

Se crearon y trabajaron **5 ramas feature/**:
- `feature/crear-usuario`
- `feature/listar-usuarios`
- `feature/actualizar-usuario`
- `feature/eliminar-usuario`
- `feature/mejorar-menu`

### Pull Requests
Cada rama `feature/` fue subida y se hizo un Pull Request hacia `developer`, demostrando el flujo de trabajo completo con Git Flow.



## Funcionalidades principales

- Crear usuario (nombre, correo, edad)
- Listar todos los usuarios registrados
- Actualizar datos de un usuario por ID
- Eliminar usuario por ID
- Almacenamiento persistente en `data.json`


---

**Autor:** Cristian7hg  
**Repositorio:** [GitHub - Tarea3_Git_CRUD](https://github.com/Cristian7hg/Tarea3_Git_CRUD)
