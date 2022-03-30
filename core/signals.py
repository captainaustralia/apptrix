from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import Participant


@receiver(post_save, sender=Participant)
def add_watermark(sender, **kwargs):
    """
    Function for add watermark for photo.
    The function takes **kwargs for enter email in path to photo
    We need only one arg -> 'instance'
    """
    try:
        email = kwargs['instance']
        user = Participant.objects.get(email=email)
        path = user.avatar
        image = Image.open(path)
        watermark = Image.open('media/watermark.png')
        image.paste(watermark, (0, 0))
        image.save('media/' + str(path))
        # we can have only 1 trouble with it func
        # if user not send photo , the model will set the default photo
        # the task does not set rules on whether a field is required
    except Exception:
        pass
