######################################
# Create date : 2020-12-28 16:22
# Modified date : 2020-12-28 16:22
# Author : zpp
# Describe: None
######################################
import numpy as np


# bool
SHOW_HEAT_MAP = False



# 
Red_Team_Num = 30
Blue_Team_Num = 30

Map_Length = 70
Map_Width = 60

Capture_Target_worker_num = 1
Obstacle_Target_worker_num = 1
Enemy_Target_worker_num = 2

Max_Distance = (Map_Length ** 2 + Map_Width ** 2) ** 0.5     # meter

# 
# Hospital_pos =[32, 14]   # 医院坐标
# Hospital_vid = 21999


# Big Influence Map Initialize
Big_Influence_Map = np.zeros((2 * Map_Width, 2 * Map_Length))
for i in range(2*Map_Width):
    for j in range(2*Map_Length):
        Big_Influence_Map[i, j] = 1. / 2 ** (abs(i - Map_Width + 1) + abs(j - Map_Length + 1))
        if Big_Influence_Map[i, j] < 1e-6:
            Big_Influence_Map[i, j] = 0.

# for test Big Map
# print(Big_Influence_Map[0, 0], Big_Influence_Map[Map_Width - 1, Map_Length - 1])
# print(Big_Influence_Map)
print("Big Influence Map Ready !")



# 系数

## calculate target val
Capture_Tension_coef = 0.5
Capture_Vulnerablity_coef = 0.5

Obstacle_Tension_coef = 0.5
Obstacle_Vulnerablity_coef = 0.5

Attack_Tension_coef = 0.5
Attack_Vulnerablity_coef = 0.5



# result
target_assign_result = {}


# 夺控点与可夺控方的对应关系    
target_relationship = {'air_detect_point':['air_detect_unit', 'air_fire_unit'],\
                        'air_fire_point':['air_fire_unit'],\
                        'air_defense_point':['air_defence_unit'],\
                        'ind_detect_point':['ind_detect_unit', 'ind_fire_unit'],\
                        'ind_fire_point':['ind_fire_unit'],\
                        'outd_detect_point':[ 'outd_detect_unit', 'outd_fire_unit'],\
                        'outd_fire_point':['air_fire_unit', 'outd_fire_unit','out_air_floor_unit'],\
                       'out_air_defense_point':['out_air_defence_unit','out_air_floor_unit'],\
                       'all_type':['outd_detect_unit','outd_fire_unit','air_detect_unit',\
                        'air_fire_unit','ind_detect_unit','ind_fire_unit','air_defence_unit','engineer','out_air_defence_unit','out_air_floor_unit'],}

enemy_pos_relationship = {'indoor_pos':['ind_fire_unit'],\
                        'outdoor_pos':['air_fire_unit', 'outd_fire_unit','air_detect_unit','out_air_floor_unit'],\
                        'air_pos':['air_defence_unit', 'air_fire_unit','out_air_defence_unit','out_air_floor_unit']}


