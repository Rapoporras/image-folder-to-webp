# Conversor de carpetas de imágenes/PDF a WebP

Este proyecto convierte archivos dentro de una carpeta (`fotos/`) a formato **WebP**, manteniendo:

- La estructura de subcarpetas.
- El nombre base de cada archivo.
- Páginas de PDF y frames de imágenes animadas como archivos separados.

Los archivos convertidos se guardan en `optimizadas/`.

## Qué formatos acepta

- `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.tif`, `.webp`, `.pdf`, `.heic`

## Requisitos

- Python 3.9 o superior
- `pip`
- Dependencias de Python:
	- `Pillow`
	- `pdf2image`
- Para convertir PDF: **Poppler** instalado en el sistema

## Instalación

### 1) Clonar el repositorio

```bash
git clone <URL_DEL_REPO>
cd image-folder-to-webp
```

### 2) Crear y activar entorno virtual (recomendado)

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Instalar dependencias de Python

```bash
pip install pillow pdf2image
```

### 4) Instalar Poppler (necesario para PDF)

`pdf2image` necesita Poppler para procesar archivos `.pdf`.

Windows:

1. Descarga Poppler para Windows.
2. Descomprime el paquete (por ejemplo, en `C:\poppler`).
3. Agrega `C:\poppler\Library\bin` (o la carpeta `bin` equivalente) al `PATH`.

macOS (Homebrew):

```bash
brew install poppler
```

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install -y poppler-utils
```

## Estructura esperada

```text
image-folder-to-webp/
├─ init.py
├─ fotos/
│  ├─ carpeta1/
│  └─ imagen.jpg
└─ optimizadas/
```

Coloca tus archivos dentro de `fotos/`. Si no existe `optimizadas/`, el script la creará.

## Ejecutar el programa

Desde la raíz del proyecto:

```bash
python init.py
```

Al terminar, verás los archivos convertidos en `optimizadas/` conservando la estructura original.

## Configuración rápida

En `init.py` puedes ajustar:

- Carpeta de origen (`origen`)
- Carpeta de salida (`destino`)
- Calidad WebP (`calidad`, por defecto 80)

Ejemplo:

```python
optimizar_manteniendo_estructura("fotos", "optimizadas", calidad=80)
```

## Notas

- Si un archivo tiene varias páginas/frames, se guarda con sufijos como `-p1`, `-p2`, etc.
- Si algún formato no abre correctamente (por ejemplo algunos `.heic`), el script mostrará el error y continuará con el resto de archivos.
