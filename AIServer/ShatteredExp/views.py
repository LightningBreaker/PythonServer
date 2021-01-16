from django.shortcuts import render
from django.http import  HttpResponse
import numpy as np
from  django.http import  JsonResponse
from django.db.models import Q

# Create your views here.
# from  AIServer.ShatteredExp.params import *
# from AIServer.rules_project.main import  make_decision
# from  AIServer.rules_project.param import *
# from  AIServer.rules_project.param import Map_Length,Map_Width
# from AIServer.ShatteredExp.models import *
from django.db import IntegrityError
from  ShatteredExp.params import *
from rules_project.main import  make_decision
from  rules_project.param import *
from  rules_project.param import Map_Length,Map_Width
from ShatteredExp.models import *
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
    if whichteam==0: #红f方
        Agent=AgentRed
        agent=AgentRed.objects.filter(vid=vid)
    else: #蓝方
        Agent=AgentBlue
        agent=AgentBlue.objects.filter(vid=vid)

    if agent.count()>0:
        updateAgentLocal(agent.first(),x,y,health)
    else:
        addAgent(whichteam,vid,x,y,health,type,weapon)


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
    if whichteam==0:
        EnemyTarget=EnemyTargetOfBlue
    else:
        EnemyTarget=EnemyTargetOfRed

    enemyTarget= EnemyTarget.objects.filter(vid=vid)

    if len(enemyTarget) >0:
        updateEnemyTargetLocal(enemyTarget.first(),x,y,health,isVisible)
    else:
        try:
            addEnemyTarget(EnemyTarget,vid,x,y,health,type,weapon,whichteam,isVisible)
        except IntegrityError as e:
            pass
    data=dict()
    return json_response(data)

def updateObstacleTarget(request,*args,**kwargs):
    vid=int(request.POST.get('vid'))
    x=int(request.POST.get('x'))
    y=int(request.POST.get('y'))
    health=float(request.POST.get('health'))
    obstacleTarget= ObstacleTarget.objects.filter(vid=vid)
    if obstacleTarget.count()>0:
        updateObstacleTargetLocal(obstacleTarget.first(),health,x,y)
    else:
        try:
            addObstacleTarget(vid,x,y,health)
        except IntegrityError as e:
            pass

    return  json_response(dict())

def updateBuildingTarget(request,*args,**kwargs):

   vid=int(request.POST.get('vid'))
   x=int(request.POST.get('x'))
   y=int(request.POST.get('y'))
   value=float(request.POST.get('value'))


   buildingTarget=BuildingTarget.objects.filter(vid=vid)
   if buildingTarget.count()>0:
       pass
   else:
       try:
            addBuildingTarget(vid,x,y,value)
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


def updateEnemyTargetLocal(enemyTarget,x,y,health,isVisible):
    enemyTarget.x=x
    enemyTarget.y=y
    enemyTarget.health=health
    if isVisible==1:
       enemyTarget.isVisible = True
    else:
        enemyTarget.isVisible=False
    enemyTarget.save()

def addEnemyTarget(EnemyTarget,vid,x,y,health,type,weapon,whichteam,isVisible):
    enemyTarget=EnemyTarget()
    enemyTarget.vid=vid
    enemyTarget.x=x
    enemyTarget.y=y
    enemyTarget.health=health
    enemyTarget.type=type
    enemyTarget.weapon=weapon
    enemyTarget.whichteam=whichteam
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
    hospital=RootMap.objects.get(vid=2)
    addApartment(root_map=hospital,**apartment_hospital_floor_1)
    addApartment(root_map=hospital, **apartment_hospital_floor_2)
    addApartment(root_map=hospital, **apartment_hospital_floor_3)
    addApartment(root_map=hospital, **apartment_hospital_floor_4)
    addApartment(root_map=hospital, **apartment_hospital_floor_5)
    addApartment(root_map=hospital, **apartment_hospital_floor_6)
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
        data=dict()
        apart_ls=list()
        for apartment in apartments:
            apart_dict=dict()
            apart_dict['floor']=apartment.floor
            apart_dict['file_name']=apartment.file_name
            apart_dict['map_vid']=rootMap.vid
            apart_dict['height_ceil']=apartment.height_ceil
            apart_dict['height_floor']=apartment.height_floor
            apart_ls.append(apart_dict)

        data['data']=apart_ls

        return json_response(data)



##########################################处理离散化地图的模块
#公共部分
#智能体
def enableNumberCapture():
    pass

def disableNumberCapture():
    pass

def addAgent(whichTeam,vid,x,y,health,type,weapon):
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
    agent.save()



def updateAgentLocal(agent,x,y,health):
    agent.x=x
    agent.y=y
    agent.health=health
    agent.save()

def removeAgent():
    AgentBlue.objects.all().delete()
    AgentRed.objects.all().delete()



def searchAgent(agent):
    pass

#目标建筑
def addBuildingTarget(vid,x,y,value):
    buildingTarget = BuildingTarget()
    buildingTarget.vid=vid
    buildingTarget.x =x
    buildingTarget.y = y
    buildingTarget.values = value
    buildingTarget.save()

def removeBuildingTarget():
    BuildingTarget.objects.all().delete()


#障碍物
def addObstacleTarget(vid,x,y,health):
    obstacleTarget=ObstacleTarget()
    obstacleTarget.vid=vid
    obstacleTarget.x=x
    obstacleTarget.y=y
    obstacleTarget.health=health
    obstacleTarget.save()

def updateObstacleTargetLocal(obstacleTarget,health,x,y):
    obstacleTarget.health=health
    obstacleTarget.x=x
    obstacleTarget.y=y
    obstacleTarget.save()

def removeObstacleTarget():
    ObstacleTarget.objects.all().delete()

def removeEnemyTarget():
    EnemyTargetOfBlue.objects.all().delete()
    EnemyTargetOfRed.objects.all().delete()

def removeMap():
    Apartment.objects.all().delete()
    RootMap.objects.all().delete()

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

def addApartment(floor,file_name,root_map,height_floor,height_ceil):
    apartment=Apartment()
   # rootMap=RootMap.objects.get(vid=rootMap_vid)
    apartment.floor=floor
    apartment.file_name=file_name
    apartment.height_floor=height_floor
    apartment.height_ceil=height_ceil
    apartment.root_map=root_map
    try:
        apartment.save()
    except IntegrityError:
        pass
