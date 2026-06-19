import os
from PIL import Image
from pathlib import Path
from pdf2image import convert_from_path

def guardar_como_webp(imagen_pil, ruta_destino, calidad):
    if imagen_pil.mode in ("RGBA", "P"):
        imagen_pil = imagen_pil.convert("RGBA")
    else:
        imagen_pil = imagen_pil.convert("RGB")
    
    imagen_pil.save(ruta_destino, "WEBP", quality=calidad, method=6)

def optimizar_manteniendo_estructura(directorio_origen, directorio_destino, calidad=80):
    path_origen = Path(directorio_origen)
    path_destino = Path(directorio_destino)
    extensiones_validas = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif', '.webp', '.pdf', '.heic')

    print("--- Iniciando Conversión a WebP (Manteniendo Estructura y Nombres) ---")

    for root, dirs, files in os.walk(path_origen):
        archivos_validos = [f for f in files if f.lower().endswith(extensiones_validas)]
        
        if not archivos_validos:
            continue

        ruta_relativa = Path(root).relative_to(path_origen)
        carpeta_destino_final = path_destino / ruta_relativa
        carpeta_destino_final.mkdir(parents=True, exist_ok=True)

        for file in archivos_validos:
            path_archivo_original = Path(root) / file
            nombre_sin_ext = path_archivo_original.stem  
            ext = path_archivo_original.suffix.lower()

            try:
                if ext == '.pdf':
                    paginas = convert_from_path(path_archivo_original)
                    for i, pagina in enumerate(paginas):
                        sufijo_pagina = f"-p{i+1}" if len(paginas) > 1 else ""
                        nuevo_nombre = f"{nombre_sin_ext}{sufijo_pagina}.webp"
                        path_archivo_webp = carpeta_destino_final / nuevo_nombre
                        guardar_como_webp(pagina, path_archivo_webp, calidad)
                
                else:
                    with Image.open(path_archivo_original) as img:
                        num_frames = getattr(img, "n_frames", 1)
                        
                        for i in range(num_frames):
                            img.seek(i)
                            sufijo_frame = f"-p{i+1}" if num_frames > 1 else ""
                            nuevo_nombre = f"{nombre_sin_ext}{sufijo_frame}.webp"
                            path_archivo_webp = carpeta_destino_final / nuevo_nombre
                            guardar_como_webp(img, path_archivo_webp, calidad)

                print(f"✅ Procesado: {path_archivo_original.relative_to(path_origen)}")

            except Exception as e:
                print(f"❌ Error en {file}: {e}")

# --- CONFIGURACIÓN ---
origen = "fotos"
destino = "optimizadas"

optimizar_manteniendo_estructura(origen, destino)