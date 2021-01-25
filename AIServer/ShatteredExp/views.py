from django.shortcuts import render
from django.http import  HttpResponse
import numpy as np
from  django.http import  JsonResponse
from django.db.models import Q

# Create your views here.
from  AIServer.ShatteredExp.params import *
from AIServer.rules_project.main import  make_decision
from  AIServer.rules_project.param import *
from  AIServer.rules_project.param import Map_Length,Map_Width
from AIServer.ShatteredExp.models import *
from  AIServer.ShatteredExp.destination_transformer import *
from django.db import IntegrityError
# from  ShatteredExp.params import *
# from rules_project.main import  make_decision
# from  rules_project.param import *
# from  rules_project.param import Map_Length,Map_Width
# from ShatteredExp.models import *
# from  ShatteredExp.destination_transformer import *
min_enemy=0
min_building=1
min_obstacles=0

def json_response(data,result=True,message="OK",code=0):
    return  JsonResponse(
        {
            "data":data,
            "result":result,
            "message":message,
            "code":code
        }
    )

def deduceBlue(request,*args,**kwargs):
    x=float(request.POST.get("x_para"))
    y=float(request.POST.get("y_para"))
    z=np.sqrt(x*x+y*y)
    data=dict()
    data["result"]=z

    return  json_response(data)


def pureTest(request,*args,**kwargs):
    return HttpResponse("Hello, world. You're at the polls index.")


#接收到Http请求，第一类，更新己方智能体信息
def updateAgent(request,*args,**kwargs):
    vid=int(request.POST.get('vid'))
    x=int(request.POST.get('x'))
    y=int(request.POST.get('y'))
    health=float(request.POST.get('health'))
    type=request.POST.get('type')
    weapon=float(request.POST.get('weapon'))
    whichteam=int((request.POST.get('whichTeam')))
    totalNums=int((request.POST.get('totalNums')))
   # point_vid=int((request.POST.get('point_vid')))
    float_x=float((request.POST.get('float_x')))
    float_height=float((request.POST.get('float_height')))
    float_z=float((request.POST.get('float_z')))
    rootmap_vid=int((request.POST.get('rootmap_vid')))
    apartment_floor=int((request.POST.get('apartment_floor')))
   # print('rootmap_vid:'+str(rootmap_vid)+' floor'+str(apartment_floor))
    agent_vid=vid
    point3d= updateDynamicPoint3D(float_x, float_height, float_z, rootmap_vid, apartment_floor, agent_vid)
    if whichteam==0: #红f方
        Agent=AgentRed
        agent=AgentRed.objects.filter(vid=vid)
    else: #蓝方
        Agent=AgentBlue
        agent=AgentBlue.objects.filter(vid=vid)

    if agent.count()>0:
        updateAgentLocal(agent.first(),x,y,health,point3d)
    else:
        addAgent(whichteam,vid,x,y,health,type,weapon,point3d)


    current_count= Agent.objects.all().count()
    data = dict()
    data['current_count'] =current_count
    if current_count==totalNums:
        isOk=True
    else:
        isOk=False

    return  json_response(data,isOk)

def updateEnemyTarget(request,*args,**kwargs):
    vid = int(request.POST.get('vid'))
    x = int(request.POST.get('x'))
    y = int(request.POST.get('y'))
    health = float(request.POST.get('health'))
    type = request.POST.get('type')
    weapon = float(request.POST.get('weapon'))
    whichteam = int((request.POST.get('whichTeam')))
    isVisible=int((request.POST.get('isVisible')))
#    point_vid = int((request.POST.get('point_vid')))
    float_x = float((request.POST.get('float_x')))
    float_height = float((request.POST.get('float_height')))
    float_z = float((request.POST.get('float_z')))
    rootmap_vid = int((request.POST.get('rootmap_vid')))
    apartment_floor = int((request.POST.get('apartment_floor')))
    agent_vid = vid
    point3d = updateDynamicPoint3D( float_x, float_height, float_z, rootmap_vid, apartment_floor, agent_vid)
    if whichteam==0:
        EnemyTarget=EnemyTargetOfBlue
    else:
        EnemyTarget=EnemyTargetOfRed

    enemyTarget= EnemyTarget.objects.filter(vid=vid)

    if len(enemyTarget) >0:
        updateEnemyTargetLocal(enemyTarget.first(),x,y,health,isVisible,point3d)
    else:
        try:
            addEnemyTarget(EnemyTarget,vid,x,y,health,type,weapon,whichteam,isVisible,point3d)
        except IntegrityError as e:
            pass
    data=dict()
    return json_response(data)

def updateObstacleTarget(request,*args,**kwargs):
    vid=int(request.POST.get('vid'))
    x=int(request.POST.get('x'))
    y=int(request.POST.get('y'))
    health=float(request.POST.get('health'))
 #   point_vid = int((request.POST.get('point_vid')))
    float_x = float((request.POST.get('float_x')))
    float_height = float((request.POST.get('float_height')))
    float_z = float((request.POST.get('float_z')))
    rootmap_vid = int((request.POST.get('rootmap_vid')))
    apartment_floor = int((request.POST.get('apartment_floor')))
    agent_vid = vid
    point3d = updateDynamicPoint3D(float_x, float_height, float_z, rootmap_vid, apartment_floor, agent_vid)
    obstacleTarget= ObstacleTarget.objects.filter(vid=vid)
    if obstacleTarget.count()>0:
        updateObstacleTargetLocal(obstacleTarget.first(),health,x,y,point3d)
    else:
        try:
            addObstacleTarget(vid,x,y,health,point3d)
        except IntegrityError as e:
            pass

    return  json_response(dict())

def updateBuildingTarget(request,*args,**kwargs):

   vid=int(request.POST.get('vid'))
   x=int(request.POST.get('x'))
   y=int(request.POST.get('y'))
   value=float(request.POST.get('value'))
  # point_vid = int((request.POST.get('point_vid')))
   float_x = float((request.POST.get('float_x')))
   float_height = float((request.POST.get('float_height')))
   float_z = float((request.POST.get('float_z')))
   rootmap_vid = int((request.POST.get('rootmap_vid')))
   apartment_floor = int((request.POST.get('apartment_floor')))
   agent_vid = vid
   point3d = updateDynamicPoint3D(float_x, float_height, float_z, rootmap_vid, apartment_floor, agent_vid)

   buildingTarget=BuildingTarget.objects.filter(vid=vid)
   if buildingTarget.count()>0:
       pass
   else:
       try:
            addBuildingTarget(vid,x,y,value,point3d)
       except IntegrityError as e:
           pass

   return json_response(dict())


def updateDestination(request,*args,**kwargs):
    totalNums=int(request.POST.get('totalNums'))
    whichTeam=int(request.POST.get('whichTeam'))
    if whichTeam==0:
        Agent=AgentRed
    else:
        Agent=AgentBlue
    current_count=Agent.objects.all().count()
    if totalNums==current_count:
        data,isOk=updateDestinationLocal(whichTeam)

    else:
        data=dict()
        isOk=False
    return json_response(data,isOk)
def updateDestinationSingle(request,*args,**kwargs):
    pass
def updateDestinationTest(request,*args,**kwargs):
    totalNums = int(request.POST.get('totalNums'))
    whichTeam = int(request.POST.get('whichTeam'))
    if whichTeam==0:
        Agent=AgentRed
    else:
        Agent=AgentBlue
    current_count=Agent.objects.all().count()
 #   print('hello hello')
    if totalNums==current_count:
        if whichTeam == 0:
            Agent = AgentRed
            EnemyTarget = EnemyTargetOfRed
        else:
            Agent = AgentBlue
            EnemyTarget = EnemyTargetOfBlue
        agent_list = list(Agent.objects.all())
        enemytarget_list = list(EnemyTarget.objects.all().filter(isVisible__exact=True))
        obstacle_list = list(ObstacleTarget.objects.all())
        building_list = list(BuildingTarget.objects.all())
        data=list()
        isOk=False
        for agent,target_destination in zip(agent_list,building_list):
            agent_dict=dict()
            isOk,is_in_map,point3d= transform_destination(whichTeam,agent.vid,target_destination.vid,enemytarget_list,obstacle_list,building_list)
            print('get_vid:'+str(point3d.vid)+'--------------------------------')
            if isOk == False:
                print('######################################## okok2')
                break
            agent_dict['vid']=agent.vid
            agent_dict['float_x']=point3d.float_x
            agent_dict['float_z']=point3d.float_z
            agent_dict['float_height']=point3d.float_height
            if point3d.vid!=None or point3d.vid!=-1:
                    if point3d.self_apartment.root_map.vid != agent.point3d.self_apartment.root_map.vid \
                        or not is_in_map or not point3d.is_in_map:
                        agent_dict['is_in_map'] = False
                    else:
                        agent_dict['is_in_map'] = True
            else:
                agent_dict['is_in_map']=False
            agent_dict['root_map_id']=point3d.self_apartment.root_map.vid
            #改进一下A *
            if point3d.self_apartment.root_map.vid==1 and  (point3d.int_y <= 73 and agent.y>=87) or (point3d.int_y>=87 and agent.y<=73):
                agent_dict['int_x'] = A_STAR_MIDDLE_X
                agent_dict['int_y'] = A_STAR_MIDDLE_Y
            elif point3d.self_apartment.root_map.vid==1 and (point3d.int_y <= 54 and agent.y>=60) or (point3d.int_y>=60 and agent.y<=54):
                agent_dict['int_x'] = A_STAR_LEFT_X
                agent_dict['int_y'] = A_STAR_LEFT_Y
            else:
                agent_dict['int_x'] = point3d.int_x
                agent_dict['int_y'] = point3d.int_y
            agent_dict['floor']=point3d.self_apartment.floor

            data.append(agent_dict)



        if isOk==False:
            data=list()
            return  json_response(data,isOk)
    else:
        data=list()
        isOk=False
    return json_response(data,isOk)
###############################以上是pythonServer调用
def updateDestinationLocal(whichTeam):
    if whichTeam==0:
        Agent=AgentRed
        EnemyTarget=EnemyTargetOfRed
    else:
        Agent=AgentBlue
        EnemyTarget=EnemyTargetOfBlue

    agent_list=list(Agent.objects.all())
    enemytarget_list=list(EnemyTarget.objects.all().filter(isVisible__exact=True))
    obstacle_list=list(ObstacleTarget.objects.all())
    building_list=list(BuildingTarget.objects.all())

    agent_pos_ls=list()
    visible_enemy_pos_ls=list()
    building_target_ls=list()
    obstacle_target_ls=list()
    enemy_target_ls=list()
    agent_ls=list()
    for agent in agent_list:
        if agent.health<=0:
            continue
        if agent.x<0 or agent.x>=Map_Width or agent.y<0 or agent.y>=Map_Length:
            continue
        agent_pos_ls.append([agent.x,agent.y])
        agent_ls.append([agent.vid,agent.x,agent.y,agent.health,name_map[agent.type],agent.weapon])

    for enemy_target in enemytarget_list:
        if enemy_target.health<=0:
            continue
        if enemy_target.x<0 or enemy_target.y<0 or enemy_target.x>=Map_Width or enemy_target.y>=Map_Length:
            continue
        visible_enemy_pos_ls.append([enemy_target.x,enemy_target.y])
        enemy_target_ls.append([enemy_target.vid,enemy_target.x,enemy_target.y,enemy_target.health,name_map[enemy_target.type],enemy_target.weapon])

    for obstacle in obstacle_list:
        if obstacle.health<=0:
            continue
        if obstacle.x<0 or obstacle.y<0 or obstacle.x>=Map_Width or obstacle.y>=Map_Length:
            continue
        obstacle_target_ls.append([obstacle.x,obstacle.y,obstacle.health])

    for building in building_list:

        if building.x<0 or building.y<0 or building.x>=Map_Width or building.y>=Map_Length:
            continue
        building_target_ls.append([building.x,building.y])


    data=list()

    isOk=False
    if len(building_target_ls)>0:
        data=ShatteredAlg(agent_pos_ls,visible_enemy_pos_ls,building_target_ls,obstacle_target_ls,enemy_target_ls,agent_ls)
        isOk=True


    return  data,isOk

###############智能体的代码在这里添加
def ShatteredAlg(agent_pos_ls,visible_enemy_pos_ls,building_target_ls,obstacle_target_ls,enemy_target_ls,agent_ls):
    destinations=list()
    dest_ls=make_decision(agent_pos_ls,visible_enemy_pos_ls,agent_ls,building_target_ls,obstacle_target_ls,enemy_target_ls)
    for agent in dest_ls:
        agent_unit= dict()
        agent_unit['vid']=agent[0]
        agent_unit['x']=agent[1]
        agent_unit['y']=agent[2]
        destinations.append(agent_unit)

    return destinations


def updateEnemyTargetLocal(enemyTarget,x,y,health,isVisible,point3d):
    enemyTarget.x=x
    enemyTarget.y=y
    enemyTarget.health=health
    # 一致转化到地图内
    while point3d.up_point!=None:
        point3d=point3d.up_point
    enemyTarget.point3d=point3d
    if isVisible==1:
       enemyTarget.isVisible = True
    else:
        enemyTarget.isVisible=False
    enemyTarget.save()

def addEnemyTarget(EnemyTarget,vid,x,y,health,type,weapon,whichteam,isVisible,point3d):
    enemyTarget=EnemyTarget()
    enemyTarget.vid=vid
    enemyTarget.x=x
    enemyTarget.y=y
    enemyTarget.health=health
    enemyTarget.type=type
    enemyTarget.weapon=weapon
    enemyTarget.whichteam=whichteam
    #一致转化到地图内
    while point3d.up_point!=None:
        point3d=point3d.up_point
    enemyTarget.point3d=point3d
    if isVisible:
        enemyTarget.isVisible=True
    else:
        enemyTarget.isVisible=False
    enemyTarget.save()
def gameOver(request,*args,**kwargs):
    removeAgent()
    removeEnemyTarget()
    removeBuildingTarget()
    removeObstacleTarget()
    removePoint3d()
    data=dict()
    ######################测试用###########################
    #removeMap()
    return  json_response(data)
#########################################通信代码部分

def gameOverTest(request,*args,**kwargs):
    removeMap()
    return gameOver(request,args,kwargs)
###############################################处理离散化地图的模块
def initializeMap(request,*args,**kwargs):
    addRootMap(**global_map_params)
    addRootMap(**hospital_map_params)
    addRootMap(**fz1_map_params)
    addRootMap(**fz2_map_params)
    addRootMap(**fz3_map_params)
    addRootMap(**TVStation_map_params)
    addRootMap(**goverment_map_params)
    globalmap=RootMap.objects.get(vid=1)
    addApartment(root_map=globalmap,**apartment_globalmap_floor_1)

    hospital=RootMap.objects.get(vid=2)
    addApartment(root_map=hospital,**apartment_hospital_floor_1)
    addApartment(root_map=hospital, **apartment_hospital_floor_2)
    addApartment(root_map=hospital, **apartment_hospital_floor_3)
    addApartment(root_map=hospital, **apartment_hospital_floor_4)
    addApartment(root_map=hospital, **apartment_hospital_floor_5)
    addApartment(root_map=hospital, **apartment_hospital_floor_6)

    fz1=RootMap.objects.get(vid=3)
    addApartment(root_map=fz1,**apartment_fz1_floor_1)
    addApartment(root_map=fz1, **apartment_fz1_floor_2)
    addApartment(root_map=fz1, **apartment_fz1_floor_3)
    addApartment(root_map=fz1, **apartment_fz1_floor_4)
    addApartment(root_map=fz1, **apartment_fz1_floor_5)
    addApartment(root_map=fz1, **apartment_fz1_floor_6)

    fz2 = RootMap.objects.get(vid=4)
    addApartment(root_map=fz2, **apartment_fz2_floor_1)
    addApartment(root_map=fz2, **apartment_fz2_floor_2)
    addApartment(root_map=fz2, **apartment_fz2_floor_3)
    addApartment(root_map=fz2, **apartment_fz2_floor_4)
    addApartment(root_map=fz2, **apartment_fz2_floor_5)
    addApartment(root_map=fz2, **apartment_fz2_floor_6)
    addApartment(root_map=fz2, **apartment_fz2_floor_7)

    fz3 = RootMap.objects.get(vid=5)
    addApartment(root_map=fz3, **apartment_fz3_floor_1)
    addApartment(root_map=fz3, **apartment_fz3_floor_2)
    addApartment(root_map=fz3, **apartment_fz3_floor_3)
    addApartment(root_map=fz3, **apartment_fz3_floor_4)
    addApartment(root_map=fz3, **apartment_fz3_floor_5)

    #TVStation还没有渲染好

    goverment=RootMap.objects.get(vid=7)
    addApartment(root_map=goverment,**apartment_goverment_floor_1)
    addApartment(root_map=goverment, **apartment_goverment_floor_2)
    addApartment(root_map=goverment, **apartment_goverment_floor_3)
    addApartment(root_map=goverment, **apartment_goverment_floor_4)
    addApartment(root_map=goverment, **apartment_goverment_floor_5)
    addApartment(root_map=goverment, **apartment_goverment_floor_6)
    addApartment(root_map=goverment, **apartment_goverment_floor_7)



    initPoint3dPart()
    data=dict()
    return  json_response(data)


def updateMapData(request,*args,**kwargs):
    result=False
    #data=dict()
    data_list=list()
    mapDatas=list(RootMap.objects.all())
    for mapData in mapDatas:
        map_dict=dict()
        map_dict['vid']=mapData.vid
        map_dict['name']=mapData.name
        map_dict['start_pos_x']=mapData.start_pos_x
        map_dict['start_pos_y']=mapData.start_pos_y
        map_dict['end_pos_x']=mapData.end_pos_x
        map_dict['end_pos_y']=mapData.end_pos_y
        map_dict['pos_interval']=mapData.pos_interval
        map_dict['stripe']=mapData.stripe
        map_dict['local_path']=mapData.local_path
        map_dict['base_height']=mapData.base_height
        data_list.append(map_dict)
    data=data_list
    if len(data_list)==UNITY_MAP_LEN:
        result=True
    return json_response(data,result)

def updateApartmentData(request,*args,**kwargs):
        map_vid=int(request.POST.get('map_vid'))
        rootMap=RootMap.objects.get(vid=map_vid)
        apartments= list(rootMap.apartment_set.all())

        apart_ls=list()
        for apartment in apartments:
            apart_dict=dict()
            apart_dict['floor']=apartment.floor
            apart_dict['file_name']=apartment.file_name
            apart_dict['map_vid']=rootMap.vid
            apart_dict['height_ceil']=apartment.height_ceil
            apart_dict['height_floor']=apartment.height_floor
            apart_dict['height_upper']=apartment.height_upper
            apart_ls.append(apart_dict)

        data=apart_ls

        return json_response(data)



##########################################处理离散化地图的模块
#公共部分
#智能体
def enableNumberCapture():
    pass

def disableNumberCapture():
    pass

def addAgent(whichTeam,vid,x,y,health,type,weapon,point3d):
    if whichTeam==0:
        agent=AgentRed()
    else:
        agent=AgentBlue()

    agent.vid=vid
    agent.x=x
    agent.y=y
    agent.health=health
    agent.type=type
    agent.weapon=weapon
    agent.point3d=point3d
    agent.save()



def updateAgentLocal(agent,x,y,health,point3d):
    agent.x=x
    agent.y=y
    agent.health=health
    agent.point3d=point3d
    agent.save()

def removeAgent():
    AgentBlue.objects.all().delete()
    AgentRed.objects.all().delete()


def removePoint3d():
    Point3D.objects.all().filter(is_static=False).delete()

def searchAgent(agent):
    pass

#目标建筑
def addBuildingTarget(vid,x,y,value,point3d):
    buildingTarget = BuildingTarget()
    buildingTarget.vid=vid
    buildingTarget.x =x
    buildingTarget.y = y
    buildingTarget.values = value
    buildingTarget.point3d=point3d
    buildingTarget.save()

def removeBuildingTarget():
    BuildingTarget.objects.all().delete()


#障碍物
def addObstacleTarget(vid,x,y,health,point3d):
    obstacleTarget=ObstacleTarget()
    obstacleTarget.vid=vid
    obstacleTarget.x=x
    obstacleTarget.y=y
    obstacleTarget.health=health
    obstacleTarget.point3d=point3d
    obstacleTarget.save()

def updateObstacleTargetLocal(obstacleTarget,health,x,y,point3d):
    obstacleTarget.health=health
    obstacleTarget.x=x
    obstacleTarget.y=y
    obstacleTarget.point3d=point3d
    obstacleTarget.save()

def removeObstacleTarget():
    ObstacleTarget.objects.all().delete()

def removeEnemyTarget():
    EnemyTargetOfBlue.objects.all().delete()
    EnemyTargetOfRed.objects.all().delete()

def removeMap():
    Apartment.objects.all().delete()
    RootMap.objects.all().delete()
    Point3D.objects.all().filter(is_static=True).delete()

#添加Map
def addRootMap(vid,name,start_pos_x,start_pos_y,end_pos_x,end_pos_y,pos_interval,stripe,local_path,base_height):
    rootmaps= RootMap.objects.filter(vid=vid)
    if len(rootmaps)==0:
        try:
            rootMap = RootMap()
            rootMap.vid = vid
            rootMap.name = name
            rootMap.start_pos_x = start_pos_x
            rootMap.start_pos_y = start_pos_y
            rootMap.end_pos_x = end_pos_x
            rootMap.end_pos_y = end_pos_y
            rootMap.pos_interval = pos_interval
            rootMap.stripe = stripe
            rootMap.local_path = local_path
            rootMap.base_height = base_height
            rootMap.save()
        except IntegrityError as e:
            pass

def addApartment(floor,file_name,root_map,height_floor,height_ceil,height_upper):
    apartment=Apartment()
   # rootMap=RootMap.objects.get(vid=rootMap_vid)
    apartment.floor=floor
    apartment.height_upper=height_upper
    apartment.file_name=file_name
    apartment.height_floor=height_floor
    apartment.height_ceil=height_ceil
    apartment.root_map=root_map
    try:
        apartment.save()
    except IntegrityError:
        pass

def initPoint3dPart():
    #先加入点，后做链接

    #global
    p_global_to_hospital= addStaticPoint3D(**point_global_to_hospital_2)


    #####Hospital
    # 一楼
    p_hospital_to_global= addStaticPoint3D(**point_hostpital_floor_1_down)
    p_hospital_1_up= addStaticPoint3D(**point_hostpital_floor_1_up)
    addStaticPoint3D(**point_hostpital_floor_1_stair_1)
    addStaticPoint3D(**point_hostpital_floor_1_stair_2)
    addStaticPoint3D(**point_hostpital_floor_1_stair_3)
    addStaticPoint3D(**point_hostpital_floor_1_stair_4)
    addStaticPoint3D(**point_hostpital_floor_1_stair_5)
    addStaticPoint3D(**point_hostpital_floor_1_stair_6)

    #二楼
    p_hospital_2_down=addStaticPoint3D(**point_hostpital_floor_2_stair_down)
    p_hospital_2_up= addStaticPoint3D(**point_hostpital_floor_2_stair_up)
    addStaticPoint3D(**point_hostpital_floor_2_stair_1)
    addStaticPoint3D(**point_hostpital_floor_2_stair_2)
    addStaticPoint3D(**point_hostpital_floor_2_stair_3)
    addStaticPoint3D(**point_hostpital_floor_2_stair_4)
    addStaticPoint3D(**point_hostpital_floor_2_stair_5)
    addStaticPoint3D(**point_hostpital_floor_2_stair_6)

    #三楼
    p_hospital_3_down= addStaticPoint3D(**point_hostpital_floor_3_stair_down)
    p_hospital_3_up=addStaticPoint3D(**point_hostpital_floor_3_stair_up)
    addStaticPoint3D(**point_hostpital_floor_3_stair_1)
    addStaticPoint3D(**point_hostpital_floor_3_stair_2)
    addStaticPoint3D(**point_hostpital_floor_3_stair_3)
    addStaticPoint3D(**point_hostpital_floor_3_stair_4)
    addStaticPoint3D(**point_hostpital_floor_3_stair_5)
    addStaticPoint3D(**point_hostpital_floor_3_stair_6)

    # 四楼
    p_hospital_4_down=addStaticPoint3D(**point_hostpital_floor_4_stair_down)
    p_hospital_4_up=addStaticPoint3D(**point_hostpital_floor_4_stair_up)
    addStaticPoint3D(**point_hostpital_floor_4_stair_1)
    addStaticPoint3D(**point_hostpital_floor_4_stair_2)
    addStaticPoint3D(**point_hostpital_floor_4_stair_3)
    addStaticPoint3D(**point_hostpital_floor_4_stair_4)
    addStaticPoint3D(**point_hostpital_floor_4_stair_5)
    addStaticPoint3D(**point_hostpital_floor_4_stair_6)

    #五楼
    p_hospital_5_down = addStaticPoint3D(**point_hostpital_floor_5_stair_down)
    p_hospital_5_up = addStaticPoint3D(**point_hostpital_floor_5_stair_up)
    addStaticPoint3D(**point_hostpital_floor_5_stair_1)
    addStaticPoint3D(**point_hostpital_floor_5_stair_2)
    addStaticPoint3D(**point_hostpital_floor_5_stair_3)
    addStaticPoint3D(**point_hostpital_floor_5_stair_4)
    addStaticPoint3D(**point_hostpital_floor_5_stair_5)
    addStaticPoint3D(**point_hostpital_floor_5_stair_6)


    #六楼
    p_hospital_6_down=addStaticPoint3D(**point_hostpital_floor_6_stair_down)

    ##Global<- Connection ->Hospital
    connectTwoPoints(p_global_to_hospital,p_hospital_to_global)
    ##Hospital_1<- Connection ->Hospital_2
    connect_apartment_floor(p_hospital_1_up.self_apartment,p_hospital_2_down)
    ##Hospital_2<- Connection ->Hospital_3
    connect_apartment_floor(p_hospital_2_up.self_apartment,p_hospital_3_down)
    ##Hospital_3<- Connection ->Hospital_4
    connect_apartment_floor(p_hospital_3_up.self_apartment,p_hospital_4_down)
    ##Hospital_4<- Connection ->Hospital_5
    connect_apartment_floor(p_hospital_4_up.self_apartment, p_hospital_5_down)
    ##Hospital_5<- Connection ->Hospital_6
    connect_apartment_floor(p_hospital_5_up.self_apartment, p_hospital_6_down)



    ##Hospital
def connect_apartment_floor(apartment,upper_point):
    #该层节点
    self_points=apartment.self_point_set.exclude(vid__isnull=True).order_by('vid')
    points_len=len(self_points)

    for i in range(0,points_len):
        point3d=self_points[i]
        if point3d.is_down_point_of_apartment:
            continue
        if i==points_len-1:
            connectTwoPoints(point3d,upper_point)
        else:
            point_post=self_points[i+1]
            connectTwoPoints(point3d,point_post)

