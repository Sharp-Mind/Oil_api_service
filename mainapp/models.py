from operator import mod
from django.db import models

class Reports(models.Model):
    date = models.DateField(verbose_name='Date', null=False)
    liquid = models.FloatField(verbose_name='Liquid', null=False)
    oil = models.FloatField(verbose_name='Oil', null=False)
    water = models.FloatField(verbose_name='Water', null=False)
    wct = models.FloatField(verbose_name='wct', null=False)

    # class Meta:
    #     ordering = ['date']

    # gid = models.IntegerField(verbose_name = "идентификатор", unique=True, null=True)
    # role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    # # role = models.CharField(verbose_name = 'роль', max_length=64, default=Role.MEMBER)
    # date_in = models.DateField(verbose_name="дата добавления")
    # is_sended = models.BooleanField(verbose_name="отправлено", null=True)
    # note = models.TextField(verbose_name="заметка", blank=True)
    # expire = models.CharField(verbose_name="дата истечения", max_length=64, null=True) # input_formats=["%d-%m-%Y"]
    # vvcard = models.CharField(verbose_name="номер карты ВВ", max_length=64, default="НЕТ КАРТЫ")

# class Post(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100, blank=True, default='')
#     body = models.TextField(blank=True, default='')
#     owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

#     class Meta:
#         ordering = ['created']