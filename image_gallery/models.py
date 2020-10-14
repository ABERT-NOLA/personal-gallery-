from django.db import models

class imggal(models.Model):
    imgtitle=models.CharField(max_length=100)
    imgdesc=models.CharField(max_length=500)
    image=models.ImageField(upload_to='images/')
    location=models.ForeignKey('location',on_delete=models.CASCADE)

    def __str__(self):
        return self.imgtitle
    def save_image(self):
        return self.save()

    def delete_image(self):
        return self.delete
    def update_image(self):
        return self.update

class location(models.Model):
    location = models.TextField(max_length=200)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()


    def update_location(self):
        self.update()


    def delete_location(self):
        self.delete()