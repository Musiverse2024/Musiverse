# Sistema de Gestión Musical y Control de Accesos ISPC

## Descripción
Sistema integral desarrollado en Python que combina gestión de usuarios, control de accesos y análisis de datos. El sistema implementa algoritmos avanzados de búsqueda y ordenamiento, junto con una robusta base de datos musical y capacidades de análisis pluvial.

## Características Principales

### 1. Gestión de Usuarios y Accesos
- Sistema CRUD completo
- Validación de credenciales y datos
- Sistema de logging y monitoreo
- Algoritmos de búsqueda:
  - Búsqueda binaria para username y DNI
  - Búsqueda secuencial para email
- Ordenamiento de usuarios por múltiples criterios

### 2. Sistema Musical
- Gestión completa de biblioteca musical
  - Artistas y álbumes
  - Playlists personalizadas
  - Historial de reproducciones
  - Sistema de favoritos
- Categorización por géneros musicales
- Recomendaciones basadas en preferencias

### 3. Análisis de Datos Pluviales
- Gestión de registros pluviales
  - Carga y generación de datos
  - Almacenamiento en formato CSV
- Visualizaciones estadísticas:
  - Gráficos de barras mensuales
  - Diagramas de dispersión anual
  - Gráficos circulares de distribución
- Análisis y consultas personalizadas

## Requisitos del Sistema
- Python 3.8+
- MySQL 5.7+
- Dependencias adicionales en `requirements.txt`

## Instalación

1. **Preparación del Entorno**
```bash
git clone 

# Crear entorno virtual:
python -m venv venv

# Activar entorno virtual:

# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

2. **Instalación de Dependencias**
```bash
pip install -r requirements.txt
```

3. **Configuración de Base de Datos**
```bash
mysql -u root -p < sql/musiverse.sql
```

4. **Variables de Entorno**
Crear archivo `.env`:
```plaintext
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_NAME=musiverseDB
```

## Estructura del Proyecto ISPC
```
app/
├── data/                    # Almacenamiento de datos
│   ├── usuarios.ispc       # Datos de usuarios
│   ├── accesos.ispc       # Registros de acceso
│   └── logs.txt           # Intentos fallidos
├── ispc/
│   ├── busquedas_y_ordenamientos/
│   │   ├── busqueda.py    # Algoritmos de búsqueda
│   │   └── ordenamiento.py # Algoritmos de ordenamiento
│   ├── gestionAcceso.py   # Gestión de accesos
│   ├── gestionUsuario.py  # Gestión de usuarios
│   └── validaciones.py    # Validación de entrada
└── menus/
    ├── accesos_ispc_menu.py # Sistema de menús principal
    └── user_menu.py         # Interfaz de usuario
```

## Uso del Sistema

### Inicio de la Aplicación
```bash
python app/main.py
```

### Módulos Principales
1. **Gestión de Usuarios**
   - Registro y autenticación
   - Búsqueda y ordenamiento
   - Gestión de accesos

2. **Sistema Musical**
   - Gestión de biblioteca
   - Control de playlists
   - Sistema de favoritos

3. **Análisis Pluvial**
   - Carga de datos
   - Visualizaciones
   - Consultas estadísticas

## Base de Datos
Sistema MySQL con esquema relacional que incluye:
- Gestión de usuarios y accesos
- Sistema musical completo
- Datos de ejemplo pre-cargados

## Desarrollo
### Stack Tecnológico
```plaintext
mysql-connector-python==8.0.26
python-dotenv==0.19.0
bcrypt==3.2.0
pandas==2.0.0
matplotlib==3.7.1
```

## Contribución
1. Fork del repositorio
2. Crear rama de feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit de cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## Licencia
MIT License - Ver archivo [LICENSE](LICENSE) para más detalles.

## Agradecimientos
- Instituto Superior Politécnico Córdoba
- Equipo de desarrollo y contribuidores
- Comunidad de código abierto