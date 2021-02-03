from .models import *
from .utils import *
from .destination_transformer import *

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

apartment_hospital_floor_1={
    'floor':1,
    'file_name':'1.png',
    'height_ceil':1.6,
    'height_floor':0.6,
    'height_upper':4.2,
}

apartment_hospital_floor_2={
    'floor':2,
    'file_name':'2.png',
    'height_ceil':5.3,
    'height_floor':4.2,
    'height_upper':7.4,
}

apartment_hospital_floor_3={
    'floor':3,
    'file_name':'3.png',
    'height_ceil':8.6,
    'height_floor':7.4,
    'height_upper':10.8,
}

apartment_hospital_floor_4={
    'floor':4,
    'file_name':'4.png',
    'height_ceil':11.9,
    'height_floor':10.8,
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

                                   'float_x': -66.186,
                                   'float_z': 64.8,
                                   'float_height': 2.5,
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
                                   'float_height': 2.8,
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
                                   'float_height': 3.2,
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
                                   'float_height':4.7,
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
                                   'float_height':4.7,
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

                                   'float_x': -64.048,
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

                                   'float_x': -62.471,
                                   'float_z': 66.698,
                                   'float_height':7.7,
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
                                   'float_z':64.906,
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

                                   'float_x':-68.2179 ,
                                   'float_z': 64.7268,
                                   'float_height':9.245271,
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

                                   'float_x':-66.876,
                                   'float_z': 66.462,
                                   'float_height':10.02,
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

                                   'float_x':-65.026,
                                   'float_z': 66.462,
                                   'float_height':10.578,
                                   'vid': 23007,
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
                                   'float_z':66.681,
                                   'float_height':11.6,
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
                                   'float_z':64.876,
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

                                   'float_x':-66.815,
                                   'float_z':66.789,
                                   'float_height':13.401,
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

                                   'float_x':-64.895,
                                   'float_z':66.789,
                                   'float_height':13.5,
                                   'vid': 24007,
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

                                   'float_x':-62.527,
                                   'float_z':65.149,
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

                                   'float_x':-64.376,
                                   'float_z':64.575,
                                   'float_height':14.875,
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

                                   'float_x':-66.177,
                                   'float_z':64.575,
                                   'float_height':15.81,
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

                                   'float_x':-67.972,
                                   'float_z':64.854,
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

                                   'float_x':-66.473,
                                   'float_z':66.328,
                                   'float_height':16.429,
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

                                   'float_x':-64.878,
                                   'float_z':66.328,
                                   'float_height':16.947,
                                   'vid': 25007,
                                   }


point_hostpital_floor_6_stair_down={'self_root_map_vid': 2,
                                   'self_floor': 6,
                                   'is_up_point_of_apartment': False,
                                   'is_down_point_of_apartment': True,

                                   'is_in_map': True,
                                   'is_junction': True,
                                   'connected_root_map_vid': 2,
                                   'connected_floor': 5,
                                   'agent_vid': -1,

                                   'float_x':-63.098,
                                   'float_z':66.54,
                                   'float_height':17.69,
                                   'vid': 26001,
                                   }

def initializeHospitalMap():
    addRootMap(**hospital_map_params)

    hospital = RootMap.objects.get(vid=2)
    addApartment(root_map=hospital, **apartment_hospital_floor_1)
    addApartment(root_map=hospital, **apartment_hospital_floor_2)
    addApartment(root_map=hospital, **apartment_hospital_floor_3)
    addApartment(root_map=hospital, **apartment_hospital_floor_4)
    addApartment(root_map=hospital, **apartment_hospital_floor_5)
    addApartment(root_map=hospital, **apartment_hospital_floor_6)

    p_global_to_hospital = addStaticPoint3D(**point_global_to_hospital_2)
    #####Hospital
    # 一楼
    p_hospital_to_global = addStaticPoint3D(**point_hostpital_floor_1_down)
    p_hospital_1_up = addStaticPoint3D(**point_hostpital_floor_1_up)
    addStaticPoint3D(**point_hostpital_floor_1_stair_1)
    addStaticPoint3D(**point_hostpital_floor_1_stair_2)
    addStaticPoint3D(**point_hostpital_floor_1_stair_3)
    addStaticPoint3D(**point_hostpital_floor_1_stair_4)
    addStaticPoint3D(**point_hostpital_floor_1_stair_5)
    addStaticPoint3D(**point_hostpital_floor_1_stair_6)

    # 二楼
    p_hospital_2_down = addStaticPoint3D(**point_hostpital_floor_2_stair_down)
    p_hospital_2_up = addStaticPoint3D(**point_hostpital_floor_2_stair_up)
    addStaticPoint3D(**point_hostpital_floor_2_stair_1)
    addStaticPoint3D(**point_hostpital_floor_2_stair_2)
    addStaticPoint3D(**point_hostpital_floor_2_stair_3)
    addStaticPoint3D(**point_hostpital_floor_2_stair_4)
    addStaticPoint3D(**point_hostpital_floor_2_stair_5)
    addStaticPoint3D(**point_hostpital_floor_2_stair_6)

    # 三楼
    p_hospital_3_down = addStaticPoint3D(**point_hostpital_floor_3_stair_down)
    p_hospital_3_up = addStaticPoint3D(**point_hostpital_floor_3_stair_up)
    addStaticPoint3D(**point_hostpital_floor_3_stair_1)
    addStaticPoint3D(**point_hostpital_floor_3_stair_2)
    addStaticPoint3D(**point_hostpital_floor_3_stair_3)
    addStaticPoint3D(**point_hostpital_floor_3_stair_4)
    addStaticPoint3D(**point_hostpital_floor_3_stair_5)


    # 四楼
    p_hospital_4_down = addStaticPoint3D(**point_hostpital_floor_4_stair_down)
    p_hospital_4_up = addStaticPoint3D(**point_hostpital_floor_4_stair_up)
    addStaticPoint3D(**point_hostpital_floor_4_stair_1)
    addStaticPoint3D(**point_hostpital_floor_4_stair_2)
    addStaticPoint3D(**point_hostpital_floor_4_stair_3)
    addStaticPoint3D(**point_hostpital_floor_4_stair_4)
    addStaticPoint3D(**point_hostpital_floor_4_stair_5)
    # addStaticPoint3D(**point_hostpital_floor_4_stair_6)

    # 五楼
    p_hospital_5_down = addStaticPoint3D(**point_hostpital_floor_5_stair_down)
    p_hospital_5_up = addStaticPoint3D(**point_hostpital_floor_5_stair_up)
    addStaticPoint3D(**point_hostpital_floor_5_stair_1)
    addStaticPoint3D(**point_hostpital_floor_5_stair_2)
    addStaticPoint3D(**point_hostpital_floor_5_stair_3)
    addStaticPoint3D(**point_hostpital_floor_5_stair_4)
    addStaticPoint3D(**point_hostpital_floor_5_stair_5)
    # addStaticPoint3D(**point_hostpital_floor_5_stair_6)

    # 六楼
    p_hospital_6_down = addStaticPoint3D(**point_hostpital_floor_6_stair_down)


    ##Global<- Connection ->Hospital
    connectTwoPoints(p_global_to_hospital, p_hospital_to_global)
    ##Hospital_1<- Connection ->Hospital_2
    connect_apartment_floor(p_hospital_1_up.self_apartment, p_hospital_2_down)
    ##Hospital_2<- Connection ->Hospital_3
    connect_apartment_floor(p_hospital_2_up.self_apartment, p_hospital_3_down)
    ##Hospital_3<- Connection ->Hospital_4
    connect_apartment_floor(p_hospital_3_up.self_apartment, p_hospital_4_down)
    ##Hospital_4<- Connection ->Hospital_5
    connect_apartment_floor(p_hospital_4_up.self_apartment, p_hospital_5_down)
    ##Hospital_5<- Connection ->Hospital_6
    connect_apartment_floor(p_hospital_5_up.self_apartment, p_hospital_6_down)

    ##Hospital
