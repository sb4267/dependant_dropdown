
from django.db import models

class Brand(models.Model):
    brand_name = models.CharField(max_length=30)

    def __str__(self):
        return self.brand_name


class Models_name(models.Model):
    model_name = models.ForeignKey(Brand, on_delete=models.CASCADE)
    brand_id = models.CharField(max_length=30)
    def __str__(self):
        return str(self.brand_id)


class V_type(models.Model):
    model_n = models.ForeignKey(Models_name, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    def __str__(self):
        return str(self.name)


class Main_table(models.Model):
    gearbox=models.CharField(max_length=100)
    power_ps=models.CharField(max_length=100,)
    kilometer=models.CharField(max_length=100,)
    fuel_type=models.CharField(max_length=100,)
    duration=models.CharField(max_length=100,)

    brand_name_1 = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    model_name = models.ForeignKey(Models_name, on_delete=models.SET_NULL, null=True)
    model_n = models.ForeignKey(V_type, on_delete=models.SET_NULL, null=True)
