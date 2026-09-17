from django.db import models

# Create your models here.


    
from django.db import models


from django.db import models


class customers(models.Model):

    id = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=200)

    city = models.CharField(max_length=100)

    state = models.CharField(max_length=100)

    region = models.CharField(max_length=100)

    country = models.CharField(max_length=100)

    class Meta:
        db_table = "customers"

    def __str__(self):
        return self.name


class products(models.Model):

    id = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=200)

    category = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name


class orders(models.Model):

    id = models.IntegerField(primary_key=True)

    customer = models.ForeignKey(
        customers,
        on_delete=models.CASCADE,
        db_column="customer_id",
        related_name="customer_orders"
    )

    order_date = models.DateField()

    class Meta:
        db_table = "orders"

    def __str__(self):
        return str(self.id)


class order_details(models.Model):

    id = models.IntegerField(primary_key=True)

    order = models.ForeignKey(
        orders,
        on_delete=models.CASCADE,
        db_column="order_id",
        related_name="order_items"
    )

    product = models.ForeignKey(
        products,
        on_delete=models.CASCADE,
        db_column="product_id",
        related_name="product_orders"
    )

    qty = models.IntegerField()

    sales = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = "order_details"

    def __str__(self):
        return f"{self.order_id} - {self.product_id}"