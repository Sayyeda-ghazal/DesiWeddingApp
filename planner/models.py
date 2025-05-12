from django.db import models

class EventType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)


class Menu(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)  
    items = models.TextField()  
    price_per_guest = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    categories = models.JSONField(default=list)  
    dietary_requirements = models.JSONField(default=list)  

    def __str__(self):
        return self.name


class QuoteRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    guests = models.PositiveIntegerField()
    message = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

