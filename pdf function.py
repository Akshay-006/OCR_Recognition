import fitz
import io
import PIL.Image

def get_pdf(pdf):
    pdf=fitz.open(pdf)
    counter=1

    for i in range(len(pdf)):
        page=pdf[i]
        images=page.get_images()
        for image in images:
            base_img=pdf.extract_image(image[0])
            image_data=base_img['image']
            img=PIL.Image.open(io.BytesIO(image_data))
            extension=base_img['ext']
            img.save(f"image{counter}.{extension}")
            counter+=1

get_pdf("sample.pdf")


