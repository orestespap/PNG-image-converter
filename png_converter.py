#https://stackoverflow.com/questions/31434278/how-do-i-use-python-pil-to-save-an-image-to-a-particular-directory
#https://stackoverflow.com/questions/6149054/how-to-give-path-while-saving-images-using-pil-in-django


from PIL import Image
import os,os.path


def png_conversion():
	input_path="C:/Users/Orestes/Desktop/pv/Device photos/Devices' photos" #original directory
	
	output_path="C:/Users/Orestes/Desktop/pv/Device photos/Dev photos PNG/" #output directory
	
	valid_images=[".jpg",".gif",".png",".tga",'.jpeg']
	
	for index,afile in enumerate(os.listdir(input_path)):
		file_format = os.path.splitext(afile)[1]
		
		if file_format.lower() in valid_images:
			with open(os.path.join(input_path,afile), "rb") as image_file:
				rgb_im = Image.open(image_file).convert('RGBA')
				rgb_im.save(f'{output_path}{afile.split(".")[0]}.png', 'PNG') #saves all photos as .PNG to new directory
				
		print(f'Photo {index} successfully converted to .png format and added to new directory!')
			
png_conversion()