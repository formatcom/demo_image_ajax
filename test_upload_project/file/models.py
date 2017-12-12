from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize


class Profile(models.Model):

    cover = models.ImageField(upload_to="profile/cover/%Y/%m/%d")
    cover_x256 = ImageSpecField(source='cover',
                    processors=[SmartResize(256, 256)],
                    format='JPEG',
                    options={'quality': 60})
    cover_x512 = ImageSpecField(source='cover',
                    processors=[SmartResize(512, 512)],
                    format='JPEG',
                    options={'quality': 60})
