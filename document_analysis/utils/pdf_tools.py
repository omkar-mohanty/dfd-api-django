import os
from pdf2image import convert_from_path, convert_from_bytes

def convert_pdf_to_image_bytes(pdf, dpi = 300):
    images = convert_from_bytes(pdf)
    return images
def convert_pdf_to_image(pdf_path, output_folder, dpi=300):
    """
    Convert a PDF into images.

    Args:
    - pdf_path (str): Path to the PDF file.
    - output_folder (str): Folder where the images should be saved.
    - dpi (int): Dots per inch for the resulting images.

    Returns:
    - List of image paths.
    """
    images = convert_from_path(pdf_path, dpi=dpi)
    image_paths = []

    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i + 1}.png")
        image.save(image_path, 'PNG')
        image_paths.append(image_path)

    return image_paths
