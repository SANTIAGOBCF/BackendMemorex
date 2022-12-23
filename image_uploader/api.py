from django.conf import settings

from ninja import Router
from ninja import File
from ninja.files import UploadedFile

import cloudinary
import cloudinary.uploader
import cloudinary.api

router = Router()

cloudinary.config( 
  cloud_name=settings.CLOUDINARY_CLOUD_NAME,
  api_key=settings.CLOUDINARY_API_KEY,
  api_secret=settings.CLOUDINARY_API_SECRET,
  secure = True
)

@router.post('/upload')
def upload(request, file: UploadedFile = File(...)):
  data = file.read()
  name_image = file.name
  cloudinary.uploader.upload(data,public_id=name_image, overwrite=True)
  # Build the URL for the image and save it in the variable 'srcURL'
  #srcURL = cloudinary.CloudinaryImage(nameImage).build_url()
  result = cloudinary.api.resources()
  src_url = 'None'
  for image in result['resources']:
    if name_image in image['url']:
        src_url = image['url']
  return {'name': file.name, 'len': len(data),'URL': src_url,}
