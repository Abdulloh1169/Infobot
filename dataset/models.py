from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def getCharacteristics(self):
        try: return self.characteristics
        except: return None


    def getMedia(self):
        try: return self.media_set.all()
        except: return None

class Characteristics(models.Model):
    parent = models.OneToOneField(Device, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.parent}_{self.id}"


class Media(models.Model):
    parent = models.ForeignKey(Device, on_delete=models.CASCADE)
    tid = models.CharField(max_length=255, null=True, blank=True)
    mediafile = models.FileField(upload_to='media/', null=True)
    status = models.BooleanField(default=False)
    filetype = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return f"{self.parent}_{self.tid}" 
