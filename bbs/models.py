from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator


MAX_STAR    = 5

class Review(models.Model):
    comment     = models.CharField(verbose_name="コメント",max_length=500)
    star        = models.IntegerField(verbose_name="星",validators=[MinValueValidator(1),MaxValueValidator(MAX_STAR)])

    def star_icon(self):
        dic                 = {}
        dic["true_star"]    = self.star * " "
        dic["false_star"]   = (MAX_STAR - self.star) * " "

        return dic



