import sys
from pprint import pprint 
from PIL import Image
from PIL.ExifTags import TAGS
import pikepdf


def get_image_metadata(image_file):
    image = Image.open(image_file)
    info_dict = {
        "Filename": image.filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated", False),
        "Frames in Image": getattr(image, "n_frames", 1)
    }  
    exifdata = image.getexif()
    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        if isinstance(data, bytes):
            data = data.decode()
        info_dict[tag] = data
    return info_dict


def get_pdf_metadata(pdf_file):
    try:
        # Abre o PDF
        pdf = pikepdf.Pdf.open(pdf_file)

        # Retorna os metadados como um dicionário
        return dict(pdf.docinfo)
    except Exception as e:
        print(f"Erro ao extrair metadados do PDF: {e}")
        return {}


if __name__ == "__main__":
    file = sys.argv[1]
    if file.endswith(".pdf"):
        print(get_pdf_metadata(file))
    elif file.lower(
        
    ).endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")):
        pprint(get_image_metadata(file))
    else:
        print(f"Unsupported file format: {file}")