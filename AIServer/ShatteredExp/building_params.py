from .params import *
TOTAL_STAGE=4

INDOOR_DISTANCE=5
OUTDOOR_DISTANCE=10
AIR_DISTANCE=50

THREAD_RATE_1=0.12
THREAD_RATE_2=0.12
THREAD_RATE_3=0.3
THREAD_RATE_4=0.6
#stage1
# w 两个驻留点 1个室内侦察点 1个空中侦察点
QUALIFIED_RATES=[0.9,1,1,1]
QUALIFIED_STAGE_GATHERING_RATES=[0.75,0.75,0.75,0.75]
QUALIFIED_STAGE_GATHERING_DISTANCE=[25,25,25,25]

target_building={
    'vid':28000001,
    'x':23,
    'y':3,
    'value':1,
    'float_x':-40,
    'float_height':0.4,
    'float_z':-340,
    'rootmap_vid':1,
    'apartment_floor':1,
    'capture_type':OUTD_DETECT_POINT,
    'is_static':1,
    'point3d_vid':-1,
    'stage':8,
    'in_stage':False,
    'whichTeam':1,
    'distance_range':OUTDOOR_DISTANCE,
    'is_air_release':False,
    'is_single_release':False,
    'load_distance_range':20,
    'thread_rate': THREAD_RATE_1,
}

#e 两个驻留点  1个室内      1个空中
s_1_w_1={
    'vid':21000001,
    'x':25,
    'y':35,
    'value':1,
    'float_x':0,
    'float_height':0.4,
    'float_z':300,
    'rootmap_vid':1,
    'apartment_floor':1,
    'capture_type':OUTD_DETECT_POINT,
    'is_static':1,
    'point3d_vid':-1,
    'stage':1,
    'in_stage':True,
    'whichTeam':1,
    'distance_range':OUTDOOR_DISTANCE,
    'is_air_release':True,
    'is_single_release':True,
    'load_distance_range':20,
    'thread_rate': THREAD_RATE_1,
}

s_1_w_2 = {
    'vid':21000002,
    'x':25,
    'y':33,
    'value':1,
    'float_x':0,
    'float_height':0.4,
    'float_z':260,
    'rootmap_vid':1,
    'apartment_floor':1,
    'capture_type':OUTD_FIRE_POINT,
    'is_static':1,
    'point3d_vid':-1,
    'stage':1,
    'in_stage':True,
    'whichTeam':1,
    'distance_range':OUTDOOR_DISTANCE,
    'is_air_release':True,
    'is_single_release':True,
    'load_distance_range':20,
    'thread_rate': THREAD_RATE_1,
}

s_1_w_indoor = {
    'vid': 21000003,
    'x': 25,
    'y': 34,
    'value': 1,
    'float_x': 16.72,
    'float_height':13.65,
    'float_z': 292.21,
    'rootmap_vid': 5,
    'apartment_floor': 5,
    'capture_type': IND_DETECT_POINT,
    'is_static': 1,
    'point3d_vid': -1,
    'stage': 1,
    'in_stage': True,
    'whichTeam': 1,
    'distance_range': INDOOR_DISTANCE,
    'is_air_release': False,
    'is_single_release': False,
    'load_distance_range': 20,
    'thread_rate': 0,
    'thread_rate': THREAD_RATE_1,
}

s_1_w_air = {
    'vid': 21000004,
    'x': 25,
    'y': 36,
    'value': 1,
    'float_x': 7.5,
    'float_height':150,
    'float_z': 321.4,
    'rootmap_vid': 1,
    'apartment_floor': 1,
    'capture_type': AIR_DETECT_POINT,
    'is_static': 1,
    'point3d_vid': 12734,
    'stage': 1,
    'in_stage': True,
    'whichTeam': 1,
    'distance_range': AIR_DISTANCE,
    'is_air_release': False,
    'is_single_release': False,
    'load_distance_range': 20,
}

s_1_e_1={
    'vid': 21100001,
    'x': 23,
    'y': 33,
    'value': 1,
    'float_x': -40,
    'float_height': 0.4,
    'float_z': 260,
    'rootmap_vid': 1,
    'apartment_floor': 1,
    'capture_type': ALL_TYPE,
    'is_static': 1,
    'point3d_vid': -1,
    'stage': 1,
    'in_stage': True,
    'whichTeam': 1,
    'distance_range': OUTDOOR_DISTANCE,
    'is_air_release': True,
    'is_single_release': True,
    'load_distance_range': 20,
    'thread_rate': THREAD_RATE_1,
}

s_1_e_2 = {
    'vid': 21100002,
    'x': 23,
    'y': 31,
    'value': 1,
    'float_x': -40,
    'float_height': 0.4,
    'float_z': 220,
    'rootmap_vid': 1,
    'apartment_floor': 1,
    'capture_type': OUTD_FIRE_POINT,
    'is_static': 1,
    'point3d_vid': -1,
    'stage': 1,
    'in_stage': True,
    'whichTeam': 1,
    'distance_range': OUTDOOR_DISTANCE,
    'is_air_release': True,
    'is_single_release': True,
    'load_distance_range': 20,
    'thread_rate': THREAD_RATE_1,
}

s_1_e_indoor_1 = {
    'vid': 21100003,
    'x': 21,
    'y': 32,
    'value': 1,
    'float_x': -63.22,
    'float_height': 8.45,
    'float_z': 246.46,
    'rootmap_vid': 4,
    'apartment_floor': 3,
    'capture_type': IND_DETECT_POINT,
    'is_static': 1,
    'point3d_vid': -1,
    'stage': 1,
    'in_stage': True,
    'whichTeam': 1,
    'distance_range': INDOOR_DISTANCE,
    'is_air_release': False,
    'is_single_release': False,
    'load_distance_range': 20,
    'thread_rate': 0,
}

s_1_e_indoor_2 = {
    'vid': 21100004,
    'x': 22,
    'y': 29,
    'value': 1,
    'float_x': -57.35,
    'float_height': 8.21,
    'float_z':197.45,
    'rootmap_vid': 3,
    'apartment_floor': 3,
    'capture_type': IND_DETECT_POINT,
    'is_static': 1,
    'point3d_vid': -1,
    'stage': 1,
    'in_stage': True,
    'whichTeam': 1,
    'distance_range': INDOOR_DISTANCE,
    'is_air_release': False,
    'is_single_release': False,
    'load_distance_range': 20,
    'thread_rate': 0,
}
s_1_e_air = {
    'vid': 21100005,
    'x': 16,
    'y': 35,
    'value': 1,
    'float_x': -170.2,
    'float_height': 150,
    'float_z': 303.6,
    'rootmap_vid': 1,
    'apartment_floor': 1,
    'capture_type': AIR_DETECT_POINT,
    'is_static': 1,
    'point3d_vid': 12737,
    'stage': 1,
    'in_stage': True,
    'whichTeam': 1,
    'distance_range': AIR_DISTANCE,
    'is_air_release': False,
    'is_single_release': False,
    'load_distance_range': 20,
}

#stage2
s_2_w_1={
    'vid':22000001,
    'x':25,
    'y':26,
    'value':1,
    'float_x':0,
    'float_height':0.4,
    'float_z':120,
    'rootmap_vid':1,
    'apartment_floor':1,
    'capture_type':OUTD_DETECT_POINT,
    'is_static':1,
    'point3d_vid':-1,
    'stage':2,
    'in_stage':False,
    'whichTeam':1,
    'distance_range':OUTDOOR_DISTANCE,
    'is_air_release':True,
    'is_single_release':True,
    'load_distance_range':20,
    'thread_rate': THREAD_RATE_2,
}

s_2_w_2 = {
    'vid':22000002,
    'x':25,
    'y':24,
    'value':1,
    'float_x':0,
    'float_height':0.4,
    'float_z':80,
    'rootmap_vid':1,
    'apartment_floor':1,
    'capture_type':OUTD_FIRE_POINT,
    'is_static':1,
    'point3d_vid':-1,
    'stage':2,
    'in_stage':False,
    'whichTeam':1,
    'distance_range':OUTDOOR_DISTANCE,
    'is_air_release':True,
    'is_single_release':True,
    'load_distance_range':20,
    'thread_rate': THREAD_RATE_2,
}




s_2_e_1={
    'vid': 22100001,
    'x': 24,
    'y': 24,
    'value': 1,
    'float_x': -20,
    'float_height': 0.4,
    'float_z': 80,
    'rootmap_vid': 1,
    'apartment_floor': 1,
    'capture_type': ALL_TYPE,
    'is_static': 1,
    'point3d_vid': -1,
    'stage': 2,
    'in_stage': False,
    'whichTeam': 1,
    'distance_range': OUTDOOR_DISTANCE,
    'is_air_release': True,
    'is_single_release': True,
    'load_distance_range': 20,
    'thread_rate': THREAD_RATE_2,
}

s_2_e_2 = {
    'vid': 22100002,
    'x': 24,
    'y': 22,
    'value': 1,
    'float_x': -20,
    'float_height': 0.4,
    'float_z': 40,
    'rootmap_vid': 1,
    'apartment_floor': 1,
    'capture_type': OUTD_FIRE_POINT,
    'is_static': 1,
    'point3d_vid': -1,
    'stage': 2,
    'in_stage': False,
    'whichTeam': 1,
    'distance_range': OUTDOOR_DISTANCE,
    'is_air_release': True,
    'is_single_release': True,
    'load_distance_range': 20,
    'thread_rate': THREAD_RATE_2,
}

s_2_e_indoor = {
    'vid': 22100004,
    'x': 22,
    'y': 22,
    'value': 1,
    'float_x': -60,
    'float_height': 18.61,
    'float_z': 40.75,
    'rootmap_vid': 2,
    'apartment_floor': 6,
    'capture_type': IND_DETECT_POINT,
    'is_static': 1,
    'point3d_vid': -1,
    'stage': 2,
    'in_stage': False,
    'whichTeam': 1,
    'distance_range': INDOOR_DISTANCE,
    'is_air_release': False,
    'is_single_release': False,
    'load_distance_range': 20,
    'thread_rate': 0,
}

s_2_e_air = {
    'vid': 22100005,
    'x': 20,
    'y': 25,
    'value': 1,
    'float_x': -94.9,
    'float_height': 150,
    'float_z': 105.9,
    'rootmap_vid': 1,
    'apartment_floor': 1,
    'capture_type': AIR_DETECT_POINT,
    'is_static': 1,
    'point3d_vid': 12740,
    'stage': 2,
    'in_stage': False,
    'whichTeam': 1,
    'distance_range': AIR_DISTANCE,
    'is_air_release': False,
    'is_single_release': False,
    'load_distance_range': 20,
}

#stage3
s_3_w_1={
    'vid': 23000001,
    'x': 29,
    'y': 15,
    'value': 1,
    'float_x': 80,
    'float_height': 0.4,
    'float_z': -100,
    'rootmap_vid': 1,
    'apartment_floor': 1,
    'capture_type': ALL_TYPE,
    'is_static': 1,
    'point3d_vid': -1,
    'stage': 3,
    'in_stage': False,
    'whichTeam': 1,
    'distance_range': OUTDOOR_DISTANCE,
    'is_air_release': False,
    'is_single_release': False,
    'load_distance_range': 20,
    'thread_rate': THREAD_RATE_3,
}


s_3_w_air = {
    'vid': 23000002,
    'x': 26,
    'y': 12,
    'value': 1,
    'float_x': 23,
    'float_height': 150,
    'float_z':-152.3,
    'rootmap_vid': 1,
    'apartment_floor': 1,
    'capture_type': AIR_DETECT_POINT,
    'is_static': 1,
    'point3d_vid': 12730,
    'stage': 3,
    'in_stage': False,
    'whichTeam': 1,
    'distance_range': AIR_DISTANCE,
    'is_air_release': False,
    'is_single_release': False,
    'load_distance_range': 20,
    'thread_rate': 0,
}

s_3_e_1={
    'vid': 23100001,
    'x': 19,
    'y': 15,
    'value': 1,
    'float_x': -120,
    'float_height': 0.4,
    'float_z': -100,
    'rootmap_vid': 1,
    'apartment_floor': 1,
    'capture_type': ALL_TYPE,
    'is_static': 1,
    'point3d_vid': -1,
    'stage': 3,
    'in_stage': False,
    'whichTeam': 1,
    'distance_range': OUTDOOR_DISTANCE,
    'is_air_release': True,
    'is_single_release': True,
    'load_distance_range': 20,
    'thread_rate':THREAD_RATE_3,
}


s_3_e_air = {
    'vid': 23100002,
    'x': 22 ,
    'y': 12,
    'value': 1,
    'float_x': -47,
    'float_height': 150,
    'float_z': -152.3,
    'rootmap_vid': 1,
    'apartment_floor': 1,
    'capture_type': AIR_DETECT_POINT,
    'is_static': 1,
    'point3d_vid': 12730,
    'stage': 3,
    'in_stage': False,
    'whichTeam': 1,
    'distance_range': AIR_DISTANCE,
    'is_air_release': False,
    'is_single_release': False,
    'load_distance_range': 20,
    'thread_rate': 0,
}

#stage4
s_4_1={
    'vid': 24000001,
    'x': 27,
    'y': 9,
    'value': 1,
    'float_x': 40,
    'float_height': 0.4,
    'float_z': -220,
    'rootmap_vid': 1,
    'apartment_floor': 1,
    'capture_type': ALL_TYPE,
    'is_static': 1,
    'point3d_vid': -1,
    'stage': 4,
    'in_stage': False,
    'whichTeam': 1,
    'distance_range': OUTDOOR_DISTANCE,
    'is_air_release': True,
    'is_single_release': True,
    'load_distance_range': 20,
    'thread_rate':THREAD_RATE_4,
}

s_4_indoor_1 = {
    'vid': 24000002,
    'x': 27,
    'y': 5,
    'value': 1,
    'float_x': 44.75,
    'float_height': 27.79,
    'float_z':-284.12,
    'rootmap_vid': 6,
    'apartment_floor': 9,
    'capture_type': IND_DETECT_POINT,
    'is_static': 1,
    'point3d_vid': -1,
    'stage': 4,
    'in_stage': False,
    'whichTeam': 1,
    'distance_range': INDOOR_DISTANCE,
    'is_air_release': False,
    'is_single_release': False,
    'load_distance_range': 20,
    'thread_rate':0,
}

s_4_indoor_2 = {
    'vid': 24000003,
    'x': 25,
    'y': 5,
    'value': 1,
    'float_x': -1.1,
    'float_height':27.43,
    'float_z': -284.12,
    'rootmap_vid': 6,
    'apartment_floor': 9,
    'capture_type': IND_DETECT_POINT,
    'is_static': 1,
    'point3d_vid': -1,
    'stage': 4,
    'in_stage': False,
    'whichTeam': 1,
    'distance_range': INDOOR_DISTANCE,
    'is_air_release': False,
    'is_single_release': False,
    'load_distance_range': 20,
    'thread_rate':0,
}

s_4_e_air = {
    'vid': 24000004,
    'x': 27 ,
    'y': 9,
    'value': 1,
    'float_x': 40,
    'float_height': 150,
    'float_z': -220,
    'rootmap_vid': 1,
    'apartment_floor': 1,
    'capture_type': AIR_DETECT_POINT,
    'is_static': 1,
    'point3d_vid': 12730,
    'stage': 4,
    'in_stage': False,
    'whichTeam': 1,
    'distance_range': AIR_DISTANCE,
    'is_air_release': False,
    'is_single_release': False,
    'load_distance_range': 20,
    'thread_rate': 0,
}

def add_static_buildings():
    pass