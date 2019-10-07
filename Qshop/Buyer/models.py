from django.db import models
from Seller.models import LoginUser

class PayOrder(models.Model):
    '''
    订单表
    订单状态
    0 未支付
    1 已支付
    2 待发货
    3 待收货
    4 完成
    5 拒收
    '''
    order_number=models.CharField(max_length=32)
    order_data=models.DateTimeField(auto_now=True)
    # order_status=models.IntegerField()
    order_total=models.FloatField(blank=True,null=True)
    order_user=models.ForeignKey(to=LoginUser,on_delete=models.CASCADE)

class OrderInfo(models.Model):
    """
    订单详情
    """
    order_id=models.ForeignKey(to=PayOrder,on_delete=models.CASCADE)
    goods_id=models.IntegerField()
    goods_picture=models.CharField(max_length=32)
    goods_name=models.CharField(max_length=32)
    goods_count=models.IntegerField()
    goods_price=models.FloatField()
    goods_total_price=models.FloatField()
    order_status=models.IntegerField(default=0)
    store_id=models.ForeignKey(to=LoginUser,on_delete=models.CASCADE)

class Cart(models.Model):
    '''
    购物车
    '''
    goods_id=models.IntegerField()
    gooods_name=models.CharField(max_length=32)
    goods_number=models.IntegerField()
    goods_price=models.FloatField()
    goods_total=models.FloatField()
    goods_picture=models.CharField(max_length=32)
    cart_user=models.IntegerField()

# Create your models here.
