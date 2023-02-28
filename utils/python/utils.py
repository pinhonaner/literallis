from PIL import Image

def resize_image(image_path, output_path, width=None, height=None):
    with Image.open(image_path) as img:
        # Obter as dimensões atuais da imagem
        old_width, old_height = img.size
        
        # Definir a proporção desejada
        aspect_ratio = width / height
        
        # Obter a proporção atual da imagem
        image_ratio = old_width / old_height
        
        # Se a imagem é mais larga do que a proporção desejada, cortar as partes laterais
        if image_ratio > aspect_ratio:
            new_width = int(old_height * aspect_ratio)
            img = img.crop(((old_width - new_width) // 2, 0, (old_width + new_width) // 2, old_height))
        
        # Se a imagem é mais alta do que a proporção desejada, cortar as partes superiores e inferiores
        elif image_ratio < aspect_ratio:
            new_height = int(old_width / aspect_ratio)
            img = img.crop((0, (old_height - new_height) // 2, old_width, (old_height + new_height) // 2))
        
        # Redimensionar a imagem para a largura e altura desejadas
        if width is not None and height is not None:
            img = img.resize((width, height), resample=Image.LANCZOS)
        elif width is not None:
            img = img.resize((width, int(width / aspect_ratio)), resample=Image.LANCZOS)
        elif height is not None:
            img = img.resize((int(height * aspect_ratio), height), resample=Image.LANCZOS)
        
        # Salvar a imagem redimensionada
        img.save(output_path)