from ninja import Router
from ninja import NinjaAPI, File
from ninja.files import UploadedFile
import cloudinary
import cloudinary.uploader
import cloudinary.api

router = Router()

cloudinary.config( 
  cloud_name = "dgbr818uh", 
  api_key = "427136126652911", 
  api_secret = "MiC1245H_E4fCnx6HTxj0rOySkA",
  secure = True
)

@router.post("/upload")
def upload(request, file: UploadedFile = File(...)):
    data = file.read()
    nameImage=file.name
    cloudinary.uploader.upload(data,public_id=nameImage, overwrite=True)
    # Build the URL for the image and save it in the variable 'srcURL'
    #srcURL = cloudinary.CloudinaryImage(nameImage).build_url()
    result = cloudinary.api.resources()
    srcUrl="None"
    for image in result["resources"]:
        print(image["url"])
        if nameImage in image["url"]:
            srcURL=image["url"]
    return {'name': file.name, 'len': len(data),'URL':srcURL}

