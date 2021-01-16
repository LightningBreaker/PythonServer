from django.db import models

# Create your models here.


class AgentBlue(models.Model):
    vid=models.IntegerField(verbose_name="agent唯一编号",unique=True)
    x=models.IntegerField(verbose_name="x坐标值")
    y=models.IntegerField(verbose_name="y坐标值")
    health=models.FloatField(verbose_name="生命值")
    type=models.TextField(verbose_name="装备类型")
    weapon=models.FloatField(verbose_name="",default=1)



class AgentRed(models.Model):
    vid = models.IntegerField(verbose_name="agent唯一编号",unique=True)
    x = models.IntegerField(verbose_name="x坐标值")
    y = models.IntegerField(verbose_name="y坐标值")
    health = models.FloatField(verbose_name="生命值")
    type = models.TextField(verbose_name="装备类型")
    weapon = models.FloatField(verbose_name="", default=1)

class NumberCapture(models.Model):
    totalRed=models.IntegerField(verbose_name="红方总数",default=0)
    totalBlue=models.IntegerField(verbose_name="蓝方总数",default=0)
    isUpdateRed=models.BooleanField(verbose_name="红方总人数是否更新",default=False)
    isUpdateBlue=models.BooleanField(verbose_name="蓝方总人数是否更新",default=False)


#存储被蓝方检测到的红方敌人
class EnemyTargetOfBlue(models.Model):
    vid = models.IntegerField(verbose_name="agent唯一编号",unique=True)
    x = models.IntegerField(verbose_name="x坐标值")
    y = models.IntegerField(verbose_name="y坐标值")
    health = models.FloatField(verbose_name="生命值")
    type = models.TextField(verbose_name="装备类型")
    weapon = models.FloatField(verbose_name="武器杀伤力", default=1)
    isVisible=models.BooleanField(verbose_name="是否从视野中消失")

#存储被红方检测到的蓝方敌人
class EnemyTargetOfRed(models.Model):
    vid = models.IntegerField(verbose_name="agent唯一编号",unique=True)
    x = models.IntegerField(verbose_name="x坐标值")
    y = models.IntegerField(verbose_name="y坐标值")
    health = models.FloatField(verbose_name="生命值")
    type = models.TextField(verbose_name="装备类型")
    weapon = models.FloatField(verbose_name="武器杀伤力", default=1)
    isVisible = models.BooleanField(verbose_name="是否从视野中消失")

class BuildingTarget(models.Model):
    vid=models.IntegerField(verbose_name="设备唯一编号",unique=True)
    x = models.IntegerField(verbose_name="x坐标值")
    y = models.IntegerField(verbose_name="y坐标值")
    values=models.FloatField(verbose_name="夺控地点价值",default=1)


class ObstacleTarget(models.Model):
    vid=models.IntegerField(verbose_name="障碍物唯一编号",unique=True)
    x = models.IntegerField(verbose_name="x坐标值")
    y = models.IntegerField(verbose_name="y坐标值")
    health = models.FloatField(verbose_name="生命值")

class RootMap(models.Model):
    vid=models.IntegerField(verbose_name="地图唯一编号,C#中通过枚举变量获取",unique=True)
    name=models.TextField(verbose_name='地图唯一名字')
    start_pos_x=models.FloatField(verbose_name='Unity起始点x')
    start_pos_y=models.FloatField(verbose_name='Unity起始点y')
    end_pos_x=models.FloatField(verbose_name='Unity终点x')
    end_pos_y=models.FloatField(verbose_name='Unity终点y')
    pos_interval=models.FloatField(verbose_name='采样间隔点')
    stripe=models.IntegerField(verbose_name='取样步长')
    local_path=models.TextField(verbose_name='地图s所对应的文件夹')
    base_height=models.FloatField(verbose_name='起始高',default=0)

class Apartment(models.Model):
  root_map=models.ForeignKey(RootMap,on_delete=models.CASCADE)
  floor=models.IntegerField(verbose_name='层数')
  file_name=models.TextField(verbose_name='目标地图名称')
  height_floor=models.FloatField(verbose_name='楼层高度下界',default=0)
  height_ceil=models.FloatField(verbose_name='楼层高度上界',default=1)
  class Meta:
      unique_together=("root_map","floor")


