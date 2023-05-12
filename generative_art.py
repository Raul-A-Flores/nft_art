from PIL import Image, ImageDraw
import random


def generative_art():
    print("Generating Art")
    image_size_h= 128
    image_size_w = 128
    image_color = ( 255, 255, 255)
    image = Image.new(
        "RGB", 
        size=(image_size_h, image_size_w) , 
        color=image_color)
    
    # Draw lines 
    
    draw = ImageDraw.Draw(image)
    
    for i in range(10):
        random_point_uno = (random.randint(0, image_size_h),random.randint(0, image_size_h) )
        random_point_dos = (random.randint(0, image_size_w),random.randint(0, image_size_w) )

        
        
        
        line_xy = (random_point_uno,random_point_dos)
        line_color=(0,0,0)
        draw.line(line_xy, fill=line_color)
        
        
    
    
    image.save("test_image.png")
    
  
  
if __name__ == "__main__":
    
    generative_art()