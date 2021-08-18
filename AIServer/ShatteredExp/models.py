from django.db import models

# Create your models here.

# class HumanTarget(models.Model):
#     vid=models.IntegerField(verbose_name='用于取point3d')
#     whichTeam=models.IntegerField(verbose_name='属于哪支队伍')
#     agent_vid=models.IntegerField(verbose_name='事实上对应Agent的vid')
#     human_target_x = models.FloatField(verbose_name='玩家给定目标点_x')
#     human_target_z = models.FloatField(verbose_name='玩家给定目标点_z')
#     human_target_height = models.FloatField(verbose_name='玩家给定目标点_height')
#     point3d = models.ForeignKey('Point3D', on_delete=models.CASCADE, null=True, blank=True)
#     class Meta:
#         unique_together = ("whichTeam", "agent_vid")

class AgentBlue(models.Model):
    vid=models.IntegerField(verbose_name="agent唯一编号",unique=True)
    x=models.IntegerField(verbose_name="x坐标值")
    y=models.IntegerField(verbose_name="y坐标值")
    health=models.FloatField(verbose_name="生命值")
    type=models.TextField(verbose_name="装备类型")
    weapon=models.FloatField(verbose_name="",default=1)
    equipment_type=models.IntegerField(verbose_name='原始装备类型',default=2)
    point3d = models.ForeignKey('Point3D', on_delete=models.CASCADE,null=True,blank=True)


    isControlledByAi=models.BooleanField(verbose_name='是否为AI分配目的地',default=True)
    is_human_target_changed=models.BooleanField(verbose_name='是否更新目的地',default=False)
    target_building=models.ForeignKey('BuildingTarget',verbose_name='指定目的地',blank=True,null=True,related_name='agent_blue_set',on_delete=models.CASCADE)

    #
    load_ability=models.BooleanField(verbose_name='是否能装载飞机',default=False)

    # 角度变换
    destination_angle_horizon = models.FloatField(verbose_name='目标角度', blank=True, null=True)
    current_angle_horizon = models.FloatField(verbose_name='当前角度', blank=True, null=True)

    destination_angle_vertical = models.FloatField(verbose_name='目标角度', blank=True, null=True)
    current_angle_vertical = models.FloatField(verbose_name='当前角度', blank=True, null=True)
    angel_range_horizon = models.FloatField(verbose_name='旋转角度范围', default=45)
    angel_range_vertical = models.FloatField(verbose_name='旋转角度范围', default=30)


class AgentRed(models.Model):
    vid = models.IntegerField(verbose_name="agent唯一编号",unique=True)
    x = models.IntegerField(verbose_name="x坐标值")
    y = models.IntegerField(verbose_name="y坐标值")
    health = models.FloatField(verbose_name="生命值")
    type = models.TextField(verbose_name="装备类型")
    weapon = models.FloatField(verbose_name="", default=1)
    equipment_type = models.IntegerField(verbose_name='原始装备类型', default=2)
    point3d=models.ForeignKey('Point3D',on_delete=models.CASCADE,null=True,blank=True)

    isControlledByAi=models.BooleanField(verbose_name='是否为AI分配目的地',default=True)
    is_human_target_changed = models.BooleanField(verbose_name='是否更新目的地', default=False)
    target_building = models.ForeignKey('BuildingTarget',verbose_name='指定目的地', blank=True, null=True, related_name='agent_red_set',
                                        on_delete=models.CASCADE)
    load_ability = models.BooleanField(verbose_name='是否能装载飞机', default=False)

    # 角度变换
    destination_angle_horizon = models.FloatField(verbose_name='目标角度', blank=True, null=True)
    current_angle_horizon = models.FloatField(verbose_name='当前角度', blank=True, null=True)

    destination_angle_vertical = models.FloatField(verbose_name='目标角度', blank=True, null=True)
    current_angle_vertical = models.FloatField(verbose_name='当前角度', blank=True, null=True)
    angel_range_horizon = models.FloatField(verbose_name='旋转角度范围', default=30)
    angel_range_vertical = models.FloatField(verbose_name='旋转角度范围', default=20)


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
    point3d = models.ForeignKey('Point3D', on_delete=models.CASCADE,null=True,blank=True)
    equipment_type = models.IntegerField(verbose_name='原始装备类型', default=2)
    pos_type=models.IntegerField(verbose_name='位置信息', default=2)



#存储被红方检测到的蓝方敌人
class EnemyTargetOfRed(models.Model):
    vid = models.IntegerField(verbose_name="agent唯一编号",unique=True)
    x = models.IntegerField(verbose_name="x坐标值")
    y = models.IntegerField(verbose_name="y坐标值")
    health = models.FloatField(verbose_name="生命值")
    type = models.TextField(verbose_name="装备类型")
    weapon = models.FloatField(verbose_name="武器杀伤力", default=1)
    isVisible = models.BooleanField(verbose_name="是否从视野中消失")
    point3d = models.ForeignKey('Point3D', on_delete=models.CASCADE,null=True,blank=True)
    equipment_type = models.IntegerField(verbose_name='原始装备类型', default=2)
    pos_type = models.IntegerField(verbose_name='位置信息', default=2)

class BuildingTarget(models.Model):
    vid=models.IntegerField(verbose_name="设备唯一编号",unique=True)
    x = models.IntegerField(verbose_name="x坐标值")
    y = models.IntegerField(verbose_name="y坐标值")
    values=models.FloatField(verbose_name="夺控地点价值",default=1)
    point3d = models.ForeignKey('Point3D', on_delete=models.CASCADE,null=True,blank=True)
    capture_type=models.IntegerField(verbose_name='夺控点的类型',default=7)
    is_static=models.BooleanField(verbose_name='是否为静态夺控点',default=True)
    is_active=models.BooleanField(verbose_name='是不是新节点',default=False)

    stage=models.IntegerField(verbose_name='推演阶段',default=1)
    in_stage=models.IntegerField(verbose_name='在这个阶段',default=False)
    #1红方 2 蓝方 0 不管
    whichTeam=models.IntegerField(verbose_name='属于哪一方的智能体',default=0)
    distance_range=models.FloatField(verbose_name='单兵达标距离',default=5)
    is_air_release=models.BooleanField(verbose_name='是否是飞机释放点',default=False)
    is_single_release=models.BooleanField(verbose_name='是否为下车点',default=False)

    is_ready_to_load=models.BooleanField(verbose_name='是否准备装载',default=False)
    is_ready_to_left=models.BooleanField(verbose_name='是否准备离开',default=False)

    load_distance_range=models.FloatField(verbose_name='装载范围',default=20)

    thread_rate=models.FloatField(verbose_name='到达率',default=0)

    #0是未完成 1是已经完成 2是该阶段结束
    status=models.IntegerField(verbose_name='是否完成',default=0)

class ObstacleTarget(models.Model):
    vid=models.IntegerField(verbose_name="障碍物唯一编号",unique=True)
    x = models.IntegerField(verbose_name="x坐标值")
    y = models.IntegerField(verbose_name="y坐标值")
    health = models.FloatField(verbose_name="生命值")
    point3d = models.ForeignKey('Point3D', on_delete=models.CASCADE,null=True,blank=True)

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

    # in_out_points=models.ManyToManyField('Point3D',null=True,blank=True)



class Apartment(models.Model):
  root_map=models.ForeignKey(RootMap,on_delete=models.CASCADE)
  floor=models.IntegerField(verbose_name='层数')
  file_name=models.TextField(verbose_name='目标地图名称')
  height_floor=models.FloatField(verbose_name='楼层高度下界',default=0)
  height_ceil=models.FloatField(verbose_name='楼层高度上界',default=1)
  height_upper=models.FloatField(verbose_name='小于该值则属于该楼层')
  up_points = models.ManyToManyField('Point3D', null=True, blank=True,related_name='down_apartments')
  down_points=models.ManyToManyField('Point3D', null=True, blank=True,related_name='up_apartments')
  class Meta:
      unique_together=("root_map","floor")

class Point3D(models.Model):
    #编号形式为ABXXX,A是地图编号，B是楼层编号，XXX是 Hospital编号暂且定义为：21999
    vid=models.IntegerField(verbose_name='point3d唯一编号',blank=True,null=True,unique=True)

    is_in_map=models.BooleanField(verbose_name='是否在地图中',default=True)
    self_apartment=models.ForeignKey(Apartment,on_delete=models.CASCADE,related_name='self_point_set')

    is_up_point_of_apartment=models.BooleanField(verbose_name='是否是上楼点',default=False)
    is_down_point_of_apartment=models.BooleanField(verbose_name='是否是上楼点',default=False)
    #if is_junction=true
    is_junction=models.BooleanField(verbose_name='是否为连接点')
    connected_apartment = models.ForeignKey(Apartment, null=True, blank=True, on_delete=models.CASCADE,related_name='connected_point_set')

    up_point=models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE,related_name='down_point_set')
    down_point=models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE,related_name='up_point_set')

    #if is_in_map=false
    float_x = models.FloatField(verbose_name='3D坐标x', blank=True, null=True)

    float_z = models.FloatField(verbose_name='3D坐标z', blank=True, null=True)

    #都要有
    float_height = models.FloatField(verbose_name='3D坐标y', blank=True, null=True)
    #if is_in_map=true
    int_x=models.IntegerField(verbose_name='所对应apartment中的点x',blank=True, null=True)
    int_y=models.IntegerField(verbose_name='所对应的apartment中的点y',blank=True, null=True)

    agent_vid=models.IntegerField(verbose_name='假设是agent的位置，则传入agent的id',default=-1)

    is_static=models.BooleanField(verbose_name='是否为静态的点',default=True)

    is_air_stop=models.BooleanField(verbose_name='是否为当前驻留点',default=False)

    is_agent=models.BooleanField(verbose_name='是否为装备节点',default=False)
    class Meta:
        unique_together = ("float_x", "float_height","float_z",'agent_vid')


