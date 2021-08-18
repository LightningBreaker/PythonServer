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
# from  AIServer.ShatteredExp.destination_transformer import *
import sys,os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')
from  .fz1_params import *
from  .fz3_params import *
from  .fz2_params import *
from  .hospital_params import *
from  .air_points_params import *
from .utils import *
from django.db import IntegrityError
from  .params import *
from rules_project.main import  make_decision
from  rules_project.param import *
from  rules_project.param import Map_Length,Map_Width
from .models import *
from  .destination_transformer import *
import json
from formation_generation.utils import *
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
    server_force_type=int((request.POST.get('serverForceType')))
    is_controlled_by_ai=True if int(request.POST.get('isControlledByAi'))==1 else False
    is_human_target_changed=True if int(request.POST.get('is_human_target_changed'))==1 else False

    azimuth=float((request.POST.get('azimuth')))

    human_target_vid=int(request.POST.get('human_target_vid'))
    if human_target_vid!=-1:
        humanTarget_set=BuildingTarget.objects.filter(is_static=0).filter(vid=human_target_vid)
        if len(humanTarget_set)>0:
            humanTarget=humanTarget_set.first()
            humanTarget.is_active=True
            humanTarget.save()
        else:
            humanTarget=None
    else:
        humanTarget=None
   # print('is_controlled_by_ai'+str(is_controlled_by_ai))
    equipment_type=servertype_2_equip_type(server_force_type)
   # print('rootmap_vid:'+str(rootmap_vid)+' floor'+str(apartment_floor))
    agent_vid=vid
    point3d= updateDynamicPoint3D(float_x, float_height, float_z, rootmap_vid, apartment_floor, agent_vid,is_agent=True)
    if whichteam==0: #红f方
        Agent=AgentRed
        agent=AgentRed.objects.filter(vid=vid)
    else: #蓝方
        Agent=AgentBlue
        agent=AgentBlue.objects.filter(vid=vid)

    if agent.count()>0:
        updateAgentLocal(agent.first(),azimuth,x,y,health,point3d,equipment_type,is_controlled_by_ai,is_human_target_changed,humanTarget)
    else:
        addAgent(whichteam,vid,azimuth,x,y,health,type,weapon,point3d,equipment_type,is_controlled_by_ai,is_human_target_changed,humanTarget)


    current_count= Agent.objects.all().count()
    data = dict()
    data['current_count'] =current_count
    if current_count==totalNums:
        isOk=True
    else:
        isOk=False

    return  json_response(data,isOk)

from django.core.exceptions import ObjectDoesNotExist
# def updateHumanTarget(request,*args,**kwargs):
#     agent_vid=int(request.POST.get('vid'))
#     vid=agent_vid+HUMAN_TARGET_BIAS
#     whichTeam=int((request.POST.get('whichTeam')))
#     human_target_x=float(request.POST.get('human_target_x'))
#     human_target_z=float(request.POST.get('human_target_z'))
#     human_target_height=float(request.POST.get('human_target_height'))
#     rootmap_vid = int((request.POST.get('rootmap_vid')))
#     apartment_floor = int((request.POST.get('apartment_floor')))
#
#     point3d = updateDynamicPoint3D(human_target_x, human_target_height, human_target_z, rootmap_vid, apartment_floor, vid)
#
#     humanTargets = HumanTarget.objects.filter(vid=vid)
#
#     if len(humanTargets) > 0:
#         updateHumanTargetLocal(humanTargets.first(), human_target_x, human_target_z, human_target_height, point3d)
#     else:
#         try:
#             addHumanTarget(agent_vid,vid,whichTeam, human_target_x,human_target_z,human_target_height,point3d)
#         except IntegrityError as e:
#             pass
#     data = dict()
#     return json_response(data)






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
    server_force_type = int((request.POST.get('serverForceType')))
    equipment_type = servertype_2_equip_type(server_force_type)
    if equipment_type==AIR_FIRE or equipment_type==AIR_DETECT or float_height>=60:
        pos_type=AIR_POS
    elif rootmap_vid==1:
        pos_type=OUTDOOR_POS
    else:
        pos_type=INDOOR_POS

    agent_vid = vid
  #  print('UpdateEnemy~~~~~~~~~~~~~~~~~~~~~~~~~~:float x:'+str(float_x)+' float height:'+str(float_height)+' z:' +str(float_z))
    point3d = updateDynamicPoint3D( float_x, float_height, float_z, rootmap_vid, apartment_floor, agent_vid,is_agent=True)
    if whichteam==0:
        EnemyTarget=EnemyTargetOfBlue
    else:
        EnemyTarget=EnemyTargetOfRed

    enemyTarget= EnemyTarget.objects.filter(vid=vid)

    if len(enemyTarget) >0:
        updateEnemyTargetLocal(enemyTarget.first(),x,y,health,isVisible,point3d,pos_type)
    else:
        try:
            addEnemyTarget(EnemyTarget,vid,x,y,health,type,weapon,whichteam,isVisible,point3d,equipment_type,pos_type)
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
    point3d = updateDynamicPoint3D(float_x, float_height, float_z, rootmap_vid, apartment_floor, agent_vid,is_agent=True)
    obstacleTarget= ObstacleTarget.objects.filter(vid=vid)
    if obstacleTarget.count()>0:
        updateObstacleTargetLocal(obstacleTarget.first(),health,x,y,point3d)
    else:
        try:
            addObstacleTarget(vid,x,y,health,point3d)
        except IntegrityError as e:
            pass

    return  json_response(dict())

from datetime import datetime
import time
from .building_params import *
def initializeBuildingTarget():
    addBuildingTargetLocal(**s_1_w_1)
    addBuildingTargetLocal(**s_1_w_2)
    addBuildingTargetLocal(**s_1_w_indoor)
    addBuildingTargetLocal(**s_1_w_air)

    addBuildingTargetLocal(**s_1_e_1)
    addBuildingTargetLocal(**s_1_e_2)
    addBuildingTargetLocal(**s_1_e_indoor_1)
    addBuildingTargetLocal(**s_1_e_indoor_2)
    addBuildingTargetLocal(**s_1_e_air)

    addBuildingTargetLocal(**s_2_w_1)
    addBuildingTargetLocal(**s_2_w_2)
    addBuildingTargetLocal(**s_2_e_1)
    addBuildingTargetLocal(**s_2_e_2)
    addBuildingTargetLocal(**s_2_e_indoor)
    addBuildingTargetLocal(**s_2_e_air)

    addBuildingTargetLocal(**s_3_w_1)
    addBuildingTargetLocal(**s_3_w_air)

    addBuildingTargetLocal(**s_3_e_1)
    addBuildingTargetLocal(**s_3_e_air)

    addBuildingTargetLocal(**s_4_1)
    addBuildingTargetLocal(**s_4_indoor_1)
    addBuildingTargetLocal(**s_4_indoor_2)
    addBuildingTargetLocal(**s_4_e_air)

    addBuildingTargetLocal(**target_building)

def addBuildingTargetLocal(vid,x,y,value,float_x,float_height,float_z,
                           rootmap_vid,apartment_floor,capture_type,
                           is_static,point3d_vid,stage,in_stage,
                           whichTeam,distance_range,is_air_release,
                           is_single_release,load_distance_range=20,thread_rate=0):
    buildingTarget = BuildingTarget.objects.filter(whichTeam=whichTeam).filter(is_static=is_static).filter(vid=vid)


    if buildingTarget.count() > 0:
        pass
    else:
        if point3d_vid == -1:
            point3d = updateDynamicPoint3D(float_x, float_height, float_z, rootmap_vid, apartment_floor, vid)
        else:
            point3d = Point3D.objects.all().get(vid=point3d_vid)
        try:

            addBuildingTarget(vid, x, y, value, point3d, capture_type, is_static,stage,in_stage,
                              whichTeam,distance_range,is_air_release,is_single_release,load_distance_range,
                              thread_rate)
            time_end2 = datetime.now()

        except IntegrityError as e:
            pass

def stepForwardStage(whichTeam,stage,filtered_buildings,stageBuildings=None):
    if stage==TOTAL_STAGE:
        if stageBuildings!=None:
            return  stageBuildings
        else:
            return list(filtered_buildings)
    else:
        filtered_buildings.update(in_stage=False)
        filtered_buildings= BuildingTarget.objects.filter(whichTeam=whichTeam + 1).filter(is_static=1).filter(stage=stage+1)
        filtered_buildings.update(in_stage=True)
        return list(filtered_buildings)


def updateBuildingTargetLocal():
    pass

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
   capture_type=int((request.POST.get('capture_type')))
   is_static=True if int((request.POST.get('is_static')))==1 else False
   point3d_vid=int((request.POST.get('point3d_vid')))
   agent_vid = vid

   time_start=datetime.now()
   time_end0=time_start
   time_end1=time_start
   if point3d_vid==-1:
        point3d = updateDynamicPoint3D(float_x, float_height, float_z, rootmap_vid, apartment_floor, agent_vid)
        time_end0 = datetime.now()
   else:
       point3d=Point3D.objects.all().get(vid=point3d_vid)
       time_end1 = datetime.now()

   durn0 = (time_end0 - time_start).microseconds / 1000
   durn1 = (time_end1 - time_start).microseconds / 1000
   #print('--------------------buildingUpdateTime Update:' + str(durn0) + ' Get:' + str(durn1) + '------------------------')

   buildingTarget=BuildingTarget.objects.filter(is_static=is_static).filter(vid=vid)
   if buildingTarget.count()>0:
       time_end2 = datetime.now()
       pass
   else:
       try:

            addBuildingTarget(vid,x,y,value,point3d,capture_type,is_static)
            time_end2 = datetime.now()

       except IntegrityError as e:
           pass
   durn2 = (time_end2 - time_start).microseconds / 1000-max(durn1,durn0)
   print('--------------------buildingUpdateTime Update:' + str(durn0) + ' Get:' + str(
       durn1) + ' add:' + str(durn2) + '------------------------')
   return json_response(dict())



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
            isOk,is_in_map,point3d,my_agent= transform_destination(whichTeam,agent.vid,target_destination.vid,enemytarget_list,obstacle_list,building_list,agent_list)
         #   print('get_vid:'+str(point3d.vid)+'--------------------------------')
            if isOk == False:
                print('######################################## okok2')
                break
            agent_dict=get_agent_dict(agent.vid,is_in_map,point3d,my_agent)

            data.append(agent_dict)



        if isOk==False:
            data=list()
            return  json_response(data,isOk)
    else:
        data=list()
        isOk=False
    return json_response(data,isOk)

def updateDestination(request,*args,**kwargs):
    totalNums=int(request.POST.get('totalNums'))
    whichTeam=int(request.POST.get('whichTeam'))
    if whichTeam==0:
        Agent=AgentRed
    else:
        Agent=AgentBlue
    current_count=Agent.objects.all().count()
 #   print('##################################### UpdateDestination')
    if totalNums==current_count:
        data,isOk=updateDestinationLocal(whichTeam)

    else:
        data=dict()
        isOk=False
    return json_response(data,isOk)

###############################以上是pythonServer调用


from rules_project import param as rule_param
from  . import params as local_param
from django.db.models import Q
def updateHospitalVid(stage):
#     current_vid=STAGE_VIDS[stage-1]
#     current_x_y=STAGE_X_Ys[stage-1]
#     local_param.POINT_HOSPITAL_VID = current_vid
#     rule_param.Hospital_pos = current_x_y
#     rule_param.Hospital_vid = current_vid
#     return current_vid,current_x_y
      return TARGET_VID,TARGET_X_Y
def get_min_max(variable,tolerance):

    return  variable-tolerance,variable+tolerance
def getStageBuildings(whichTeam):
    filtered_buildings= BuildingTarget.objects.filter(whichTeam=whichTeam+1).filter(is_static=1)
    test_building=filtered_buildings.filter(stage=1).first()

    stage=1
    while test_building.in_stage==False and stage<TOTAL_STAGE:
        stage+=1
        test_building=filtered_buildings.filter(stage=stage).first()
    #此时，已经得到当前阶段，判断该阶段任务是否完成,若未完成，返回当前的building_target，否则
    #更新当前阶段与下一阶段的building
    filtered_buildings=filtered_buildings.filter(stage=stage)

    ground_building_len=filtered_buildings.exclude(capture_type=AIR_DETECT_POINT)\
        .exclude(capture_type=AIR_FIRE_POINT).exclude(capture_type=IND_FIRE_POINT).\
        exclude(capture_type=IND_DETECT_POINT).count()
    indoor_building_len=filtered_buildings.filter(Q(capture_type=IND_FIRE_POINT)|Q(capture_type=IND_DETECT_POINT)).count()
    total_building_len=filtered_buildings.count()
    air_building_len=total_building_len-ground_building_len-indoor_building_len

    current_buildings=list(filtered_buildings)

    current_vid,current_x_y= updateHospitalVid(stage)
    if stage==TOTAL_STAGE:
        return current_vid,current_x_y, current_buildings
    #判断任务是否完成
    if whichTeam==0:
        Agent=AgentRed
    else:
        Agent=AgentBlue

    current_building_len=0
    Agent=Agent.objects.exclude(equipment_type=AIR_DETECT).exclude(equipment_type=AIR_FIRE).exclude(health__lte=0)
    calculate_agent_num=Agent.count()
    indoor_agent_num=Agent.filter(Q(equipment_type=IND_FIRE)|Q(equipment_type=IND_DETECT)).count()

    qualified_num =int( QUALIFIED_RATES[stage - 1] * (total_building_len - air_building_len))

    for building_target in current_buildings:
        building_capture_type=building_target.capture_type
        if building_capture_type==AIR_FIRE_POINT or building_capture_type==AIR_DETECT_POINT:
           # current_building_len+=1
            continue
        if building_target.status==1:
            current_building_len+=1
            continue
        if building_target.status==2:
            current_building_len=qualified_num
            break
        float_x= building_target.point3d.float_x
        float_height=building_target.point3d.float_height
        float_z=building_target.point3d.float_z
        distance_range=building_target.distance_range
        thread_rate=building_target.thread_rate

        min_x,max_x=get_min_max(float_x,distance_range)
        min_height,max_height=get_min_max(float_height,distance_range)
        min_z,max_z=get_min_max(float_z,distance_range)

        agent_nums=  Agent.filter(Q(point3d__float_x__lte=max_x) & Q(point3d__float_x__gte=min_x)) \
            .filter(Q(point3d__float_height__lte=max_height) & Q(point3d__float_height__gte=min_height))\
            .filter(Q(point3d__float_z__lte=max_z)&Q(point3d__float_z__gte=min_z)).count()
        # if thread_rate==0 and agent_nums>0:
        #     building_target.status=1
        #     building_target.save()
        #     current_building_len+=1
        #     continue
        if thread_rate==0:
            num_thread=1
        else:
            num_thread=int(calculate_agent_num*thread_rate)
        accomplished=False
        if agent_nums>=num_thread:
           accomplished=True
        else:
            if (building_capture_type==IND_DETECT_POINT or building_capture_type==IND_FIRE_POINT) :
                # print('==================buildingtarget_distance_range:'+str(building_target.distance_range)
                #       +'agent num:'+str(agent_nums)+'=================================')
                if indoor_agent_num==0:
                   accomplished=True
            else:
                if calculate_agent_num-indoor_agent_num<num_thread:
                    accomplished=True
        if accomplished:
            building_target.status = 1
            building_target.save()
            current_building_len += 1
            continue
    print('===================gathering_nums:' + str(current_building_len)+':'+str(qualified_num) + "=============================")
    if current_building_len>=qualified_num:
        #进入第二阶段,开始集合进入下一阶段
        gathering_places=  list(filtered_buildings.filter(capture_type=ALL_TYPE))
        gather_agent_num=0
        for gathering_place in gathering_places:
            if  gathering_place.status!=2:
                gathering_place.status=2
                gathering_place.save()
            float_x=gathering_place.point3d.float_x
            float_height=gathering_place.point3d.float_height
            float_z=gathering_place.point3d.float_z
            min_x,max_x=get_min_max(float_x,QUALIFIED_STAGE_GATHERING_DISTANCE[stage-1])
            min_height,max_height=get_min_max(float_height,QUALIFIED_STAGE_GATHERING_DISTANCE[stage-1])
            min_z,max_z=get_min_max(float_z,QUALIFIED_STAGE_GATHERING_DISTANCE[stage-1])
            agent_num= Agent.filter(Q(point3d__float_x__lte=max_x) & Q(point3d__float_x__gte=min_x)) \
            .filter(Q(point3d__float_height__lte=max_height) & Q(point3d__float_height__gte=min_height))\
            .filter(Q(point3d__float_z__lte=max_z)&Q(point3d__float_z__gte=min_z)).count()
            gather_agent_num+=agent_num

        print('===================gathering_total_nums:'+str(gather_agent_num)+"=============================")
        if gather_agent_num>=int(QUALIFIED_STAGE_GATHERING_RATES[stage-1]*calculate_agent_num):
                return current_vid,current_x_y, stepForwardStage(whichTeam,stage,filtered_buildings,current_buildings)
        else:
            return current_vid,current_x_y, gathering_places
    else:
        #仍然在本阶段停留
        return current_vid,current_x_y, current_buildings

def updateDestinationLocal(whichTeam):
    if whichTeam==0:
        Agent=AgentRed
        EnemyTarget=EnemyTargetOfRed
    else:
        Agent=AgentBlue
        EnemyTarget=EnemyTargetOfBlue
    ai_or_human=len(Agent.objects.filter(isControlledByAi=True))
    data=list()
    if  ai_or_human>0: #ai

        agent_list=list(Agent.objects.all().filter(isControlledByAi=True))
        enemytarget_list=list(EnemyTarget.objects.all().filter(isVisible__exact=True))
        obstacle_list=list(ObstacleTarget.objects.all())

        if STAGE_SPLIT:
           hospital_vid,hospital_x_y,building_list=getStageBuildings(whichTeam)
        else:
           building_list=list(BuildingTarget.objects.all().filter(is_static=1))
           hospital_vid=TARGET_VID
           hospital_x_y=TARGET_X_Y

        agent_pos_ls, visible_enemy_pos_ls, building_target_ls,\
        obstacle_target_ls, enemy_target_ls, agent_ls,sorted_building_list=data_process(agent_list,enemytarget_list,obstacle_list,building_list)
        isOk = False

        if len(building_target_ls) > 0:
            print("start Update destination by AI Control")
            isOk, data = ShatteredAlg(whichTeam, agent_pos_ls, visible_enemy_pos_ls,
                                      building_target_ls, obstacle_target_ls, enemy_target_ls, agent_ls,
                                      enemytarget_list, obstacle_list, building_list, agent_list,
                                      hospital_vid,hospital_x_y)

    else:
       # agent_list_iter = Agent.objects.all().filter(isControlledByAi=False).filter(is_human_target_changed=1)
      #  enemytarget_list = list(EnemyTarget.objects.all().filter(isVisible__exact=True))
        time0=datetime.now()
        enemytarget_list=[]
       # obstacle_list = list(ObstacleTarget.objects.all())

        obstacle_list=[]
        building_list = list(BuildingTarget.objects.all().filter(is_static=0).filter(is_active=True))
        agent_pos_ls, visible_enemy_pos_ls, building_target_ls, \
        obstacle_target_ls, enemy_target_ls, agent_ls,sorted_building_list = data_process([], enemytarget_list, obstacle_list,
                                                                         building_list)

        isOk = False
        data=list()
        if len(sorted_building_list)>0:
            print("start Update destination by Human Control")
        for building in sorted_building_list:

            if whichTeam==0: # REd
                agent_list=list(building.agent_red_set.all())
                #agent_pos_ls,agent_ls=agent_process(agent_list)
            else:
                agent_list=list(building.agent_blue_set.all())
                #agent_pos_ls, agent_ls = agent_process(agent_list)
            #print('~~~~~~~~~Len of Agent:'+str(len(agent_list)))
            # isOk, data_part = ShatteredAlg(whichTeam, agent_pos_ls, visible_enemy_pos_ls,
            #                           [building_target], obstacle_target_ls, enemy_target_ls, agent_ls,
            #                           enemytarget_list, obstacle_list, building_list, agent_list, [])
            if len(agent_list)==0:
                building.is_active=False
                building.save()
            isOk,data_part=HumanAlg(whichTeam,agent_list,building)

            if isOk:
                data+=data_part

        time1 = datetime.now()
        durn1 = (time1 - time0).microseconds // 1000

        print("----------------------duration 1 cost:" + str(durn1) + " milliseconds-----------------------")




        isOK=True


    return data, isOk

def HumanAlg(whichTeam,agent_list,building_unit):
    destinations = list()
    isOk = True
    for agent in agent_list:
        agent_dict = dict()
        print(' agent vid:'+str(agent.vid)+' target vid:'+str(building_unit.vid))
        try:
            isOk, is_in_map, point3d,my_agent = transform_destination(whichTeam, agent.vid, building_unit.vid, [],
                        [], [],[], \
                        human_target_point=building_unit.point3d,para_agent=agent)
            # print('get_vid:' + str(point3d.vid) + '--------------------------------')
            if isOk == False:
                #   print('######################################## okok2')
                break
            agent_dict=get_agent_dict(agent.vid,is_in_map,point3d,my_agent)
            destinations.append(agent_dict)
        except Point3D.DoesNotExist:
            print('Error agent:id' + str(agent.vid) + ' agent vid:' + str(agent))
            isOk=False
            break

    if isOk == False:
        destinations = list()

    return isOk,destinations

def agent_process(agent_list):
    agent_pos_ls = list()
    agent_ls = list()
    for agent in agent_list:
        if agent.health <= 0:
            continue
        if agent.x < 0 or agent.x >= Map_Width or agent.y < 0 or agent.y >= Map_Length:
            continue
        # if not agent.isControlledByAi:
        #     # agent_human_ls.append([agent.vid])
        #     continue
        agent_pos_ls.append([agent.x, agent.y])
        agent_ls.append(
            [equipment_type_2_int[agent.equipment_type], agent.vid, agent.x, agent.y, agent.vid, agent.health,
             name_map[agent.type], agent.weapon])
    return  agent_pos_ls,agent_ls
def data_process(agent_list,enemytarget_list,obstacle_list,building_list):
    agent_pos_ls = list()
    visible_enemy_pos_ls = list()
    building_target_ls = list()
    obstacle_target_ls = list()
    enemy_target_ls = list()
    agent_ls = list()
    sorted_building_list=list()
    # agent_human_ls=list()
    agent_pos_ls,agent_ls=agent_process(agent_list)

    for enemy_target in enemytarget_list:
        if enemy_target.health <= 0:
            continue
        if enemy_target.x < 0 or enemy_target.y < 0 or enemy_target.x >= Map_Width or enemy_target.y >= Map_Length:
            continue
        visible_enemy_pos_ls.append([enemy_target.x, enemy_target.y])
        enemy_target_ls.append(
            [pos_type_2_int[enemy_target.pos_type], enemy_target.vid, enemy_target.x, enemy_target.y, enemy_target.vid,
             enemy_target.health, name_map[enemy_target.type], enemy_target.weapon])

    for obstacle in obstacle_list:
        if obstacle.health <= 0:
            continue
        if obstacle.x < 0 or obstacle.y < 0 or obstacle.x >= Map_Width or obstacle.y >= Map_Length:
            continue
        obstacle_target_ls.append([obstacle.x, obstacle.y, obstacle.vid, obstacle.health])

    for building in building_list:

        if building.x < 0 or building.y < 0 or building.x >= Map_Width or building.y >= Map_Length:
            continue
        # print('capture type is:'+capture_type_2_int[building.capture_type])
        building_target_ls.append([capture_type_2_int[building.capture_type], building.x, building.y, building.vid])
        sorted_building_list.append(building)
    return agent_pos_ls,visible_enemy_pos_ls,building_target_ls,obstacle_target_ls,enemy_target_ls,agent_ls,sorted_building_list


def get_agent_dict(vid,is_in_map,point3d,my_agent):
    agent_dict=dict()
    agent_dict['vid'] =vid
    agent_dict['float_x'] = point3d.float_x
    agent_dict['float_z'] = point3d.float_z
    agent_dict['float_height'] = point3d.float_height
    if point3d.vid != None or point3d.vid != -1:
        if point3d.self_apartment.root_map.vid != my_agent.point3d.self_apartment.root_map.vid \
                or not is_in_map or not point3d.is_in_map:
            agent_dict['is_in_map'] = False
        else:
            agent_dict['is_in_map'] = True
    else:
        agent_dict['is_in_map'] = False
    agent_dict['root_map_id'] = point3d.self_apartment.root_map.vid
    # 改进一下A *
    # if point3d.self_apartment.root_map.vid == 1 and (point3d.int_y <= 73 and my_agent.y >= 87) or (
    #         point3d.int_y >= 87 and my_agent.y <= 73):
    #     agent_dict['int_x'] = A_STAR_MIDDLE_X
    #     agent_dict['int_y'] = A_STAR_MIDDLE_Y
    # elif point3d.self_apartment.root_map.vid == 1 and (point3d.int_y <= 54 and my_agent.y >= 60) or (
    #         point3d.int_y >= 60 and my_agent.y <= 54):
    #     agent_dict['int_x'] = A_STAR_LEFT_X
    #     agent_dict['int_y'] = A_STAR_LEFT_Y
    # elif point3d.self_apartment.root_map.vid == 1 and (point3d.int_y <= 26 and my_agent.y >= 35) or (
    #         point3d.int_y >= 35 and my_agent.y <= 26):
    #     agent_dict['int_x'] = A_STAR_LEFT_2_X
    #     agent_dict['int_y'] = A_STAR_LEFT_2_Y
    #
    # else:
    angle_horizon,angel_range_horizon,angle_vertical,angel_range_vertical= \
        updateAgentRotation(point3d,my_agent)
    #print("=========================="+str(angle_horizon)+"=========================")
    agent_dict['angle_horizon']=angle_horizon
    agent_dict['angel_range_horizon']=angel_range_horizon
    agent_dict['angle_vertical']=angle_vertical
    agent_dict['angel_range_vertical']=angel_range_vertical
    agent_dict['int_x'] = point3d.int_x
    agent_dict['int_y'] = point3d.int_y
    agent_dict['floor'] = point3d.self_apartment.floor

    return agent_dict

###############智能体的代码在这里添加


def ShatteredAlg(whichTeam,agent_pos_ls,visible_enemy_pos_ls,building_target_ls,obstacle_target_ls,\
                 enemy_target_ls,agent_ls,enemytarget_list,obstacle_list,building_list,my_agent_list,
                 hospital_vid,hospital_x_y):
    destinations=list()
    isOk=True
    if len(agent_pos_ls)>0:
        dest_ls=make_decision(agent_pos_ls,visible_enemy_pos_ls,
                              agent_ls,building_target_ls,obstacle_target_ls,enemy_target_ls,
                              hospital_vid,hospital_x_y)
        for agent in dest_ls:
            agent_dict = dict()
            print(' agent vid:'+str(agent[0])+' target vid:'+str(agent[3]))
            try:
                isOk, is_in_map, point3d,my_agent = transform_destination(whichTeam, agent[0], agent[3], enemytarget_list,
                                                             obstacle_list, building_list,my_agent_list)
                # print('get_vid:' + str(point3d.vid) + '--------------------------------')
                if isOk == False:
                    #   print('######################################## okok2')
                    break
                agent_dict=get_agent_dict(agent[0],is_in_map,point3d,my_agent)
                destinations.append(agent_dict)
            except Point3D.DoesNotExist:
                print('Error agent:id' + str(agent[0]) + ' agent vid:' + str(agent[3]))
                isOk=False
                break



    if isOk == False:
        destinations = list()

    return isOk,destinations

def updateHumanTargetLocal(humanTarget,human_target_x, human_target_z, human_target_height, point3d):
    humanTarget.human_target_x=human_target_x
    humanTarget.human_target_z=human_target_z
    humanTarget.human_target_height=human_target_height
    humanTarget.point3d=point3d
    humanTarget.save()

# def  addHumanTarget(agent_vid,vid,whichTeam, human_target_x,human_target_z,human_target_height,point3d):
#     humanTarget=HumanTarget()
#     humanTarget.agent_vid=agent_vid
#     humanTarget.vid=vid
#     humanTarget.whichTeam=whichTeam
#     humanTarget.human_target_x=human_target_x
#     humanTarget.human_target_z=human_target_z
#     humanTarget.human_target_height=human_target_height
#     humanTarget.point3d=point3d
#     humanTarget.save()

def updateEnemyTargetLocal(enemyTarget,x,y,health,isVisible,point3d,pos_type):
    enemyTarget.x=x
    enemyTarget.y=y
    enemyTarget.health=health
    enemyTarget.pos_type=pos_type
    # 一致转化到地图内
    while point3d.up_point!=None:
        point3d=point3d.up_point
    enemyTarget.point3d=point3d
    if isVisible==1:
       enemyTarget.isVisible = True
    else:
        enemyTarget.isVisible=False
    enemyTarget.save()

def addEnemyTarget(EnemyTarget,vid,x,y,health,type,weapon,whichteam,isVisible,point3d,equipment_type,pos_type):
    enemyTarget=EnemyTarget()
    enemyTarget.vid=vid
    enemyTarget.x=x
    enemyTarget.y=y
    enemyTarget.health=health
    enemyTarget.type=type
    enemyTarget.weapon=weapon
    enemyTarget.whichteam=whichteam
    enemyTarget.equipment_type=equipment_type
    enemyTarget.pos_type=pos_type
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

    # addRootMap(**fz1_map_params)
    #addRootMap(**fz2_map_params)
    # addRootMap(**fz3_map_params)
   # addRootMap(**TVStation_map_params)
    addRootMap(**goverment_map_params)
    globalmap=RootMap.objects.get(vid=1)
    addApartment(root_map=globalmap,**apartment_globalmap_floor_1)

    initializeHospitalMap()

    initializeFz1Map()
    initializeFz2Map()
    initializeFz3Map()

    # fz2 = RootMap.objects.get(vid=4)
    # addApartment(root_map=fz2, **apartment_fz2_floor_1)
    # addApartment(root_map=fz2, **apartment_fz2_floor_2)
    # addApartment(root_map=fz2, **apartment_fz2_floor_3)
    # addApartment(root_map=fz2, **apartment_fz2_floor_4)
    # addApartment(root_map=fz2, **apartment_fz2_floor_5)
    # addApartment(root_map=fz2, **apartment_fz2_floor_6)
    # addApartment(root_map=fz2, **apartment_fz2_floor_7)



    #TVStation还没有渲染好

    goverment=RootMap.objects.get(vid=6)
    addApartment(root_map=goverment,**apartment_goverment_floor_1)
    addApartment(root_map=goverment, **apartment_goverment_floor_2)
    addApartment(root_map=goverment, **apartment_goverment_floor_3)
    addApartment(root_map=goverment, **apartment_goverment_floor_4)
    addApartment(root_map=goverment, **apartment_goverment_floor_5)
    addApartment(root_map=goverment, **apartment_goverment_floor_6)
    addApartment(root_map=goverment, **apartment_goverment_floor_7)
    addApartment(root_map=goverment, **apartment_goverment_floor_8)
    addApartment(root_map=goverment, **apartment_goverment_floor_9)

    # 加一个dynamicpoint3d 作为医院的点
    #updateDynamicPoint3D(**dynamic_hopital_point)
    initPoint3dPart()
    initialize_air_map()
    initializeBuildingTarget()
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



def multi_agent_path_planning(request,*args,**kwargs):
    #处理发来的数据，不可行区域用附近点代替，并在最后包含原点
    inputAgents=request.POST.get('inputAgents')
    print(inputAgents)
    destination_x=float(request.POST.get('destination_x'))
    destination_y=float(request.POST.get('destination_y'))
    destination_z=float(request.POST.get('destination_z'))
    taskType=int(request.POST.get('taskType'))
    whichTeam=int(request.POST.get('whichTeam'))

    agent_dict= json.loads(inputAgents)
    agentList=agent_dict['agentList']
    agent_pos_list,multi_agent_poses,end_coord= process_multi_agent_poses(agentList,[destination_x,destination_y,destination_z])

    #TODO which Team
    result,agents_path= test_cbs_formation(len(agentList),multi_agent_poses,agent_pos_list,taskType,end_coord)
    if result:
        agents_path_json=get_agents_path_json(agents_path,destination_y)

        data=agents_path_json
    else:
        data=list()
    return json_response(data,result=result)

##########################################处理离散化地图的模块
#公共部分
#智能体
def enableNumberCapture():
    pass

def disableNumberCapture():
    pass

def addAgent(whichTeam,vid,azimuth,x,y,health,type,weapon,point3d,equipment_type,is_controlled_by_ai,is_human_target_changed,humanTarget):
    if whichTeam==0:
        agent=AgentRed()
    else:
        agent=AgentBlue()

    agent.destination_angle_horizon=0

    agent.destination_angle_vertical=0


    agent.current_angle_horizon=azimuth

    agent.current_angle_horizon = azimuth
    agent.vid=vid
    agent.x=x
    agent.y=y
    agent.health=health
    agent.type=type
    agent.weapon=weapon
    agent.point3d=point3d
    agent.equipment_type=equipment_type
    agent.isControlledByAi=is_controlled_by_ai
    agent.is_human_target_changed = is_human_target_changed
    agent.target_building = humanTarget
    agent.save()



def updateAgentLocal(agent,azimuth,x,y,health,point3d,equipment_type,is_controlled_by_ai,is_human_target_changed,humanTarget):
    agent.x=x
    agent.y=y
    if agent.destination_angle_horizon==None:
        agent.destination_angle_horizon=0
    if agent.destination_angle_vertical==None:
        agent.destination_angle_vertical=0

    if agent.current_angle_horizon==None:
        agent.current_angle_horizon=azimuth
    if agent.destination_angle_horizon==None:
        agent.current_angle_horizon = azimuth

    agent.health=health
    agent.point3d=point3d
    agent.equipment_type=equipment_type
    agent.isControlledByAi=is_controlled_by_ai
    agent.is_human_target_changed=is_human_target_changed
    agent.target_building=humanTarget
    agent.save()

def removeAgent():
    AgentBlue.objects.all().delete()
    AgentRed.objects.all().delete()


def removePoint3d():
    Point3D.objects.all().filter(is_static=False).delete()

def searchAgent(agent):
    pass

#目标建筑
def addBuildingTarget(vid,x,y,value,point3d,capture_type,is_static,stage=0,in_stage=False,
                           whichTeam=0,distance_range=20,is_air_release=False,
                           is_single_release=False,load_distance_range=20,thread_rate=0):
    buildingTarget = BuildingTarget()
    buildingTarget.vid=vid
    buildingTarget.x =x
    buildingTarget.y = y
    buildingTarget.values = value
    buildingTarget.point3d=point3d
    buildingTarget.capture_type=capture_type
    buildingTarget.is_static=is_static
    buildingTarget.stage=stage
    buildingTarget.in_stage=in_stage
    buildingTarget.whichTeam=whichTeam
    buildingTarget.distance_range=distance_range
    buildingTarget.is_air_release=is_air_release
    buildingTarget.is_single_release=is_single_release
    buildingTarget.load_distance_range=load_distance_range
    buildingTarget.thread_rate=thread_rate
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

    p_global_to_goverment=addStaticPoint3D(**point_global_to_goverment_7)

    ##Goverment
    #一楼
    p_goverment_to_global=addStaticPoint3D(**point_goverment_floor_1_down)
    p_goverment_1_up=addStaticPoint3D(**point_goverment_floor_1_up)
    addStaticPoint3D(**point_goverment_floor_1_stair_1)
    addStaticPoint3D(**point_goverment_floor_1_stair_2)
    addStaticPoint3D(**point_goverment_floor_1_stair_3)
    addStaticPoint3D(**point_goverment_floor_1_stair_4)
    addStaticPoint3D(**point_goverment_floor_1_stair_5)
    addStaticPoint3D(**point_goverment_floor_1_stair_6)

    #二楼
    p_goverment_2_down=addStaticPoint3D(**point_goverment_floor_2_down)
    p_goverment_2_up=addStaticPoint3D(**point_goverment_floor_2_up)
    addStaticPoint3D(**point_goverment_floor_2_stair_1)
    addStaticPoint3D(**point_goverment_floor_2_stair_2)
    addStaticPoint3D(**point_goverment_floor_2_stair_3)
    addStaticPoint3D(**point_goverment_floor_2_stair_4)
    addStaticPoint3D(**point_goverment_floor_2_stair_5)
   # addStaticPoint3D(**point_goverment_floor_2_stair_6)

    #三楼
    p_goverment_3_down = addStaticPoint3D(**point_goverment_floor_3_down)
    p_goverment_3_up = addStaticPoint3D(**point_goverment_floor_3_up)
    addStaticPoint3D(**point_goverment_floor_3_stair_1)
    addStaticPoint3D(**point_goverment_floor_3_stair_2)
    addStaticPoint3D(**point_goverment_floor_3_stair_3)
    addStaticPoint3D(**point_goverment_floor_3_stair_4)
    addStaticPoint3D(**point_goverment_floor_3_stair_5)
    addStaticPoint3D(**point_goverment_floor_3_stair_6)

    #四楼
    p_goverment_4_down = addStaticPoint3D(**point_goverment_floor_4_down)
    p_goverment_4_up = addStaticPoint3D(**point_goverment_floor_4_up)
    addStaticPoint3D(**point_goverment_floor_4_stair_1)
    addStaticPoint3D(**point_goverment_floor_4_stair_2)
    addStaticPoint3D(**point_goverment_floor_4_stair_3)
    addStaticPoint3D(**point_goverment_floor_4_stair_4)
    addStaticPoint3D(**point_goverment_floor_4_stair_5)
    # 五楼
    p_goverment_5_down = addStaticPoint3D(**point_goverment_floor_5_down)
    p_goverment_5_up = addStaticPoint3D(**point_goverment_floor_5_up)
    addStaticPoint3D(**point_goverment_floor_5_stair_1)
    addStaticPoint3D(**point_goverment_floor_5_stair_2)
    addStaticPoint3D(**point_goverment_floor_5_stair_3)
    addStaticPoint3D(**point_goverment_floor_5_stair_4)
    addStaticPoint3D(**point_goverment_floor_5_stair_5)
    addStaticPoint3D(**point_goverment_floor_5_stair_6)

    # 六楼
    p_goverment_6_down = addStaticPoint3D(**point_goverment_floor_6_down)
    p_goverment_6_up = addStaticPoint3D(**point_goverment_floor_6_up)
    addStaticPoint3D(**point_goverment_floor_6_stair_1)
    addStaticPoint3D(**point_goverment_floor_6_stair_2)
    addStaticPoint3D(**point_goverment_floor_6_stair_3)
    addStaticPoint3D(**point_goverment_floor_6_stair_4)
    addStaticPoint3D(**point_goverment_floor_6_stair_5)

    #七楼
    p_goverment_7_down = addStaticPoint3D(**point_goverment_floor_7_down)
    p_goverment_7_up = addStaticPoint3D(**point_goverment_floor_7_up)
    addStaticPoint3D(**point_goverment_floor_7_stair_1)
    addStaticPoint3D(**point_goverment_floor_7_stair_2)
    addStaticPoint3D(**point_goverment_floor_7_stair_3)
    addStaticPoint3D(**point_goverment_floor_7_stair_4)
    addStaticPoint3D(**point_goverment_floor_7_stair_5)

    # 八楼
    p_goverment_8_down = addStaticPoint3D(**point_goverment_floor_8_down)
    p_goverment_8_up = addStaticPoint3D(**point_goverment_floor_8_up)
    addStaticPoint3D(**point_goverment_floor_8_stair_1)
    addStaticPoint3D(**point_goverment_floor_8_stair_2)
    addStaticPoint3D(**point_goverment_floor_8_stair_3)
    addStaticPoint3D(**point_goverment_floor_8_stair_4)
    addStaticPoint3D(**point_goverment_floor_8_stair_5)

    # 九楼
    p_goverment_9_down = addStaticPoint3D(**point_goverment_floor_9_down)

    ##Global<- Connection ->Goverment
    connectTwoPoints(p_global_to_goverment, p_goverment_to_global)
    ##goverment_1<- Connection ->goverment_2
    connect_apartment_floor(p_goverment_1_up.self_apartment, p_goverment_2_down)
    connect_apartment_floor(p_goverment_2_up.self_apartment, p_goverment_3_down)
    connect_apartment_floor(p_goverment_3_up.self_apartment, p_goverment_4_down)
    connect_apartment_floor(p_goverment_4_up.self_apartment, p_goverment_5_down)
    connect_apartment_floor(p_goverment_5_up.self_apartment, p_goverment_6_down)
    connect_apartment_floor(p_goverment_6_up.self_apartment, p_goverment_7_down)
    connect_apartment_floor(p_goverment_7_up.self_apartment, p_goverment_8_down)
    connect_apartment_floor(p_goverment_8_up.self_apartment, p_goverment_9_down)



