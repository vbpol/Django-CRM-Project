class ImageSlider(models.Model):
    fs = FileSytemStorage(location="C:/")
    
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')