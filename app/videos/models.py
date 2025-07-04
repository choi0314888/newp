from django.db import models
from common.models import CommonModel
from users.models import User

#
# - title
# - description
# - link
# - category
# - views_count
# - thumbnail
# - video_file : link
# - User : FK

class Video(CommonModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    category = models.CharField(max_length=20)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField() # S3 Bucket => Save File => Return URL => Save URL
    video_file = models.FileField(upload_to='storage/')

    user = models.ForeignKey(User, on_delete=models.CASCADE)


# User : Video == 1 : N => 부모 : 자녀(FK)
# User = Video * x
# Video = User * 1
