
# Essentials :
# pip install qrcode
# pip install "qrcode[pil]" --> essentail for setting up the color and background color

# importing module for the project
import qrcode

# defining a function to generate and save qrcode image
def QR_generate():

    # getting qrcode parameters input
    data = input("Enter the url for QR : ")
    color = input("Enter the color of QR you want : ")
    bgColor = input("Enter the background color you want :")


    # creating a instance of qrcode.QRCode class
    imgQR = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L)

    # adding url or data for creating QR-code
    imgQR.add_data(data)

    # compile the data for qr-code
    imgQR.make(fit = True)

    # creating a image to store qr-code 
    img=imgQR.make_image(
        fill_color = color,
        back_color = bgColor
    )

    # saving the image as a .png file 
    img.save('qr.png')



QR_generate()

