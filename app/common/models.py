from django.db import models

# - created_at : 데이터 생성시간
# - updated_at : 데이터 업데이트 시간

class CommonModel(models.Model):
    # 데이터 생성 시간 (고정)
    created_at = models.DateTimeField(auto_now_add=True) # 0000-00-00, 00:00:00

    # 데이터가 업데이트 될 떄마다 시간이 게속 최신화.
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # DB에 테이블을 추가하지 말아주세요.