from django.db import models
from common.models import CommonModel

# - User: FK = > subscriber
# - User: FK = > subscribed_user

class Subscription(CommonModel):
    subscriber = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscriptions')
    subscribed_to = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscribers')