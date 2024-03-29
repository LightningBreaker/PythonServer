# from  AIServer.ShatteredExp.models import *
# from  AIServer.rules_project.param import *
# from  AIServer.ShatteredExp.params import *
from django.db import IntegrityError
from  .models import *
from  rules_project.param import *
from  .params import *

#用于判断该点属于那一张图，哪一个点后返回
def get_start_point(which_team,vid):
    if which_team==0:
        Agent=AgentRed
    else:
        Agent=AgentBlue
    agent= Agent.objects.get(vid=vid)

    return  agent.point3d,agent

def get_end_point(target_vid,enemy_target_list,obstacle_list,building_list,my_agent_list):
    if target_vid==POINT_HOSPITAL_VID:
        return  Point3D.objects.get(agent_vid=POINT_HOSPITAL_VID)
    for obstacle in obstacle_list:
        if obstacle.vid==target_vid:
            return  obstacle.point3d

    for enemy_target in enemy_target_list:
        if enemy_target.isVisible !=True or enemy_target.x<0 or enemy_target.y<0 or enemy_target.x>=Map_Width or enemy_target.y>=Map_Length:
            continue

        if enemy_target.vid==target_vid:
            return  enemy_target.point3d


    for building in building_list:
        if building.x<0 or building.y<0 or building.x>=Map_Width or building.y>=Map_Length:
            continue

        if building.vid==target_vid:
            return  building.point3d

    for my_agent in my_agent_list:
        if my_agent.vid==target_vid:
            return  my_agent.point3d

    return Point3D.objects.exclude(vid__isnull=True).get(vid=POINT_HOSPITAL_VID)

#主函数
#start_point:is_in_map?True:False, ，
def transform_destination(which_team,vid,target_vid,enemy_target_list,obstacle_list,building_list,my_agent_list,human_target_point=None
                          ,para_agent=None):

    if para_agent !=None:
        start_point, my_agent=para_agent.point3d,para_agent
    else:
        start_point,my_agent=get_start_point(which_team,vid)
    # if start_point==None:
    #     print('Its None:'+start_point)
    # else:
    #     print('Its None:' +str(start_point.float_x)+','+str(start_point.float_z)+')')
   # print('start_point_vid:'+str(start_point.vid)+' ######################## vid:'+str(vid))

    if human_target_point!=None:
        end_point=human_target_point
    else:
        end_point=get_end_point(target_vid,enemy_target_list,obstacle_list,building_list,my_agent_list)

    if my_agent !=None and (my_agent.equipment_type==AIR_FIRE or my_agent.equipment_type==AIR_DETECT or start_point.float_height>=48):
            return True,False,transform_in_air(start_point,end_point),my_agent


    if start_point.is_in_map:
        if start_point.self_apartment.root_map.vid == end_point.self_apartment.root_map.vid:
          #     print('in the same maaaaap~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                return True,True,tranform_in_map(start_point,end_point),my_agent

        else:
        #    print('in the different maaaaap~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            if start_point.self_apartment.root_map.vid==1: #startpoint在global内，而endpoint不在
                enter_points= start_point.self_apartment.up_points.all()
                for enter_point in enter_points:
                    if end_point.self_apartment.root_map.vid==enter_point.connected_apartment.root_map.vid:
                        if start_point.is_up_point_of_apartment and start_point.connected_apartment.root_map.vid==end_point.self_apartment.root_map.vid:
                            return  True,True,enter_point.up_point,my_agent
                        else:
                            return True,True,enter_point,my_agent
                return  False,True,None,my_agent
            elif end_point.self_apartment.root_map.vid==1: #startpoint在楼内，endpoint在global内
               # print('start in building end in global~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                #修改
                # print('end_point x:' + str(end_point.float_x) + ' end_point z:' + str( \
                #    end_point.float_z) + ' end_point_height:' + str(end_point.float_height))
                if start_point.self_apartment.floor==1 and start_point.is_down_point_of_apartment:
                    if start_point.down_point==None:
                        print('error in building->global :junction')
                    return True,True,start_point.down_point,my_agent
                input_end_point=start_point.self_apartment.root_map.apartment_set.all().get(floor=1).down_points.first()
                if input_end_point==None:
              #      print('End point is None start point apartment:'+str(start_point.self_apartment.floor)+' root_map_vid:'+str(start_point.self_apartment.root_map.vid))
                    isOk=False
                    ret_point=None
                else:
                    isOk=True
                    ret_point=tranform_in_map(start_point,input_end_point)
                    if ret_point==None:
                        print('error in building->global :Not junction')
                return isOk,True,ret_point,my_agent

            else:
            #    print('start in building end in building~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                if start_point.self_apartment.floor==1 and start_point.is_down_point_of_apartment:
                    return True,True,start_point.down_point,my_agent
                else:
                    input_end_point = start_point.self_apartment.root_map.apartment_set.all().get(floor=1).down_points.first()
                    if input_end_point == None:
                        print('End point is None start point apartment:' + str(
                            start_point.self_apartment.floor) + ' root_map_vid:' + str(
                            start_point.self_apartment.root_map.vid))
                        isOk = False
                        ret_point = None
                    else:
                        isOk = True
                        ret_point = tranform_in_map(start_point, input_end_point)
                        if ret_point == None:
                            print('error in building->global :Not junction')
                    return isOk, True, ret_point, my_agent


    else: #start_point 在楼梯上
        if start_point.self_apartment.root_map.vid==end_point.self_apartment.root_map.vid:
            if start_point.float_height>end_point.float_height:
                return True,False,start_point.down_point,my_agent

            else:

                return True,False,start_point.up_point,my_agent

        else:
            return  True,False,start_point.down_point,my_agent

from math import sqrt
TOLERANCE_DISTANCE=10
def transform_in_air(start_point,end_point):
    stop_point=end_point
    while stop_point.down_point!=None and stop_point.is_air_stop==False:
        stop_point=stop_point.down_point
        if stop_point.vid==end_point.vid:
            break

    delta_distance= sqrt((start_point.float_x - stop_point.float_x) ** 2+(start_point.float_z-stop_point.float_z)**2)

    if delta_distance<=TOLERANCE_DISTANCE and stop_point.down_point!=None:
        stop_point.is_air_stop=False
        stop_point.save()
        stop_point.down_point.is_air_stop=True
        stop_point.down_point.save()
        stop_point=stop_point.down_point

    return stop_point




def tranform_in_map(start_point,end_point):
        #同楼同层一张图
        if start_point==None:
            print("start point is None in same map~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if end_point==None:
            print("end point is None in same map~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if start_point.self_apartment.floor==end_point.self_apartment.floor:
            return end_point
        #同楼不同层
        else:
            if start_point.float_height>end_point.float_height:
                down_point= start_point.self_apartment.down_points.all().first()
                if start_point.is_down_point_of_apartment:
                    return  start_point.down_point
                else:
                    if down_point==None:
                        print(' same map downpoint is none: apartment'+str(start_point.self_apartment.floor)+' root_map:'+str(start_point.self_apartment.root_map.vid))
                    return  down_point

            else:
                up_point=  start_point.self_apartment.up_points.all().first()
                if start_point.is_up_point_of_apartment:
                    return  up_point.up_point
        
                else:
                    return  up_point

def transform_float_pos_to_int(root_map,float_x,float_z):
    int_x=int(((float_x-root_map.start_pos_x)+0.1)/(root_map.pos_interval*root_map.stripe))
    int_y=int(((float_z-root_map.start_pos_y)+0.1)/(root_map.pos_interval*root_map.stripe))

    return  int_x,int_y
##静态添加一个Point3D
def addStaticPoint3D(self_root_map_vid,self_floor,is_up_point_of_apartment,is_down_point_of_apartment, \
                     vid,is_in_map,is_junction,connected_root_map_vid,connected_floor,float_x,float_z,float_height,agent_vid=-1,is_air_stop=False):
    points_static= Point3D.objects.filter(vid=vid)
    if len(points_static)>0:
        return points_static.first()
    self_root_map=RootMap.objects.get(vid=self_root_map_vid)
    int_x, int_y = transform_float_pos_to_int(self_root_map,float_x,float_z)
    self_apartment=self_root_map.apartment_set.get(floor=self_floor)

    point3d=Point3D()
    point3d.self_apartment=self_apartment
    point3d.vid=vid
    point3d.is_in_map=is_in_map
    point3d.is_junction=is_junction
    if connected_root_map_vid !=None and connected_floor!=None:
        connected_root_map=RootMap.objects.get(vid=connected_root_map_vid)
        connected_apartment=connected_root_map.apartment_set.get(floor=connected_floor)
        point3d.connected_apartment=connected_apartment
    point3d.float_x=float_x
    point3d.float_z=float_z
    point3d.float_height=float_height
    point3d.int_x=int_x
    point3d.int_y=int_y
    point3d.agent_vid=agent_vid
    point3d.is_up_point_of_apartment=is_up_point_of_apartment
    point3d.is_down_point_of_apartment=is_down_point_of_apartment
    point3d.is_air_stop=is_air_stop
    point3d.save()

    if is_up_point_of_apartment:
        self_apartment.up_points.add(point3d)
        self_apartment.save()
    if is_down_point_of_apartment:
        self_apartment.down_points.add(point3d)
        self_apartment.save()
    return point3d
    #TODO 添加apartment up 和apartment down

from datetime import datetime
import time
#TODO 保证vid要唯一
def updateDynamicPoint3D(float_x,float_height,float_z,rootmap_vid,apartment_floor,agent_vid=-1,is_agent=False):

    time_start = datetime.now()
    time_end0 = time_start
    time_end1 = time_start
    time_end2 = time_start
    time_end3 = time_start
    points= Point3D.objects.exclude(agent_vid=-1).filter(is_agent=is_agent).filter(agent_vid=agent_vid)
    # time_end1 = datetime.now()
    if len(points)>0:
       # points.delete()
        ret_point= addDynamicPoint3D(float_x, float_height, float_z, rootmap_vid, apartment_floor,
                                 agent_vid,points.first(),is_agent)
        time_end0 = datetime.now()
    elif agent_vid!=-1:
        ret_point= addDynamicPoint3D(float_x,float_height,float_z,rootmap_vid,apartment_floor,agent_vid,is_agent=is_agent)
        time_end1 = datetime.now()
    else: #agent_vid=-1
         points= Point3D.objects.filter(float_x=float_x).filter(float_z=float_z).filter(float_height=float_height)
         if len(points)>0:
             ret_point=  points.first()
             time_end2 = datetime.now()
         else:
             ret_point= addDynamicPoint3D(float_x,float_height,float_z,rootmap_vid,apartment_floor,agent_vid,is_agent)
             time_end3 = datetime.now()

    durn0 = (time_end0 - time_start).microseconds // 1000
    durn1 = (time_end1 - time_start).microseconds // 1000
    durn2 = (time_end2 - time_start).microseconds // 1000
    durn3 = (time_end3 - time_start).microseconds // 1000
    print('--------------------updateDynamicPoint3D 0:' + str(durn0) + ' 1:' + str(durn1) + '------------------------'+
          ' 2:'+str(durn2)+' 3:'+str(durn3))
    return  ret_point




def addDynamicPoint3D(float_x,float_height,float_z,rootmap_vid,apartment_floor,agent_vid=-1,point3d=None,is_agent=False):
    time_start0=datetime.now()
    if point3d==None:
        point3d = Point3D()
    rootmap = RootMap.objects.all().get(vid=rootmap_vid)
    apartment = rootmap.apartment_set.get(floor=apartment_floor)
    point_vid,point_static=getStaticPointFromRequest(apartment,float_x,float_z,float_height)
    time_end0 = datetime.now()
   # print('-------------------------addDynamic Duration:'+str((time_end0-time_start0).microseconds//1000))
    if point_vid!=-1:

        #point_static=Point3D.objects.get(vid=point_vid)
        int_x, int_y = transform_float_pos_to_int(point_static.self_apartment.root_map, float_x, float_z)

        point3d.is_in_map=point_static.is_in_map
        point3d.self_apartment=point_static.self_apartment
        point3d.is_junction=point_static.is_junction
        point3d.connected_apartment=point_static.connected_apartment
        point3d.up_point=point_static.up_point
        point3d.down_point=point_static.down_point
        point3d.float_x=float_x
        point3d.float_height=float_height
        point3d.float_z=float_z
        point3d.int_x=int_x
        point3d.int_y=int_y
        point3d.agent_vid=agent_vid
        point3d.is_up_point_of_apartment=point_static.is_up_point_of_apartment
        point3d.is_down_point_of_apartment=point_static.is_down_point_of_apartment
        point3d.is_static=False
        try:
            point3d.save()
        except IntegrityError:
            return None
        return point3d

    if(agent_vid==1850013):
        print('Enemy Rootmap: pos_interval'+str(rootmap.pos_interval)+' float x:'+str(float_x)+' z:'+str(float_z)+'stripe:'+str(rootmap.stripe))
    int_x, int_y = transform_float_pos_to_int(rootmap, float_x, float_z)
   # print('###################################')
    # point3d=Point3D()
    point3d.is_in_map=True
    point3d.self_apartment=apartment
    point3d.is_junction=False
    point3d.is_up_point_of_apartment=False
    point3d.is_down_point_of_apartment=False
    #point3d.connected_apartment.connected_point_set.remove(point3d)
    point3d.connected_apartment=None
    point3d.up_point=None
    point3d.down_point=None
    point3d.is_static = False
    point3d.float_x=float_x
    point3d.float_z=float_z
    point3d.float_height=float_height
    point3d.int_x=int_x
    point3d.int_y=int_y
    point3d.agent_vid=agent_vid
    point3d.is_agent=is_agent

    try:
        point3d.save()
    except IntegrityError:
        filtered_point3d=Point3D.objects.filter(float_x=float_x).filter(float_height=float_height).\
            filter(float_z=float_z).filter(agent_vid=agent_vid)
        if filtered_point3d.count()>0:
            return filtered_point3d.first()

        else:
            return None
    return  point3d
    #TODO 增加一个dynamic point

##链接两个Point3D,
def connectTwoPoints(down_point,up_point):
    if up_point!=None:
        up_point.down_point=down_point
        up_point.save()
    if down_point!=None:
        down_point.up_point=up_point
        down_point.save()


def getStaticPointFromRequest(apartment,float_x,float_z,float_height):
    static_points=list(apartment.self_point_set.filter(is_static=True))
    point_vid=-1
    ret_point=None
    for static_point in static_points:
       if abs(float_x-static_point.float_x)<=COLLIDER_WIDTH and abs(float_z-static_point.float_z)<=COLLIDER_THICKNESS \
               and abs(static_point.float_height+COLLIDER_HEIGHT_BIAS-float_height)<=COLLIDER_HEIGHT:
           point_vid=static_point.vid
           ret_point=static_point
           break

    return point_vid,ret_point
