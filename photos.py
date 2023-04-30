from PIL import Image, ImageFont, ImageDraw
import os
import datetime


def make_avatar():
    text_color = (100, 200, 255) #change color of a text
    if os.path.exists("avatar/result.jpg"):
        os.remove("avatar/result.jpg")

    now = datetime.datetime.now()

    #for example we have got 19:04 minute return 4 but needed is 04, so i add zero manually
    if(now.minute < 10):
        time = str(now.hour) + " : 0" + str(now.minute)
    else:
        time = str(now.hour) + " : " + str(now.minute)

    my_image = Image.open('avatar/avatar.png')

    font = ImageFont.truetype("arial.ttf", 200)

    width, height = my_image.size

    image_editable = ImageDraw.Draw(my_image)

    #here text is added
    image_editable.text((width/2, height/2), anchor="mm",
                        text=time, font=font,  fill=text_color)
    
    my_image.save("avatar/result.jpg", format="png")
    my_image.close()



make_avatar()