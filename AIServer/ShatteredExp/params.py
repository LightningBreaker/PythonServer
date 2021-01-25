UNITY_MAP_LEN=6

COLLIDER_HEIGHT=1
COLLIDER_HEIGHT_BIAS=0.3

COLLIDER_WIDTH=1
COLLIDER_THICKNESS=1

A_STAR_MIDDLE_X=int(26)
A_STAR_MIDDLE_Y=int(73)

A_STAR_LEFT_X=int(27)
A_STAR_LEFT_Y=int(57)
global_map_params={"vid":1,
                   'name':'GlobalMap',
                  'start_pos_x':-300,
                  'start_pos_y':-400,
                  'end_pos_x':300,
                  'end_pos_y':1000,
                  'pos_interval':0.2,
                  'stripe':50,
                  'local_path': '/../PreMap/GlobalMap/',
                  # 'floor_gap':300,
                  'base_height':0,}

goverment_map_params={"vid":7,
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

hospital_map_params={"vid":2,
                   'name':'HospitalMap',
                  'start_pos_x':-70,
                  'start_pos_y':29,
                  'end_pos_x':-46,
                  'end_pos_y':83,
                  'pos_interval':0.8,
                  'stripe':1,
                  'local_path': '/../PreMap/HospitalMap/',
                  # 'floor_gap':3.34,
                  'base_height':0.6,}



fz1_map_params={"vid":3,
                   'name':'fz1Map',
                  'start_pos_x':-68,
                  'start_pos_y':184,
                  'end_pos_x':-50,
                  'end_pos_y':204,
                  'pos_interval':1,
                  'stripe':1,
                  'local_path': '/../PreMap/Fz1Map/',
                  # 'floor_gap':3.51,
                  'base_height':0.3,}

fz2_map_params={"vid":4,
                   'name':'fz2Map',
                  'start_pos_x':-82,
                  'start_pos_y':208,
                  'end_pos_x':-54,
                  'end_pos_y':252,
                  'pos_interval':1,
                  'stripe':1,
                  'local_path': '/../PreMap/Fz2Map/',
                  # 'floor_gap':3.51,
                  'base_height':0.3,}

fz3_map_params={"vid":5,
                   'name':'fz3Map',
                  'start_pos_x':10,
                  'start_pos_y':262,
                  'end_pos_x':40,
                  'end_pos_y':302,
                  'pos_interval':1,
                  'stripe':1,
                  'local_path': '/../PreMap/Fz3Map/',
                  # 'floor_gap':3.1,
                  'base_height':0.4,}

TVStation_map_params={"vid":6,
                   'name':'TVStationMap',
                  'start_pos_x':-140,
                  'start_pos_y':298,
                  'end_pos_x':-98,
                  'end_pos_y':358,
                  'pos_interval':1,
                  'stripe':1,
                  'local_path': '/../PreMap/TVStationMap/',
                  # 'floor_gap':3.1,
                  'base_height':0.4,}


apartment_hospital_floor_1={
    'floor':1,
    'file_name':'1.png',
    'height_ceil':1.6,
    'height_floor':0.6,
    'height_upper':4.3,
}

apartment_hospital_floor_2={
    'floor':2,
    'file_name':'2.png',
    'height_ceil':5.3,
    'height_floor':4.3,
    'height_upper':7.6,
}

apartment_hospital_floor_3={
    'floor':3,
    'file_name':'3.png',
    'height_ceil':8.6,
    'height_floor':7.6,
    'height_upper':10.9,
}

apartment_hospital_floor_4={
    'floor':4,
    'file_name':'4.png',
    'height_ceil':11.9,
    'height_floor':10.9,
    'height_upper':14.1,
}

apartment_hospital_floor_5={
    'floor':5,
    'file_name':'5.png',
    'height_ceil':15.1,
    'height_floor':14.1,
    'height_upper':17.3,
}

#顶楼
apartment_hospital_floor_6={
    'floor':6,
    'file_name':'6.png',
    'height_ceil':19.3,
    'height_floor':17.3,
    'height_upper': 25,
}

apartment_globalmap_floor_1={
    'floor': 1,
    'file_name': '1.png',
    'height_ceil': 300,
    'height_floor': 0,
    'height_upper': 300,
}

apartment_goverment_floor_1={
    'floor': 1,
    'file_name': '1.png',
    'height_ceil': 4.37,
    'height_floor': 1.1,
    'height_upper': 4.37,
}

apartment_goverment_floor_2={
    'floor': 2,
    'file_name': '2.png',
    'height_ceil': 10.7,
    'height_floor':4.37,
    'height_upper': 10.7,
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
    'file_name': '3.png',
    'height_ceil': 13.87,
    'height_floor':10.7,
    'height_upper': 13.87,
}
apartment_goverment_floor_5={
    'floor': 5,
    'file_name': '4.png',
    'height_ceil': 17,
    'height_floor':13.87,
    'height_upper': 17,
}

apartment_goverment_floor_6={
    'floor': 6,
    'file_name': '5.png',
    'height_ceil': 20.2,
    'height_floor':17,
    'height_upper': 20.2,
}

apartment_goverment_floor_7={
    'floor': 7,
    'file_name': '6.png',
    'height_ceil': 23.3,
    'height_floor':20.2,
    'height_upper': 23.3,
}

apartment_goverment_floor_8={
    'floor': 8,
    'file_name': '7.png',
    'height_ceil': 26.5,
    'height_floor':23.3,
    'height_upper':26.5,
}

apartment_goverment_floor_9={
    'floor': 9,
    'file_name': '7.png',
    'height_ceil': 30,
    'height_floor':26.5,
    'height_upper':30,
}

apartment_fz1_floor_1={
    'floor': 1,
    'file_name': '1.png',
    'height_ceil': 4.2,
    'height_floor':0.3,
    'height_upper': 4.2,
}

apartment_fz1_floor_2={
    'floor': 2,
    'file_name': '2.png',
    'height_ceil': 7.7,
    'height_floor':4.2,
    'height_upper': 7.7,
}

apartment_fz1_floor_3={
    'floor': 3,
    'file_name': '3.png',
    'height_ceil': 10.8,
    'height_floor':7.7,
    'height_upper': 10.8,
}

apartment_fz1_floor_4={
    'floor': 4,
    'file_name': '4.png',
    'height_ceil': 13.8,
    'height_floor':10.8,
    'height_upper': 13.8,
}

apartment_fz1_floor_5={
    'floor': 5,
    'file_name': '5.png',
    'height_ceil': 17.5,
    'height_floor':13.8,
    'height_upper': 17.5,
}

apartment_fz1_floor_6={
    'floor': 6,
    'file_name': '6.png',
    'height_ceil': 20.8,
    'height_floor':17.5,
    'height_upper': 20.8,
}

apartment_fz2_floor_1={
    'floor': 1,
    'file_name': '1.png',
    'height_ceil': 4,
    'height_floor':0.3,
    'height_upper': 4,
}

apartment_fz2_floor_2={
    'floor': 2,
    'file_name': '2.png',
    'height_ceil': 7.5,
    'height_floor':4,
    'height_upper': 7.5,
}

apartment_fz2_floor_3={
    'floor': 3,
    'file_name': '3.png',
    'height_ceil': 10.6,
    'height_floor':7.5,
    'height_upper': 10.6,
}

apartment_fz2_floor_4={
    'floor': 4,
    'file_name': '4.png',
    'height_ceil': 13.8,
    'height_floor':10.6,
    'height_upper': 13.8,
}

apartment_fz2_floor_5={
    'floor': 5,
    'file_name': '5.png',
    'height_ceil': 17.2,
    'height_floor':13.8,
    'height_upper': 17.2,
}

apartment_fz2_floor_6={
    'floor': 6,
    'file_name': '6.png',
    'height_ceil': 21.7,
    'height_floor':17.2,
    'height_upper': 21.7,
}

apartment_fz2_floor_7={
    'floor': 7,
    'file_name': '7.png',
    'height_ceil': 24.2,
    'height_floor':21.7,
    'height_upper': 24.2,
}

apartment_fz3_floor_1={
    'floor': 1,
    'file_name': '1.png',
    'height_ceil': 3.5,
    'height_upper': 3.5,
    'height_floor':0.4,
}

apartment_fz3_floor_2={
    'floor': 2,
    'file_name': '2.png',
    'height_ceil': 6.5,
    'height_upper': 6.5,
    'height_floor':3.5,
}

apartment_fz3_floor_3={
    'floor': 3,
    'file_name': '3.png',
    'height_ceil': 9.6,
    'height_upper': 9.6,
    'height_floor':6.5,
}

apartment_fz3_floor_4={
    'floor': 4,
    'file_name': '4.png',
    'height_ceil': 12.7,
    'height_upper': 12.7,
    'height_floor':9.6,
}

apartment_fz3_floor_5={
    'floor': 5,
    'file_name': '5.png',
    'height_ceil': 16.6,
    'height_upper': 16.6,
    'height_floor':12.7,
}

POINT_HOSPITAL_VID=21999
point_global_to_goverment_7={'self_root_map_vid':1,
                        'self_floor':1,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,
                        'vid':11007,
                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':1,
                        'float_x':40,
                        'float_z':-266,
                        'float_height':1,
                        'agent_vid':-1}

point_global_to_hospital_2={'self_root_map_vid':1,
                        'self_floor':1,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,
                        'vid':11002,
                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':2,
                        'connected_floor':1,
                        'float_x':-45,
                        'float_z':57.8,
                        'float_height':0,
                        'agent_vid':-1}




point_hostpital_floor_1_down={'self_root_map_vid':2,
                        'self_floor':1,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':True,
                        'vid':21001,
                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':1,
                        'connected_floor':1,
                        'float_x':-47.6,
                        'float_z':57.8,
                        'float_height':0.6,
                        'agent_vid':-1}

point_hostpital_floor_1_up={'self_root_map_vid':2,
                        'self_floor':1,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,
                        'vid':21002,
                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':2,
                        'connected_floor':2,
                        'float_x':-62.8,
                        'float_z':66.6,
                        'float_height':1,
                        'agent_vid':-1}

point_hostpital_floor_1_stair_1={'self_root_map_vid':2,
                        'self_floor':1,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,
                        'vid':21003,
                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':2,
                        'connected_floor':2,
                        'float_x':-62.8,
                        'float_z':64.8,
                        'float_height':1.5,
                        'agent_vid':-1}

point_hostpital_floor_1_stair_2={'self_root_map_vid':2,
                        'self_floor':1,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':2,
                        'connected_floor':2,
                        'agent_vid': -1,

                        'float_x':-64.54,
                        'float_z':64.8,
                        'float_height':2,
                        'vid': 21004,
                       }


point_hostpital_floor_1_stair_3 = {'self_root_map_vid': 2,
                                   'self_floor': 1,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 2,
                                   'agent_vid': -1,

                                   'float_x': -65.76,
                                   'float_z': 64.8,
                                   'float_height': 2.69,
                                   'vid': 21005,
                                   }

point_hostpital_floor_1_stair_4 = {'self_root_map_vid': 2,  
                                   'self_floor': 1,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 2,
                                   'agent_vid': -1,

                                   'float_x': -67.77,
                                   'float_z': 64.8,
                                   'float_height': 3.24,
                                   'vid': 21006,
                                   }


point_hostpital_floor_1_stair_5 = {'self_root_map_vid': 2,
                                   'self_floor': 1,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 2,
                                   'agent_vid': -1,

                                   'float_x': -67.77,
                                   'float_z': 66.62,
                                   'float_height': 3.25,
                                   'vid': 21007,
                                   }


point_hostpital_floor_1_stair_6 = {'self_root_map_vid': 2,
                                   'self_floor': 1,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 2,
                                   'agent_vid': -1,

                                   'float_x': -66,
                                   'float_z': 66.624,
                                   'float_height': 3.75,
                                   'vid': 21008,
                                   }


point_hostpital_floor_2_stair_down = {'self_root_map_vid': 2,
                                   'self_floor': 2,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': True,

                                   'is_in_map': True,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 1,
                                   'agent_vid': -1,

                                   'float_x': -64.09,
                                   'float_z': 66.624,
                                   'float_height':4.35,
                                   'vid': 22001,
                                   }

point_hostpital_floor_2_stair_up = {'self_root_map_vid': 2,
                                   'self_floor': 2,
                                   'is_up_point_of_apartment': True,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': True,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 3,
                                   'agent_vid': -1,

                                   'float_x': -62.69,
                                   'float_z': 66.44,
                                   'float_height':4.35,
                                   'vid': 22002,
                                   }

point_hostpital_floor_2_stair_1 = {'self_root_map_vid': 2,
                                   'self_floor': 2,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 3,
                                   'agent_vid': -1,

                                   'float_x': -64.46,
                                   'float_z': 64.44,
                                   'float_height':4.85,
                                   'vid': 22003,
                                   }

point_hostpital_floor_2_stair_2 = {'self_root_map_vid': 2,
                                   'self_floor': 2,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 3,
                                   'agent_vid': -1,

                                   'float_x': -65.96,
                                   'float_z': 64.44,
                                   'float_height':5.35,
                                   'vid': 22004,
                                   }

point_hostpital_floor_2_stair_3 = {'self_root_map_vid': 2,
                                   'self_floor': 2,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 3,
                                   'agent_vid': -1,

                                   'float_x': -67.77,
                                   'float_z': 64.44,
                                   'float_height':5.9,
                                   'vid': 22005,
                                   }

point_hostpital_floor_2_stair_4 = {'self_root_map_vid': 2,
                                   'self_floor': 2,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 3,
                                   'agent_vid': -1,

                                   'float_x': -67.77,
                                   'float_z': 66.56,
                                   'float_height':5.9,
                                   'vid': 22006,
                                   }

point_hostpital_floor_2_stair_5 = {'self_root_map_vid': 2,
                                   'self_floor': 2,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 3,
                                   'agent_vid': -1,

                                   'float_x': -65.9,
                                   'float_z': 66.567,
                                   'float_height':6.4,
                                   'vid': 22007,
                                   }

point_hostpital_floor_2_stair_6 = {'self_root_map_vid': 2,
                                   'self_floor': 2,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 3,
                                   'agent_vid': -1,

                                   'float_x': -64.41,
                                   'float_z': 66.567,
                                   'float_height':6.9,
                                   'vid': 22008,
                                   }
#Hospital 三楼
point_hostpital_floor_3_stair_down = {'self_root_map_vid': 2,
                                   'self_floor': 3,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': True,

                                   'is_in_map': True,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 2,
                                   'agent_vid': -1,

                                   'float_x': -62.9,
                                   'float_z': 66.567,
                                   'float_height':7.6,
                                   'vid': 23001,
                                   }


point_hostpital_floor_3_stair_up = {'self_root_map_vid': 2,
                                   'self_floor': 3,
                                   'is_up_point_of_apartment': True,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': True,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 4,
                                   'agent_vid': -1,

                                   'float_x':-62.836,
                                   'float_z':65.065,
                                   'float_height':7.6,
                                   'vid': 23002,
                                   }

point_hostpital_floor_3_stair_1= {'self_root_map_vid': 2,
                                   'self_floor': 3,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 4,
                                   'agent_vid': -1,

                                   'float_x':-64.581,
                                   'float_z': 64.261,
                                   'float_height':8.1,
                                   'vid': 23003,
                                   }


point_hostpital_floor_3_stair_2= {'self_root_map_vid': 2,
                                   'self_floor': 3,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 4,
                                   'agent_vid': -1,

                                   'float_x':-66.527,
                                   'float_z': 64.54,
                                   'float_height':8.7,
                                   'vid': 23004,
                                   }


point_hostpital_floor_3_stair_3= {'self_root_map_vid': 2,
                                   'self_floor': 3,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 4,
                                   'agent_vid': -1,

                                   'float_x':-67.59 ,
                                   'float_z': 64.661,
                                   'float_height':9.4,
                                   'vid': 23005,
                                   }

point_hostpital_floor_3_stair_4= {'self_root_map_vid': 2,
                                   'self_floor': 3,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 4,
                                   'agent_vid': -1,

                                   'float_x':-67.59,
                                   'float_z': 66.462,
                                   'float_height':9.4,
                                   'vid': 23006,
                                   }

point_hostpital_floor_3_stair_5= {'self_root_map_vid': 2,
                                   'self_floor': 3,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 4,
                                   'agent_vid': -1,

                                   'float_x':-66.21,
                                   'float_z': 66.462,
                                   'float_height':10,
                                   'vid': 23007,
                                   }

point_hostpital_floor_3_stair_6= {'self_root_map_vid': 2,
                                   'self_floor': 3,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 4,
                                   'agent_vid': -1,

                                   'float_x':-64.821,
                                   'float_z': 66.462,
                                   'float_height':10.5,
                                   'vid': 23008,
                                   }

point_hostpital_floor_4_stair_down={'self_root_map_vid': 2,
                                   'self_floor': 4,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': True,

                                   'is_in_map': True,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 3,
                                   'agent_vid': -1,

                                   'float_x':-63.202,
                                   'float_z':66.582,
                                   'float_height':11,
                                   'vid': 24001,
                                   }

point_hostpital_floor_4_stair_up={'self_root_map_vid': 2,
                                   'self_floor': 4,
                                   'is_up_point_of_apartment': True,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': True,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 5,
                                   'agent_vid': -1,

                                   'float_x':-63.6,
                                   'float_z':65,
                                   'float_height':11,
                                       'vid': 24002,
                                   }

point_hostpital_floor_4_stair_1={'self_root_map_vid': 2,
                                   'self_floor': 4,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 5,
                                   'agent_vid': -1,

                                   'float_x':-64.939,
                                   'float_z':64.727,
                                   'float_height':11.5,
                                   'vid': 24003,
                                   }

point_hostpital_floor_4_stair_2={'self_root_map_vid': 2,
                                   'self_floor': 4,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 5,
                                   'agent_vid': -1,

                                   'float_x':-66.5,
                                   'float_z':64.727,
                                   'float_height':12,
                                   'vid': 24004,
                                   }

point_hostpital_floor_4_stair_3={'self_root_map_vid': 2,
                                   'self_floor': 4,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 5,
                                   'agent_vid': -1,

                                   'float_x':-67.77,
                                   'float_z':64.633,
                                   'float_height':12.5,
                                   'vid': 24005,
                                   }

point_hostpital_floor_4_stair_4={'self_root_map_vid': 2,
                                   'self_floor': 4,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 5,
                                   'agent_vid': -1,

                                   'float_x':-67.77,
                                   'float_z':66.789,
                                   'float_height':12.5,
                                   'vid': 24006,
                                   }

point_hostpital_floor_4_stair_5={'self_root_map_vid': 2,
                                   'self_floor': 4,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 5,
                                   'agent_vid': -1,

                                   'float_x':-66.31,
                                   'float_z':66.789,
                                   'float_height':13,
                                   'vid': 24007,
                                   }

point_hostpital_floor_4_stair_6={'self_root_map_vid': 2,
                                   'self_floor': 4,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 5,
                                   'agent_vid': -1,

                                   'float_x':-64.813,
                                   'float_z':66.789,
                                   'float_height':13.5,
                                   'vid': 24008,
                                   }

point_hostpital_floor_5_stair_down={'self_root_map_vid': 2,
                                   'self_floor': 5,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': True,

                                   'is_in_map': True,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 4,
                                   'agent_vid': -1,

                                   'float_x':-62.957,
                                   'float_z':66.789,
                                   'float_height':14.2  ,
                                   'vid': 25001,
                                   }

point_hostpital_floor_5_stair_up={'self_root_map_vid': 2,
                                   'self_floor': 5,
                                   'is_up_point_of_apartment': True,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': True,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 6,
                                   'agent_vid': -1,

                                   'float_x':-62.957,
                                   'float_z':65.677,
                                   'float_height':14.2,
                                   'vid': 25002,
                                   }

point_hostpital_floor_5_stair_1={'self_root_map_vid': 2,
                                   'self_floor': 5,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 6,
                                   'agent_vid': -1,

                                   'float_x':-64.257,
                                   'float_z':64.575,
                                   'float_height':14.7,
                                   'vid': 25003,
                                   }

point_hostpital_floor_5_stair_2={'self_root_map_vid': 2,
                                   'self_floor': 5,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 6,
                                   'agent_vid': -1,

                                   'float_x':-65.285,
                                   'float_z':64.575,
                                   'float_height':15.2,
                                   'vid': 25004,
                                   }

point_hostpital_floor_5_stair_3={'self_root_map_vid': 2,
                                   'self_floor': 5,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 6,
                                   'agent_vid': -1,

                                   'float_x':-67.056,
                                   'float_z':64.575,
                                   'float_height':15.81,
                                   'vid': 25005,
                                   }

point_hostpital_floor_5_stair_4={'self_root_map_vid': 2,
                                   'self_floor': 5,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 6,
                                   'agent_vid': -1,

                                   'float_x':-67.972,
                                   'float_z':66.328,
                                   'float_height':15.81,
                                   'vid': 25006,
                                   }

point_hostpital_floor_5_stair_5={'self_root_map_vid': 2,
                                   'self_floor': 5,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 6,
                                   'agent_vid': -1,

                                   'float_x':-66.473,
                                   'float_z':66.328,
                                   'float_height':16.429,
                                   'vid': 25007,
                                   }

point_hostpital_floor_5_stair_6={'self_root_map_vid': 2,
                                   'self_floor': 5,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 6,
                                   'agent_vid': -1,

                                   'float_x':-64.878,
                                   'float_z':66.328,
                                   'float_height':16.947,
                                   'vid': 25008,
                                   }


point_hostpital_floor_6_stair_down={'self_root_map_vid': 2,
                                   'self_floor': 5,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': False,

                                   'is_in_map': False,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 5,
                                   'agent_vid': -1,

                                   'float_x':-63.49,
                                   'float_z':66.54,
                                   'float_height':17.53,
                                   'vid': 26001,
                                   }

point_goverment_floor_1_down={'self_root_map_vid':7,
                        'self_floor':1,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':True,
                        'vid':71001,
                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':1,
                        'connected_floor':1,
                        'float_x':26.7,
                        'float_z':-272,
                        'float_height':1.1,
                        'agent_vid':-1}

point_goverment_floor_1_up={'self_root_map_vid':7,
                        'self_floor':1,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,
                        'vid':71002,
                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':2,
                        'float_x':24,
                        'float_z':-293.5,
                        'float_height':1.1,
                        'agent_vid':-1}

point_goverment_floor_1_stair_1={'self_root_map_vid':7,
                        'self_floor':1,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,
                        'vid':71003,
                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':2,
                        'float_x':24,
                        'float_z':-295.3,
                        'float_height':1.68,
                        'agent_vid':-1}

point_goverment_floor_1_stair_2={'self_root_map_vid':7,
                        'self_floor':1,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,
                        'vid':71004,
                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':2,
                        'float_x':24,
                        'float_z':-297,
                        'float_height':2.57,
                        'agent_vid':-1}

point_goverment_floor_1_stair_3={'self_root_map_vid':7,
                        'self_floor':1,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,
                        'vid':71005,
                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':2,

                        'float_x':24,
                        'float_z':-299,
                        'float_height':3.13,
                        'agent_vid':-1}

point_goverment_floor_1_stair_4={'self_root_map_vid':7,
                        'self_floor':1,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,
                        'vid':71006,
                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':2,
                        'float_x':25.5,
                        'float_z':298.99,
                        'float_height':3.13,
                        'agent_vid':-1}

point_goverment_floor_1_stair_5={'self_root_map_vid':7,
                        'self_floor':1,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,
                        'vid':71007,
                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':2,
                        'float_x':27,
                        'float_z':-297.2,
                        'float_height':3.374,
                        'agent_vid':-1}


point_goverment_floor_1_stair_6={'self_root_map_vid':7,
                        'self_floor':1,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':2,

                        'vid':71008,
                        'float_x':26.92,
                        'float_z':-295.434,
                        'float_height':3.944,
                        'agent_vid':-1}


point_goverment_floor_2_down={'self_root_map_vid':7,
                        'self_floor':2,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':True,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':1,

                        'vid': 72001,
                        'float_x':26.92,
                        'float_z':-293.598,
                        'float_height':4.44,
                        'agent_vid':-1}

point_goverment_floor_2_up={'self_root_map_vid':7,
                        'self_floor':2,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':3,

                        'vid':72002,
                        'float_x':25.108,
                        'float_z':-293.598,
                        'float_height':4.44,
                        'agent_vid':-1}


point_goverment_floor_2_stair_1={'self_root_map_vid':7,
                        'self_floor':2,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':3,

                        'vid':72003,
                        'float_x':23.8,
                        'float_z':-295.096,
                        'float_height':4.81,
                        'agent_vid':-1}


point_goverment_floor_2_stair_2={'self_root_map_vid':7,
                        'self_floor':2,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':3,

                        'vid':72004,
                        'float_x':23.8,
                        'float_z':-296.519,
                        'float_height':5.174,
                        'agent_vid':-1}

point_goverment_floor_2_stair_3={'self_root_map_vid':7,
                        'self_floor':2,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':3,

                        'vid':72005,
                        'float_x':23.8,
                        'float_z':-298.324,
                        'float_height':5.831,
                        'agent_vid':-1}


point_goverment_floor_2_stair_4={'self_root_map_vid':7,
                        'self_floor':2,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':3,

                        'vid':72006,
                        'float_x':25.598,
                        'float_z':-298.324,
                        'float_height':5.831,
                        'agent_vid':-1}

point_goverment_floor_2_stair_5={'self_root_map_vid':7,
                        'self_floor':2,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':3,

                        'vid':72007,
                        'float_x':26.603,
                        'float_z':-296.79,
                        'float_height':6.75,
                        'agent_vid':-1}

point_goverment_floor_2_stair_6={'self_root_map_vid':7,
                        'self_floor':2,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':3,

                        'vid':72008,
                        'float_x':26.603,
                        'float_z':-295.194,
                        'float_height':7.564,
                        'agent_vid':-1}

#第三层
point_goverment_floor_3_down={'self_root_map_vid':7,
                        'self_floor':3,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':True,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':2,

                        'vid': 73001,
                        'float_x':26.603,
                        'float_z':-293.429,
                        'float_height':7.721,
                        'agent_vid':-1}

point_goverment_floor_3_up={'self_root_map_vid':7,
                        'self_floor':3,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':4,

                        'vid':73002,
                        'float_x':29.96,
                        'float_z':-293.429,
                        'float_height':7.721,
                        'agent_vid':-1}
#3->4楼梯
point_goverment_floor_3_stair_1={'self_root_map_vid':7,
                        'self_floor':3,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':4,

                        'vid':73003,
                        'float_x':29.96,
                        'float_z':-295.132,
                        'float_height':8.192,
                        'agent_vid':-1}

point_goverment_floor_3_stair_2={'self_root_map_vid':7,
                        'self_floor':3,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':4,

                        'vid':73004,
                        'float_x':29.96,
                        'float_z':-297.023,
                        'float_height':8.694,
                        'agent_vid':-1}

point_goverment_floor_3_stair_3={'self_root_map_vid':7,
                        'self_floor':3,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':4,

                        'vid':73005,
                        'float_x':29.96,
                        'float_z':-298.941,
                        'float_height':9.125,
                        'agent_vid':-1}

point_goverment_floor_3_stair_4={'self_root_map_vid':7,
                        'self_floor':3,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':4,

                        'vid':73006,
                        'float_x':28.1,
                        'float_z':-298.941,
                        'float_height':9.125,
                        'agent_vid':-1}


point_goverment_floor_3_stair_5={'self_root_map_vid':7,
                        'self_floor':3,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':4,

                        'vid':73007,
                        'float_x':26.65,
                        'float_z':-297.35,
                        'float_height':9.697,
                        'agent_vid':-1}

point_goverment_floor_3_stair_6={'self_root_map_vid':7,
                        'self_floor':3,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':4,

                        'vid':73008,
                        'float_x':26.65,
                        'float_z':-295.955,
                        'float_height':10.343,
                        'agent_vid':-1}
#四楼
point_goverment_floor_3_down={'self_root_map_vid':7,
                        'self_floor':4,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':True,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':3,

                        'vid': 74001,
                        'float_x':26.65,
                        'float_z':-294.003,
                        'float_height':10.824,
                        'agent_vid':-1}

point_goverment_floor_3_up={'self_root_map_vid':7,
                        'self_floor':4,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':5,

                        'vid':74002,
                        'float_x':24.81,
                        'float_z':-294.003,
                        'float_height':10.824,
                        'agent_vid':-1}

point_goverment_floor_4_stair_1={'self_root_map_vid':7,
                        'self_floor':4,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':5,

                        'vid':74003,
                        'float_x':23.911,
                        'float_z':-295.8,
                        'float_height':11.59,
                        'agent_vid':-1}

point_goverment_floor_4_stair_2={'self_root_map_vid':7,
                        'self_floor':4,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':5,

                        'vid':74004,
                        'float_x':23.911,
                        'float_z':-297.946,
                        'float_height':12.307,
                        'agent_vid':-1}

point_goverment_floor_4_stair_3={'self_root_map_vid':7,
                        'self_floor':4,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':5,

                        'vid':74005,
                        'float_x':25.74,
                        'float_z':-299.025,
                        'float_height':12.307,
                        'agent_vid':-1}

point_goverment_floor_4_stair_4={'self_root_map_vid':7,
                        'self_floor':4,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':5,

                        'vid':74006,
                        'float_x':25.74,
                        'float_z':-299.025,
                        'float_height':12.307,
                        'agent_vid':-1}

point_goverment_floor_4_stair_5={'self_root_map_vid':7,
                        'self_floor':4,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':5,

                        'vid':74007,
                        'float_x':27.078,
                        'float_z':-297.311,
                        'float_height':13,
                        'agent_vid':-1}

point_goverment_floor_4_stair_6={'self_root_map_vid':7,
                        'self_floor':4,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':5,

                        'vid':74008,
                        'float_x':27.078,
                        'float_z':-295.426,
                        'float_height':13.608,
                        'agent_vid':-1}

#五楼
point_goverment_floor_5_down={'self_root_map_vid':7,
                        'self_floor':5,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':True,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':4,

                        'vid': 75001,
                        'float_x':27.078,
                        'float_z':-293.531,
                        'float_height':14.068,
                        'agent_vid':-1}

point_goverment_floor_5_up={'self_root_map_vid':7,
                        'self_floor':5,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':6,

                        'vid':75002,
                        'float_x':23.86,
                        'float_z':-293.531,
                        'float_height':14.068,
                        'agent_vid':-1}

point_goverment_floor_5_stair_1={'self_root_map_vid':7,
                        'self_floor':5,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':6,

                        'vid':75003,
                        'float_x':23.86,
                        'float_z':-295.13,
                        'float_height':14.644,
                        'agent_vid':-1}

point_goverment_floor_5_stair_2={'self_root_map_vid':7,
                        'self_floor':5,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':6,

                        'vid':75004,
                        'float_x':23.86,
                        'float_z':-296.95,
                        'float_height':15.43,
                        'agent_vid':-1}

point_goverment_floor_5_stair_3={'self_root_map_vid':7,
                        'self_floor':5,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':6,

                        'vid':75005,
                        'float_x':24.925,
                        'float_z':-298.776,
                        'float_height':15.739,
                        'agent_vid':-1}

point_goverment_floor_5_stair_4={'self_root_map_vid':7,
                        'self_floor':5,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':6,

                        'vid':75006,
                        'float_x':26.794,
                        'float_z':-297.69,
                        'float_height':16.294,
                        'agent_vid':-1}

point_goverment_floor_5_stair_5={'self_root_map_vid':7,
                        'self_floor':5,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':6,

                        'vid':75007,
                        'float_x':26.536,
                        'float_z':-296.006,
                        'float_height':16.716,
                        'agent_vid':-1}

point_goverment_floor_5_stair_6={'self_root_map_vid':7,
                        'self_floor':5,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':6,

                        'vid':75008,
                        'float_x':26.536,
                        'float_z':-296.006,
                        'float_height':16.716,
                        'agent_vid':-1}
#六楼
point_goverment_floor_6_down={'self_root_map_vid':7,
                        'self_floor':6,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':True,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':5,

                        'vid': 76001,
                        'float_x':26.536,
                        'float_z':-294.025,
                        'float_height':17.28,
                        'agent_vid':-1}

point_goverment_floor_6_up={'self_root_map_vid':7,
                        'self_floor':6,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':7,

                        'vid':76002,
                        'float_x':23.94,
                        'float_z':-294.025,
                        'float_height':17.28,
                        'agent_vid':-1}

point_goverment_floor_6_stair_1={'self_root_map_vid':7,
                        'self_floor':6,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':7,

                        'vid':76003,
                        'float_x':23.94,
                        'float_z':-295.8,
                        'float_height':18.069,
                        'agent_vid':-1}

point_goverment_floor_6_stair_2={'self_root_map_vid':7,
                        'self_floor':6,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':7,

                        'vid':76004,
                        'float_x':23.94,
                        'float_z':-297.54,
                        'float_height':18.85,
                        'agent_vid':-1}

point_goverment_floor_6_stair_3={'self_root_map_vid':7,
                        'self_floor':6,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':7,

                        'vid':76005,
                        'float_x':25.015,
                        'float_z':-299.254,
                        'float_height':19.093,
                        'agent_vid':-1}

point_goverment_floor_6_stair_4={'self_root_map_vid':7,
                        'self_floor':6,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':7,

                        'vid':76006,
                        'float_x':26.432,
                        'float_z':-297.71,
                        'float_height':19.093,
                        'agent_vid':-1}

point_goverment_floor_6_stair_5={'self_root_map_vid':7,
                        'self_floor':6,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':7,

                        'vid':76007,
                        'float_x':26.432,
                        'float_z':-295.866,
                        'float_height':19.53,
                        'agent_vid':-1}

point_goverment_floor_6_stair_6={'self_root_map_vid':7,
                        'self_floor':6,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':7,

                        'vid':76008,
                        'float_x':26.432,
                        'float_z':-294.008,
                        'float_height':20.287,
                        'agent_vid':-1}


point_goverment_floor_7_down={'self_root_map_vid':7,
                        'self_floor':7,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':True,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':6,

                        'vid': 77001,
                        'float_x': 26.432,
                        'float_z': -294.008,
                        'float_height': 20.287,
                        'agent_vid':-1}

point_goverment_floor_7_up={'self_root_map_vid':7,
                        'self_floor':7,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':8,

                        'vid':76002,
                        'float_x':23.94,
                        'float_z':-294.025,
                        'float_height':17.28,
                        'agent_vid':-1}

point_goverment_floor_7_stair_1={'self_root_map_vid':7,
                        'self_floor':7,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':8,

                        'vid':77003,
                        'float_x':29.99,
                        'float_z':-295.85,
                        'float_height':20.97,
                        'agent_vid':-1}

point_goverment_floor_7_stair_2={'self_root_map_vid':7,
                        'self_floor':7,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':8,

                        'vid':77004,
                        'float_x':29.99,
                        'float_z':-297.74,
                        'float_height':21.79,
                        'agent_vid':-1}

point_goverment_floor_7_stair_3={'self_root_map_vid':7,
                        'self_floor':7,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':8,

                        'vid':77005,
                        'float_x':28.13,
                        'float_z':-299.5,
                        'float_height':22.377,
                        'agent_vid':-1}

point_goverment_floor_7_stair_4={'self_root_map_vid':7,
                        'self_floor':7,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':8,

                        'vid':77006,
                        'float_x':26.871,
                        'float_z':-297.59,
                        'float_height':22.984,
                        'agent_vid':-1}

point_goverment_floor_7_stair_5={'self_root_map_vid':7,
                        'self_floor':7,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':8,

                        'vid':77007,
                        'float_x':26.871,
                        'float_z':-295.644,
                        'float_height':23.424,
                        'agent_vid':-1}

#八楼
point_goverment_floor_8_down={'self_root_map_vid':7,
                        'self_floor':8,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':True,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':7,

                        'vid': 78001,
                        'float_x': 26.871,
                        'float_z': -293.781,
                        'float_height': 24.054,
                        'agent_vid':-1}

point_goverment_floor_8_up={'self_root_map_vid':7,
                        'self_floor':8,
                        'is_up_point_of_apartment':True,
                        'is_down_point_of_apartment':False,

                        'is_in_map':True,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':9,

                        'vid':78002,
                        'float_x':24.23,
                        'float_z':-293.781,
                        'float_height':24.054,
                        'agent_vid':-1}

point_goverment_floor_8_stair_1={'self_root_map_vid':7,
                        'self_floor':8,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':9,

                        'vid':78003,
                        'float_x':24.23,
                        'float_z':-295.66,
                        'float_height':24.62,
                        'agent_vid':-1}


point_goverment_floor_8_stair_2={'self_root_map_vid':7,
                        'self_floor':8,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':9,

                        'vid':78004,
                        'float_x':24.23,
                        'float_z':-297.55,
                        'float_height':25.24,
                        'agent_vid':-1}

point_goverment_floor_8_stair_3={'self_root_map_vid':7,
                        'self_floor':8,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':9,

                        'vid':78005,
                        'float_x':26.02,
                        'float_z':-299.02,
                        'float_height':25.53,
                        'agent_vid':-1}

point_goverment_floor_8_stair_4={'self_root_map_vid':7,
                        'self_floor':8,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':9,

                        'vid':78006,
                        'float_x':27.1,
                        'float_z':-297.49,
                        'float_height':25.62,
                        'agent_vid':-1}

point_goverment_floor_8_stair_5={'self_root_map_vid':7,
                        'self_floor':8,
                        'is_up_point_of_apartment':False,
                        'is_down_point_of_apartment':False,

                        'is_in_map':False,
                        'is_junction':True,
                        'connected_root_map_vid':7,
                        'connected_floor':9,

                        'vid':78007,
                        'float_x':26.09,
                        'float_z':-295.507,
                        'float_height':25.62,
                        'agent_vid':-1}



from enum import  Enum

class PointType(Enum):
    IN_MAP=1
    IN_STAIRS=2
