from pycocotools.coco import COCO
import requests

coco = COCO('annotations/instances_train2014.json') #set path to annotations folder
cat_Ids = coco.getCatIds(catNms = ['dog']) # specify name of category to fetch
img_Ids = coco.getImgIds(catIds = cat_Ids)
images = coco.loadImgs(img_Ids) #fetch images

for im in images:
    img_data = requests.get(im['coco_url']).content
    img_folder = 'dog_images' #specify folder to save images
    with open(img_folder+'/'+ im['file_name'], 'wb') as handler: 
        handler.write(img_data)

