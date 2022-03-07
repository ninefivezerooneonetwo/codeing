from django.db import models

# Create your models here.

class Info(models.Model):
    id = models.AutoField(primary_key=True);
    title = models.CharField(max_length=50);
    content = models.TextField();
    #writer = models.ForeignKey(Cust, on_delete=models.CASCADE, related_name='custid')
    pub_date = models.DateField(auto_now=True);
    class Meta:
        db_table = 'db_info'