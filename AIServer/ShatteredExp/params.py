UNITY_MAP_LEN=6

COLLIDER_HEIGHT=1
COLLIDER_HEIGHT_BIAS=0.3

COLLIDER_WIDTH=1.15
COLLIDER_THICKNESS=1.15

A_STAR_MIDDLE_X=int(26)
A_STAR_MIDDLE_Y=int(73)

A_STAR_LEFT_X=int(27)
A_STAR_LEFT_Y=int(57)

A_STAR_LEFT_2_X=int(29)
A_STAR_LEFT_2_Y=int(30)
POINT_HOSPITAL_VID=21999

#三个参数需要通过Stage来做出修改
STAGE_1_VID=21100001
STAGE_1_X_Y=[23,33]

STAGE_2_VID=22100001
STAGE_2_X_Y=[24,24]

STAGE_3_VID=23100001
STAGE_3_X_Y=[19,15]

STAGE_4_VID=24000001
STAGE_4_X_Y=[27,9]

STAGE_VIDS=[STAGE_1_VID,STAGE_2_VID,STAGE_3_VID,STAGE_4_VID]
STAGE_X_Ys=[STAGE_1_X_Y,STAGE_2_X_Y,STAGE_3_X_Y,STAGE_4_X_Y]

TARGET_VID=28000001
TARGET_X_Y=[23,3]
STAGE_SPLIT=True
HUMAN_TARGET_BIAS=80000000

GOVERMENT_VID=6
global_map_params={"vid":1,
                   'name':'GlobalMap',
                  'start_pos_x':-500,
                  'start_pos_y':-400,
                  'end_pos_x':700,
                  'end_pos_y':1000,
                  'pos_interval':0.2,
                  'stripe':100,
                  'local_path': '/../PreMap/GlobalMap/',
                  # 'floor_gap':300,
                  'base_height':0,}

goverment_map_params={"vid":6,
                   'name':'Goverment',
                  'start_pos_x':-25,
                  'start_pos_y':-311,
                  'end_pos_x':75,
                  'end_pos_y':-269,
                  'pos_interval':1,
                  'stripe':1,
                  'local_path': '/../PreMap/GovermentMap/',
                  # 'floor_gap':300,
                  'base_height':0,}









#
# TVStation_map_params={"vid":6,
#                    'name':'TVStationMap',
#                   'start_pos_x':-140,
#                   'start_pos_y':298,
#                   'end_pos_x':-98,
#                   'end_pos_y':358,
#                   'pos_interval':1,
#                   'stripe':1,
#                   'local_path': '/../PreMap/TVStationMap/',
#                   # 'floor_gap':3.1,
#                   'base_height':0.4,}



apartment_globalmap_floor_1={
    'floor': 1,
    'file_name': '3.png',
    'height_ceil': 300,
    'height_floor': 0.4,
    'height_upper': 300,
}

apartment_goverment_floor_1={
    'floor': 1,
    'file_name': '1.png',
    'height_ceil': 4.37,
    'height_floor': 0.8,
    'height_upper': 4.37,
}

apartment_goverment_floor_2={
    'floor': 2,
    'file_name': '2.png',
    'height_ceil': 7.6,
    'height_floor':4.37,
    'height_upper': 7.6,
}
apartment_goverment_floor_3={
    'floor': 3,
    'file_name': '3.png',
    'height_ceil': 10.7,
    'height_floor':7.6,
    'height_upper': 10.7,
}
apartment_goverment_floor_4={
    'floor': 4,
    'file_name': '4.png',
    'height_ceil': 13.87,
    'height_floor':10.7,
    'height_upper': 13.87,
}
apartment_goverment_floor_5={
    'floor': 5,
    'file_name': '5.png',
    'height_ceil': 17,
    'height_floor':13.87,
    'height_upper': 17,
}

apartment_goverment_floor_6={
    'floor': 6,
    'file_name': '6.png',
    'height_ceil': 20.2,
    'height_floor':17,
    'height_upper': 20.2,
}

apartment_goverment_floor_7={
    'floor': 7,
    'file_name': '7.png',
    'height_ceil': 23.3,
    'height_floor':20.2,
    'height_upper': 23.3,
}

apartment_goverment_floor_8={
    'floor': 8,
    'file_name': '8.png',
    'height_ceil': 26.5,
    'height_floor':23.3,
    'height_upper':26.5,
}

apartment_goverment_floor_9={
    'floor': 9,
    'file_name': '9.png',
    'height_ceil': 30,
    'height_floor':26.5,
    'height_upper':30,
}




point_global_to_goverment_7={'self_root_map_vid':1,
                        'self_floor':1,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,
                        'vid':11007,
                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':6,
                        'connected_floor':1,
                        'float_x':50,
                        'float_z':-264,
                        'float_height':1,
                        'agent_vid':-1}



point_goverment_floor_1_down={'self_root_map_vid':6,
                        'self_floor':1,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':True,
                        'vid':71001,
                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':1,
                        'connected_floor':1,
                        'float_x':50,
                        'float_z':-272,
                        'float_height':0.4,
                        'agent_vid':-1}

point_goverment_floor_1_up={'self_root_map_vid':6,
                        'self_floor':1,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,
                        'vid':71002,
                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':2,
                        'float_x':24,
                        'float_z':-293.5,
                        'float_height':1.1,
                        'agent_vid':-1}

point_goverment_floor_1_stair_1={'self_root_map_vid':6,
                        'self_floor':1,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,
                        'vid':71003,
                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':2,
                        'float_x':24,
                        'float_z':-295.3,
                        'float_height':1.68,
                        'agent_vid':-1}

point_goverment_floor_1_stair_2={'self_root_map_vid':6,
                        'self_floor':1,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,
                        'vid':71004,
                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':2,
                        'float_x':24,
                        'float_z':-297,
                        'float_height':2.57,
                        'agent_vid':-1}

point_goverment_floor_1_stair_3={'self_root_map_vid':6,
                        'self_floor':1,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,
                        'vid':71005,
                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':2,

                        'float_x':24,
                        'float_z':-299,
                        'float_height':3.13,
                        'agent_vid':-1}

point_goverment_floor_1_stair_4={'self_root_map_vid':6,
                        'self_floor':1,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,
                        'vid':71006,
                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':2,
                        'float_x':25.716,
                        'float_z':-298.99,
                        'float_height':3.13,
                        'agent_vid':-1}

point_goverment_floor_1_stair_5={'self_root_map_vid':6,
                        'self_floor':1,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,
                        'vid':71007,
                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':2,
                        'float_x':27,
                        'float_z':-297.2,
                        'float_height':3.374,
                        'agent_vid':-1}


point_goverment_floor_1_stair_6={'self_root_map_vid':6,
                        'self_floor':1,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':2,

                        'vid':71008,
                        'float_x':26.92,
                        'float_z':-295.434,
                        'float_height':3.944,
                        'agent_vid':-1}


point_goverment_floor_2_down={'self_root_map_vid':6,
                        'self_floor':2,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':True,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':1,

                        'vid': 72001,
                        'float_x':26.92,
                        'float_z':-293.598,
                        'float_height':4.8,
                        'agent_vid':-1}

point_goverment_floor_2_up={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':2,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':3,

                        'vid':72002,
                        'float_x':25.108,
                        'float_z':-293.598,
                        'float_height':4.8,
                        'agent_vid':-1}


point_goverment_floor_2_stair_1={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':2,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':3,

                        'vid':72003,
                        'float_x':23.8,
                        'float_z':-295.096,
                        'float_height':4.912,
                        'agent_vid':-1}


point_goverment_floor_2_stair_2={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':2,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':3,

                        'vid':72004,
                        'float_x':23.8,
                        'float_z':-296.756,
                        'float_height':5.831,
                        'agent_vid':-1}


point_goverment_floor_2_stair_3={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':2,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':3,

                        'vid':72005,
                        'float_x':23.8,
                        'float_z':-298.324,
                        'float_height':5.831,
                        'agent_vid':-1}

point_goverment_floor_2_stair_4={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':2,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':3,

                        'vid':72006,
                        'float_x':26.603,
                        'float_z':-296.79,
                        'float_height':6.75,
                        'agent_vid':-1}

point_goverment_floor_2_stair_5={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':2,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':3,

                        'vid':72007,
                        'float_x':26.603,
                        'float_z':-295.194,
                        'float_height':7.564,
                        'agent_vid':-1}

#第三层
point_goverment_floor_3_down={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':3,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':True,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':2,

                        'vid': 73001,
                        'float_x':26.603,
                        'float_z':-293.429,
                        'float_height':7.921,
                        'agent_vid':-1}

point_goverment_floor_3_up={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':3,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':4,

                        'vid':73002,
                        'float_x':29.96,
                        'float_z':-293.429,
                        'float_height':7.921,
                        'agent_vid':-1}
#3->4楼梯
point_goverment_floor_3_stair_1={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':3,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':4,

                        'vid':73003,
                        'float_x':29.96,
                        'float_z':-295.132,
                        'float_height':8.192,
                        'agent_vid':-1}

point_goverment_floor_3_stair_2={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':3,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':4,

                        'vid':73004,
                        'float_x':29.96,
                        'float_z':-297.023,
                        'float_height':8.694,
                        'agent_vid':-1}

point_goverment_floor_3_stair_3={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':3,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':4,

                        'vid':73005,
                        'float_x':29.96,
                        'float_z':-298.941,
                        'float_height':9.125,
                        'agent_vid':-1}

point_goverment_floor_3_stair_4={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':3,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':4,

                        'vid':73006,
                        'float_x':28.1,
                        'float_z':-299.5,
                        'float_height':9.125,
                        'agent_vid':-1}


point_goverment_floor_3_stair_5={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':3,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':4,

                        'vid':73007,
                        'float_x':26.65,
                        'float_z':-297.513,
                        'float_height':9.697,
                        'agent_vid':-1}

point_goverment_floor_3_stair_6={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':3,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':4,

                        'vid':73008,
                        'float_x':26.65,
                        'float_z':-295.955,
                        'float_height':10.343,
                        'agent_vid':-1}
#四楼
point_goverment_floor_4_down={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':4,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':True,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':3,

                        'vid': 74001,
                        'float_x':26.65,
                        'float_z':-294.003,
                        'float_height':10.824,
                        'agent_vid':-1}

point_goverment_floor_4_up={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':4,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':5,

                        'vid':74002,
                        'float_x':24.81,
                        'float_z':-294.003,
                        'float_height':10.824,
                        'agent_vid':-1}

point_goverment_floor_4_stair_1={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':4,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':5,

                        'vid':74003,
                        'float_x':23.911,
                        'float_z':-295.8,
                        'float_height':11.59,
                        'agent_vid':-1}

point_goverment_floor_4_stair_2={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':4,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':5,

                        'vid':74004,
                        'float_x':23.911,
                        'float_z':-297.946,
                        'float_height':12.307,
                        'agent_vid':-1}

point_goverment_floor_4_stair_3={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':4,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':5,

                        'vid':74005,
                        'float_x':25.74,
                        'float_z':-299.025,
                        'float_height':12.307,
                        'agent_vid':-1}

point_goverment_floor_4_stair_4={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':4,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':5,

                        'vid':74006,
                        'float_x':27.078,
                        'float_z':-297.311,
                        'float_height':13,
                        'agent_vid':-1}

point_goverment_floor_4_stair_5={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':4,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':5,

                        'vid':74007,
                        'float_x':27.078,
                        'float_z':-295.426,
                        'float_height':13.608,
                        'agent_vid':-1}


#五楼
point_goverment_floor_5_down={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':5,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':True,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':4,

                        'vid': 75001,
                        'float_x':27.078,
                        'float_z':-293.531,
                        'float_height':14.068,
                        'agent_vid':-1}

point_goverment_floor_5_up={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':5,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':6,

                        'vid':75002,
                        'float_x':24.21,
                        'float_z':-293.17,
                        'float_height':14.1,
                        'agent_vid':-1}

point_goverment_floor_5_stair_1={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':5,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':6,

                        'vid':75003,
                        'float_x':23.86,
                        'float_z':-295.042,
                        'float_height':14.644,
                        'agent_vid':-1}

point_goverment_floor_5_stair_2={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':5,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':6,

                        'vid':75004,
                        'float_x':23.86,
                        'float_z':-296.95,
                        'float_height':15.43,
                        'agent_vid':-1}

point_goverment_floor_5_stair_3={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':5,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':6,

                        'vid':75005,
                        'float_x':23.86,
                        'float_z':-298.776,
                        'float_height':15.739,
                        'agent_vid':-1}

point_goverment_floor_5_stair_4={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':5,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':6,

                        'vid':75006,
                        'float_x':26.097,
                        'float_z':-299.817,
                        'float_height':15.739,
                        'agent_vid':-1}

point_goverment_floor_5_stair_5={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':5,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':6,

                        'vid':75007,
                        'float_x':26.536,
                        'float_z':-297.857,
                        'float_height':16.294,
                        'agent_vid':-1}

point_goverment_floor_5_stair_6={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':5,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':6,

                        'vid':75008,
                        'float_x':26.536,
                        'float_z':-296.006,
                        'float_height':16.716,
                        'agent_vid':-1}
#六楼
point_goverment_floor_6_down={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':6,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':True,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':5,

                        'vid': 76001,
                        'float_x':26.536,
                        'float_z':-294.025,
                        'float_height':17.28,
                        'agent_vid':-1}

point_goverment_floor_6_up={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':6,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':7,

                        'vid':76002,
                        'float_x':23.94,
                        'float_z':-294.025,
                        'float_height':17.28,
                        'agent_vid':-1}

point_goverment_floor_6_stair_1={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':6,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':7,

                        'vid':76003,
                        'float_x':23.94,
                        'float_z':-295.8,
                        'float_height':18.069,
                        'agent_vid':-1}

point_goverment_floor_6_stair_2={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':6,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':7,

                        'vid':76004,
                        'float_x':23.94,
                        'float_z':-297.54,
                        'float_height':18.85,
                        'agent_vid':-1}

point_goverment_floor_6_stair_3={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':6,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':7,

                        'vid':76005,
                        'float_x':25.015,
                        'float_z':-299.254,
                        'float_height':19.093,
                        'agent_vid':-1}

point_goverment_floor_6_stair_4={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':6,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':7,

                        'vid':76006,
                        'float_x':26.432,
                        'float_z':-297.71,
                        'float_height':19.093,
                        'agent_vid':-1}

point_goverment_floor_6_stair_5={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':6,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':7,

                        'vid':76007,
                        'float_x':26.432,
                        'float_z':-295.866,
                        'float_height':19.53,
                        'agent_vid':-1}


point_goverment_floor_7_down={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':7,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':True,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':6,

                        'vid': 77001,
                        'float_x': 26.432,
                        'float_z': -294.008,
                        'float_height': 20.287,
                        'agent_vid':-1}

point_goverment_floor_7_up={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':7,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':8,

                        'vid':77002,
                        'float_x':29.99,
                        'float_z':-294.008,
                        'float_height':20.287,
                        'agent_vid':-1}

point_goverment_floor_7_stair_1={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':7,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':8,

                        'vid':77003,
                        'float_x':29.99,
                        'float_z':-295.85,
                        'float_height':20.97,
                        'agent_vid':-1}

point_goverment_floor_7_stair_2={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':7,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':8,

                        'vid':77004,
                        'float_x':29.99,
                        'float_z':-297.74,
                        'float_height':21.79,
                        'agent_vid':-1}

point_goverment_floor_7_stair_3={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':7,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':8,

                        'vid':77005,
                        'float_x':28.13,
                        'float_z':-299.5,
                        'float_height':22.377,
                        'agent_vid':-1}

point_goverment_floor_7_stair_4={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':7,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':8,

                        'vid':77006,
                        'float_x':26.871,
                        'float_z':-297.59,
                        'float_height':22.984,
                        'agent_vid':-1}

point_goverment_floor_7_stair_5={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':7,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':8,

                        'vid':77007,
                        'float_x':26.871,
                        'float_z':-295.644,
                        'float_height':23.424,
                        'agent_vid':-1}

#八楼
point_goverment_floor_8_down={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':8,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':True,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':7,

                        'vid': 78001,
                        'float_x': 26.871,
                        'float_z': -293.781,
                        'float_height': 24.054,
                        'agent_vid':-1}

point_goverment_floor_8_up={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':8,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':9,

                        'vid':78002,
                        'float_x':24.23,
                        'float_z':-293.781,
                        'float_height':24.054,
                        'agent_vid':-1}

point_goverment_floor_8_stair_1={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':8,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':9,

                        'vid':78003,
                        'float_x':24.23,
                        'float_z':-295.66,
                        'float_height':24.62,
                        'agent_vid':-1}


point_goverment_floor_8_stair_2={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':8,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':9,

                        'vid':78004,
                        'float_x':24.23,
                        'float_z':-297.55,
                        'float_height':25.24,
                        'agent_vid':-1}

point_goverment_floor_8_stair_3={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':8,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':9,

                        'vid':78005,
                        'float_x':26.02,
                        'float_z':-299.02,
                        'float_height':25.53,
                        'agent_vid':-1}

point_goverment_floor_8_stair_4={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':8,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':9,

                        'vid':78006,
                        'float_x':27.1,
                        'float_z':-297.49,
                        'float_height':25.62,
                        'agent_vid':-1}

point_goverment_floor_8_stair_5={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':8,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':9,

                        'vid':78007,
                        'float_x':26.09,
                        'float_z':-295.507,
                        'float_height':25.62,
                        'agent_vid':-1}

point_goverment_floor_9_down={'self_root_map_vid':GOVERMENT_VID,
                        'self_floor':9,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':True,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':GOVERMENT_VID,
                        'connected_floor':8,

                        'vid': 79001,
                        'float_x': 26.02,
                        'float_z': -293.79,
                        'float_height': 26.72,
                        'agent_vid':-1}

from enum import  Enum

class PointType(Enum):
    IN_MAP=1
    IN_STAIRS=2


AIR_DETECT_POINT = 1
AIR_FIRE_POINT = 2

AIR_DEFENSE_POINT = 3

IND_DETECT_POINT = 4
IND_FIRE_POINT = 5

OUTD_DETECT_POINT = 6
OUTD_FIRE_POINT = 7

OUT_AIR_DENFENSE_POINT = 8

ALL_TYPE = 9

capture_type_2_int={
    "air_detect_point":1,
    1:"air_detect_point",

    "air_fire_point":2,
    2:"air_fire_point",

    'air_defense_point':3,
    3:'air_defense_point',

    'ind_detect_point':4,
    4:'ind_detect_point',

    'ind_fire_point':5,
    5:'ind_fire_point',

    'outd_detect_point':6,
    6:'outd_detect_point',

    'outd_fire_point':7,
    7:'outd_fire_point',

    'out_air_defense_point':8,
    8:'out_air_defense_point',
    'all_type':9,
    9:'all_type',
}



equipment_type_2_int={
    'outd_detect_unit':1,
    1:'outd_detect_unit',

    'outd_fire_unit':2,
    2:'outd_fire_unit',

    'air_detect_unit':3,
    3:'air_detect_unit',

    'air_fire_unit':4,
    4:'air_fire_unit',

    'ind_detect_unit':5,
    5:'ind_detect_unit',

    'ind_fire_unit':6,
    6:'ind_fire_unit',

    'air_defence_unit':7,
    7:'air_defence_unit',

    'engineer':8,
    8:'engineer',
    'out_air_defence_unit':9,
    9:'out_air_defence_unit',

    10:'out_air_floor_unit',
    'out_air_floor_unit':10,

    11:'cant_move_unit',
    'cant_move_unit':11,
}
INDOOR_POS=1
OUTDOOR_POS=2
AIR_POS=3
pos_type_2_int={
    'indoor_pos':1,
    1:'indoor_pos',

    'outdoor_pos':2,
    2:'outdoor_pos',

    'air_pos':3,
    3:'air_pos',
}

dynamic_hopital_point={
    'float_x':-63,
    'float_height':17.53,
    'float_z':75,
    'rootmap_vid':2,
    'apartment_floor':6,
    'agent_vid':POINT_HOSPITAL_VID,

}


OUTDOOR_DETECT=1
OUTDOOR_FIRE=2
AIR_DETECT=3
AIR_FIRE=4
IND_DETECT=5
IND_FIRE=6
AIR_DEFENSE=7
ENGINEER=8
OUT_AIR_DEFENSE=9
OUT_AIR_FLOOR=10
CANT_MOVE=11
# outdoor_detect_ls=[2,6,14,13,15,36,39,40]
# outdoor_fire_ls=[1,3,9,16,17,20,22,83,8]
# air_detect_ls=[12,19,26,27,28,29,31,32]
# #8 仅能对地 需要改进
# air_fire_ls=[7,37,38]
# ind_detect_ls=[11,23,86]
# ind_fire_ls=[10,33,34,35,84,85]
# #21，24仅能在室外 需改进
#
# air_defense_ls=[5,18,25,72]
#
# out_air_defense_ls=[21,24]
#
# out_air_floor_ls=[46,48]
#
# cant_move_ls=[]
# engineer=[]
load_ability=[11001,12005,22007,22008,22010,30008]
loaded_ability=[26001,26002,26004]
outdoor_detect_ls=[11001,11008,11009,11010,11011,11012,11013,12005,12012,12013,12015,12016,12017,12018,12018,13001
,13002,13003,13004,13005,13006,13007,
                   13008,13009,13010,13011,13012,21002,21003,21004,21005,21006,30001,30002,30007,30008,27002]
outdoor_fire_ls=[12001,12002,12004,12014,21001,22001,12003,22003,22007,22008,22009,23001,23002,23003,23004,23005,23006,
                 23007,23008,23009]
air_detect_ls=[11002,11003,11004,11005,11006,11007,25001,25002,25004,25006,25007,25008,30004,30005,
               30006]
#8 仅能对地 需要改进
air_fire_ls=[25003,25005]
ind_detect_ls=[30003,]
ind_fire_ls=[12008,12009,12010,26001,26002,26004]
#21，24仅能在室外 需改进

air_defense_ls=[12011,24002,26003]

out_air_defense_ls=[23010,24001]

out_air_floor_ls=[22002,22004,22005,22006]

cant_move_ls=[12006,12007,27001]
engineer=[]
def is_in(number,ls):
    for _digit in ls:
          if number==_digit:
              return  True

    return  False
#servertype 映射表
def servertype_2_equip_type(serverType):
    if is_in(serverType,outdoor_detect_ls):
        return  OUTDOOR_DETECT
    elif is_in(serverType,outdoor_fire_ls):
        return  OUTDOOR_FIRE
    elif is_in(serverType,air_detect_ls):
        return  AIR_DETECT
    elif is_in(serverType,air_fire_ls):
        return  AIR_FIRE
    elif is_in(serverType,ind_detect_ls):
        return  IND_DETECT
    elif is_in(serverType,ind_fire_ls):
        return  IND_FIRE
    elif is_in(serverType,air_defense_ls):
        return  AIR_DEFENSE
    elif is_in(serverType,engineer):
        return  ENGINEER
    elif is_in(serverType,out_air_defense_ls):
        return OUT_AIR_DEFENSE
    elif is_in(serverType,out_air_floor_ls):
        return OUT_AIR_FLOOR
    else:
        return CANT_MOVE

name_map={"Single":"Engineer",
          "Vehicle":"ArmoredCar",
          "AirCraft":"Military_Helicopter"}

BUILDING_RED=1
BUILDING_BLUE=2
BUILDING_DEFAULT=3