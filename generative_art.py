from PIL import Image, ImageDraw, ImageChops
import random


def random_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def interpolate( start_color, end_color, factor: float):
    reciprocal = 1 - factor
    return (
        int(start_color[0] * reciprocal + end_color[0] * factor),
        int(start_color[1] * reciprocal + end_color[1] * factor),
        int(start_color[2] * reciprocal + end_color[2] * factor),

    )


def generative_art(path: str):
    print("Generating Art")
    image_size_h= 128
    image_size_w = 128
    image_color = (0,0,0)
    start_color = random_color()
    end_color = random_color()
    
    thickness = 2
    padding = 12
    image = Image.new(
        "RGB", 
        size=(image_size_h, image_size_w) , 
        color=image_color)
    
    # Draw lines 
    
    draw = ImageDraw.Draw(image)
    points=[]
    
    # Generate the points 
    for i in range(10):
        random_point =(
            random.randint(padding,image_size_h - padding),
            random.randint(padding,image_size_w - padding)

        )
        points.append(random_point)
        
    '''  # Draw bounding box 
    
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[0] for p in points)
    max_y = max(p[0] for p in points)
    draw.rectangle((min_x, min_y, max_x, max_y), outline=(235, 0,0))
    
    
    # center the image 
    
    delta_x = min_x - (image_size_h - max_x)
    delta_y = min_y - (image_size_w - max_y)

    
    for i , point in enumerate(points):
        points[i] = (point[0] - delta_x // 2, point[1] - delta_y //2)
        
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[0] for p in points)
    max_y = max(p[0] for p in points)
    draw.rectangle((min_x, min_y, max_x, max_y), outline=(255, 0,0))
    
'''

    # Drawing the points

    n_points = len(points) - 1
    
    # Overlay cavas
    
    overlay_image = Image.new("RGB", size=(image_size_h, image_size_w) ,color=image_color)
    overlay_draw = ImageDraw.Draw(overlay_image)
    

    for i, point in enumerate(points):
        p1 = point
        if i == n_points :
            p2 = points[0]
        else:
            p2 = points[i + 1]
            
        
        line_xy = (p1,p2)
        color_factor=  i/ n_points
        line_color= interpolate(start_color, end_color, color_factor)
        thickness += 1
        overlay_draw.line(line_xy, fill=line_color, width=thickness)
        image = ImageChops.add(image, overlay_image)
        
        
    
    
    image.save(path)
    
  
  
if __name__ == "__main__":
    for i in range(10):
        generative_art(f"test_image_{i}.png")