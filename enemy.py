import pygame
import os
from laser import Laser
from ship import Ship

WIDTH, HEIGHT = 1000, 700

# ENEMY SHIP 1 / ENEMY SHIP EXPLOSION 1
ENEMY_SHIP_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_A", "Enemy_ship1.png"))
EXPLOSION1_1 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship1_Explosion", "Ship1_Explosion_001.png"))
EXPLOSION1_2 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship1_Explosion", "Ship1_Explosion_003.png"))
EXPLOSION1_3 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship1_Explosion", "Ship1_Explosion_008.png"))
EXPLOSION1_5 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship1_Explosion", "Ship1_Explosion_012.png"))
EXPLOSION1_4 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship1_Explosion", "Ship1_Explosion_009.png"))
EXPLOSION1_6 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship1_Explosion", "Ship1_Explosion_013.png"))
EXPLOSION1_7 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship1_Explosion", "Ship1_Explosion_014.png"))
EXPLOSION1_8 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship1_Explosion", "Ship1_Explosion_017.png"))
EXPLOSION1_9 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship1_Explosion", "Ship1_Explosion_019.png"))
EXPLOSION1_10 = pygame.image.load(
    os.path.join("Images/Enemy/Planet_A/Ship_Explosion/Ship1_Explosion", "Ship1_Explosion_020.png"))
# ENEMY 1 LASER / ENEMY 1 LASER EXPLOSION
ENEMY_1_1_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot1", "shot1_1.png"))
ENEMY_1_2_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot1", "shot1_2.png"))
ENEMY_1_3_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot1", "shot1_3.png"))
ENEMY_1_4_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot1", "shot1_4.png"))
ENEMY_1_5_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot1", "shot1_asset.png"))
ENEMY_1_1_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot1", "shot1_exp0.png"))
ENEMY_1_2_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot1", "shot1_exp1.png"))
ENEMY_1_3_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot1", "shot1_exp2.png"))
ENEMY_1_4_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot1", "shot1_exp3.png"))
ENEMY_1_5_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot1", "shot1_exp4.png"))
# ENEMY SHIP 2 / ENEMY SHIP EXPLOSION 2
ENEMY_SHIP_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_A", "Enemy_ship2.png"))
EXPLOSION2_1 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship2_Explosion", "Ship2_Explosion_000.png"))
EXPLOSION2_2 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship2_Explosion", "Ship2_Explosion_000.png"))
EXPLOSION2_3 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship2_Explosion", "Ship2_Explosion_000.png"))
EXPLOSION2_4 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship2_Explosion", "Ship2_Explosion_000.png"))
EXPLOSION2_5 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship2_Explosion", "Ship2_Explosion_000.png"))
EXPLOSION2_6 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship2_Explosion", "Ship2_Explosion_000.png"))
EXPLOSION2_7 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship2_Explosion", "Ship2_Explosion_000.png"))
EXPLOSION2_8 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship2_Explosion", "Ship2_Explosion_000.png"))
EXPLOSION2_9 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship2_Explosion", "Ship2_Explosion_000.png"))
EXPLOSION2_10 = pygame.image.load(
    os.path.join("Images/Enemy/Planet_A/Ship_Explosion/Ship2_Explosion", "Ship2_Explosion_000.png"))
EXPLOSION2_11 = pygame.image.load(
    os.path.join("Images/Enemy/Planet_A/Ship_Explosion/Ship2_Explosion", "Ship2_Explosion_000.png"))
# ENEMY 2 LASER / ENEMY 2 LASER EXPLOSION
ENEMY_2_1_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot2", "shot2_1.png"))
ENEMY_2_2_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot2", "shot2_2.png"))
ENEMY_2_3_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot2", "shot2_3.png"))
ENEMY_2_4_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot2", "shot2_4.png"))
ENEMY_2_5_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot2", "shot2_5.png"))
ENEMY_2_6_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot2", "shot2_6.png"))
ENEMY_2_7_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot2", "shot2_asset.png"))
ENEMY_2_1_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot2", "shot2_exp1.png"))
ENEMY_2_2_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot2", "shot2_exp2.png"))
ENEMY_2_3_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot2", "shot2_exp3.png"))
ENEMY_2_4_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot2", "shot2_exp4.png"))
ENEMY_2_5_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot2", "shot2_exp5.png"))
# ENEMY SHIP 3 / ENEMY SHIP EXPLOSION 3
ENEMY_SHIP_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_A", "Enemy_ship3.png"))
EXPLOSION3_1 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship3_Explosion", "Ship3_Explosion_004.png"))
EXPLOSION3_2 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship3_Explosion", "Ship3_Explosion_005.png"))
EXPLOSION3_3 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship3_Explosion", "Ship3_Explosion_007.png"))
EXPLOSION3_4 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship3_Explosion", "Ship3_Explosion_009.png"))
EXPLOSION3_5 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship3_Explosion", "Ship3_Explosion_012.png"))
EXPLOSION3_6 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship3_Explosion", "Ship3_Explosion_013.png"))
EXPLOSION3_7 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship3_Explosion", "Ship3_Explosion_015.png"))
EXPLOSION3_8 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship3_Explosion", "Ship3_Explosion_018.png"))
EXPLOSION3_9 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship3_Explosion", "Ship3_Explosion_019.png"))
EXPLOSION3_10 = pygame.image.load(
    os.path.join("Images/Enemy/Planet_A/Ship_Explosion/Ship3_Explosion", "Ship3_Explosion_021.png"))
# ENEMY 3 LASER / ENEMY 3 LASER EXPLOSION
ENEMY_3_1_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot3", "shot3_1.png"))
ENEMY_3_2_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot3", "shot3_2.png"))
ENEMY_3_3_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot3", "shot3_3.png"))
ENEMY_3_4_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot3", "shot3_asset.png"))
ENEMY_3_1_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot3", "shot3_exp1.png"))
ENEMY_3_2_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot3", "shot3_exp2.png"))
ENEMY_3_3_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot3", "shot3_exp3.png"))
ENEMY_3_4_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot3", "shot3_exp4.png"))

# ENEMY SHIP 4 / ENEMY SHIP EXPLOSION 4
ENEMY_SHIP_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_A", "Enemy_ship4.png"))
EXPLOSION4_1 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship4_Explosion", "Ship4_Explosion_000.png"))
EXPLOSION4_2 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship4_Explosion", "Ship4_Explosion_003.png"))
EXPLOSION4_3 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship4_Explosion", "Ship4_Explosion_005.png"))
EXPLOSION4_4 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship4_Explosion", "Ship4_Explosion_007.png"))
EXPLOSION4_5 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship4_Explosion", "Ship4_Explosion_008.png"))
EXPLOSION4_6 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship4_Explosion", "Ship4_Explosion_012.png"))
EXPLOSION4_7 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship4_Explosion", "Ship4_Explosion_013.png"))
EXPLOSION4_8 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship4_Explosion", "Ship4_Explosion_015.png"))
EXPLOSION4_9 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship4_Explosion", "Ship4_Explosion_018.png"))
EXPLOSION4_10 = pygame.image.load(
    os.path.join("Images/Enemy/Planet_A/Ship_Explosion/Ship4_Explosion", "Ship4_Explosion_019.png"))
# ENEMY 4 LASER / ENEMY 4 LASER EXPLOSION
ENEMY_4_1_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot4", "shot4_1.png"))
ENEMY_4_2_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot4", "shot4_2.png"))
ENEMY_4_3_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot4", "shot4_3.png"))
ENEMY_4_4_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot4", "shot4_4.png"))
ENEMY_4_5_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot4", "shot4_5.png"))
ENEMY_4_6_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot4", "shot4_asset.png"))
ENEMY_4_1_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot4", "shot4_exp1.png"))
ENEMY_4_2_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot4", "shot4_exp2.png"))
ENEMY_4_3_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot4", "shot4_exp3.png"))
ENEMY_4_4_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot4", "shot4_exp4.png"))
ENEMY_4_5_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot4", "shot4_exp5.png"))
ENEMY_4_6_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot4", "shot4_exp6.png"))
ENEMY_4_7_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot4", "shot4_exp7.png"))
ENEMY_4_8_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot4", "shot4_exp8.png"))

# ENEMY 5 SHIP / ENEMY SHIP EXPLOSION 5
ENEMY_SHIP_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_A", "Enemy_ship5.png"))
EXPLOSION5_1 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship5_Explosion", "Ship5_Explosion_001.png"))
EXPLOSION5_2 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship5_Explosion", "Ship5_Explosion_003.png"))
EXPLOSION5_3 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship5_Explosion", "Ship5_Explosion_006.png"))
EXPLOSION5_4 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship5_Explosion", "Ship5_Explosion_007.png"))
EXPLOSION5_5 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship5_Explosion", "Ship5_Explosion_008.png"))
EXPLOSION5_6 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship5_Explosion", "Ship5_Explosion_011.png"))
EXPLOSION5_7 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship5_Explosion", "Ship5_Explosion_013.png"))
EXPLOSION5_8 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship5_Explosion", "Ship5_Explosion_014.png"))
EXPLOSION5_9 = pygame.image.load(os.path.join
                                 ("Images/Enemy/Planet_A/Ship_Explosion/Ship5_Explosion", "Ship5_Explosion_017.png"))
EXPLOSION5_10 = pygame.image.load(
    os.path.join("Images/Enemy/Planet_A/Ship_Explosion/Ship5_Explosion", "Ship5_Explosion_019.png"))
# ENEMY 5 LASER / ENEMY 5 LASER EXPLOSION
ENEMY_5_1_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot5", "shot5_1.png"))
ENEMY_5_2_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot5", "shot5_2.png"))
ENEMY_5_3_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot5", "shot5_3.png"))
ENEMY_5_4_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot5", "shot5_4.png"))
ENEMY_5_5_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot5", "shot5_5.png"))
ENEMY_5_6_LASER = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot5", "shot5_asset.png"))
ENEMY_5_1_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot5", "shot5_exp1.png"))
ENEMY_5_2_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot5", "shot5_exp2.png"))
ENEMY_5_3_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot5", "shot5_exp3.png"))
ENEMY_5_4_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot5", "shot5_exp4.png"))
ENEMY_5_5_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot5", "shot5_exp5.png"))
ENEMY_5_6_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot5", "shot5_exp6.png"))
ENEMY_5_7_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot5", "shot5_exp7.png"))
ENEMY_5_8_LASER_EXP = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot5", "shot5_exp8.png"))

# PLANET A ENEMY SHIPS ------------------------

# PLANET B ENEMY SHIPS ------------------------


# ENEMY 1
ENEMY_1_SHIP = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Ship1", "ship1.png"))
ENEMY_1_EXPLOSION_1 = pygame.image.load(os.path.join(
    "Images/Enemy/Planet_B/Ships/Explotions/Explotion1", "Explotion1_1.png"))
ENEMY_1_EXPLOSION_2 = pygame.image.load(os.path.join(
    "Images/Enemy/Planet_B/Ships/Explotions/Explotion1", "Explotion1_2.png"))
ENEMY_1_EXPLOSION_3 = pygame.image.load(os.path.join(
    "Images/Enemy/Planet_B/Ships/Explotions/Explotion1", "Explotion1_3.png"))
ENEMY_1_EXPLOSION_4 = pygame.image.load(os.path.join(
    "Images/Enemy/Planet_B/Ships/Explotions/Explotion1", "Explotion1_4.png"))
ENEMY_1_EXPLOSION_5 = pygame.image.load(os.path.join(
    "Images/Enemy/Planet_B/Ships/Explotions/Explotion1", "Explotion1_5.png"))
ENEMY_1_EXPLOSION_6 = pygame.image.load(os.path.join(
    "Images/Enemy/Planet_B/Ships/Explotions/Explotion1", "Explotion1_6.png"))
ENEMY_1_EXPLOSION_7 = pygame.image.load(os.path.join(
    "Images/Enemy/Planet_B/Ships/Explotions/Explotion1", "Explotion1_7.png"))
ENEMY_1_EXPLOSION_8 = pygame.image.load(os.path.join(
    "Images/Enemy/Planet_B/Ships/Explotions/Explotion1", "Explotion1_8.png"))
ENEMY_1_EXPLOSION_9 = pygame.image.load(os.path.join(
    "Images/Enemy/Planet_B/Ships/Explotions/Explotion1", "Explotion1_9.png"))
ENEMY_1_EXPLOSION_10 = pygame.image.load(os.path.join(
    "Images/Enemy/Planet_B/Ships/Explotions/Explotion1", "Explotion1_10.png"))

# ENEMY 1 LASERS
ENEMY_1_LASER_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot1", "shot1_1.png"))
ENEMY_1_LASER_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot1", "shot1_2.png"))
ENEMY_1_LASER_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot1", "shot1_3.png"))
ENEMY_1_LASER_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot1", "shot1_4.png"))
ENEMY_1_LASER_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot1", "shot1_5.png"))
ENEMY_1_LASER_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot1", "shot1_6.png"))
ENEMY_1_LASER_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot1", "shot1_asset.png"))
ENEMY_1_LASER_EXP_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot1", "shot1_exp_1.png"))
ENEMY_1_LASER_EXP_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot1", "shot1_exp_2.png"))
ENEMY_1_LASER_EXP_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot1", "shot1_exp_3.png"))
ENEMY_1_LASER_EXP_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot1", "shot1_exp_4.png"))
ENEMY_1_LASER_EXP_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot1", "shot1_exp_5.png"))

# ENEMY 2
ENEMY_2_SHIP = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Ship2", "ship2.png"))
# ENEMY 2 LASERS
ENEMY_2_LASER_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot2", "shot2_1.png"))
ENEMY_2_LASER_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot2", "shot2_2.png"))
ENEMY_2_LASER_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot2", "shot2_3.png"))
ENEMY_2_LASER_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot2", "shot2_4.png"))
ENEMY_2_LASER_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot2", "shot2_5.png"))
ENEMY_2_LASER_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot2", "shot2_asset.png"))
ENEMY_2_LASER_EXP_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot2", "shot2_exp_1.png"))
ENEMY_2_LASER_EXP_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot2", "shot2_exp_2.png"))
ENEMY_2_LASER_EXP_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot2", "shot2_exp_3.png"))
ENEMY_2_LASER_EXP_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot2", "shot2_exp_4.png"))
ENEMY_2_LASER_EXP_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot2", "shot2_exp_5.png"))
ENEMY_2_LASER_EXP_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot2", "shot4_exp_6.png"))
ENEMY_2_LASER_EXP_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot2", "shot4_exp_7.png"))
# ENEMY 3
ENEMY_3_SHIP = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Ship3", "ship3.png"))
# ENEMY 3 LASERS
ENEMY_3_LASER_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot3", "shot3_1.png"))
ENEMY_3_LASER_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot3", "shot3_2.png"))
ENEMY_3_LASER_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot3", "shot3_3.png"))
ENEMY_3_LASER_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot3", "shot3_4.png"))
ENEMY_3_LASER_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot3", "shot3_5.png"))
ENEMY_3_LASER_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot3", "shot3_6.png"))
ENEMY_3_LASER_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot3", "shot3_asset.png"))
ENEMY_3_LASER_EXP_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot3", "shot3_exp_1.png"))
ENEMY_3_LASER_EXP_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot3", "shot3_exp_2.png"))
ENEMY_3_LASER_EXP_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot3", "shot3_exp_3.png"))
ENEMY_3_LASER_EXP_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot3", "shot3_exp_4.png"))
ENEMY_3_LASER_EXP_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot3", "shot3_exp_5.png"))
ENEMY_3_LASER_EXP_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot3", "shot3_exp_6.png"))
ENEMY_3_LASER_EXP_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot3", "shot3_exp_7.png"))
# ENEMY 4
ENEMY_4_SHIP = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Ship4", "ship4.png"))
ENEMY_4_LASER_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot4", "shot4_1.png"))
ENEMY_4_LASER_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot4", "shot4_2.png"))
ENEMY_4_LASER_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot4", "shot4_3.png"))
ENEMY_4_LASER_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot4", "shot4_4.png"))
ENEMY_4_LASER_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot4", "shot4_5.png"))
ENEMY_4_LASER_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot4", "shot4_6.png"))
ENEMY_4_LASER_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot4", "shot4_7.png"))
ENEMY_4_LASER_8 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot4", "shot4_asset.png"))
ENEMY_4_LASER_EXP_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot4", "shot4_exp_1.png"))
ENEMY_4_LASER_EXP_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot4", "shot4_exp_2.png"))
ENEMY_4_LASER_EXP_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot4", "shot4_exp_3.png"))
ENEMY_4_LASER_EXP_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot4", "shot4_exp_4.png"))
ENEMY_4_LASER_EXP_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot4", "shot4_exp_5.png"))
ENEMY_4_LASER_EXP_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot4", "shot4_exp_6.png"))

# ENEMY 5 SHIP/EXPLOTION
ENEMY_5_SHIP = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Ship5", "ship5.png"))
ENEMY_5_SHIP_EXP_1 = pygame.image.load(os.path.join
                                       ("Images/Enemy/Planet_B/Ships/Explotions/Explotion2", "Explotion2_1.png"))
ENEMY_5_SHIP_EXP_2 = pygame.image.load(os.path.join
                                       ("Images/Enemy/Planet_B/Ships/Explotions/Explotion2", "Explotion2_2.png"))
ENEMY_5_SHIP_EXP_3 = pygame.image.load(os.path.join
                                       ("Images/Enemy/Planet_B/Ships/Explotions/Explotion2", "Explotion2_3.png"))
ENEMY_5_SHIP_EXP_4 = pygame.image.load(os.path.join
                                       ("Images/Enemy/Planet_B/Ships/Explotions/Explotion2", "Explotion2_4.png"))
ENEMY_5_SHIP_EXP_5 = pygame.image.load(os.path.join
                                       ("Images/Enemy/Planet_B/Ships/Explotions/Explotion2", "Explotion2_5.png"))
ENEMY_5_SHIP_EXP_6 = pygame.image.load(os.path.join
                                       ("Images/Enemy/Planet_B/Ships/Explotions/Explotion2", "Explotion2_6.png"))
ENEMY_5_SHIP_EXP_7 = pygame.image.load(os.path.join
                                       ("Images/Enemy/Planet_B/Ships/Explotions/Explotion2", "Explotion2_7.png"))
ENEMY_5_SHIP_EXP_8 = pygame.image.load(os.path.join
                                       ("Images/Enemy/Planet_B/Ships/Explotions/Explotion2", "Explotion2_8.png"))
ENEMY_5_SHIP_EXP_9 = pygame.image.load(os.path.join
                                       ("Images/Enemy/Planet_B/Ships/Explotions/Explotion2", "Explotion2_9.png"))
ENEMY_5_SHIP_EXP_10 = pygame.image.load(os.path.join
                                        ("Images/Enemy/Planet_B/Ships/Explotions/Explotion2", "Explotion2_10.png"))
ENEMY_5_LASER_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot5", "shot5_1.png"))
ENEMY_5_LASER_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot5", "shot5_2.png"))
ENEMY_5_LASER_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot5", "shot5_3.png"))
ENEMY_5_LASER_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot5", "shot5_4.png"))
ENEMY_5_LASER_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot5", "shot5_5.png"))
ENEMY_5_LASER_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot5", "shot5_6.png"))
ENEMY_5_LASER_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot5", "shot5_7.png"))
ENEMY_5_LASER_8 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot5", "shot5_asset.png"))
ENEMY_5_LASER_EXP_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot5", "shot5_exp_1.png"))
ENEMY_5_LASER_EXP_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot5", "shot5_exp_2.png"))
ENEMY_5_LASER_EXP_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot5", "shot5_exp_3.png"))
ENEMY_5_LASER_EXP_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot5", "shot5_exp_4.png"))
ENEMY_5_LASER_EXP_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot5", "shot5_exp_5.png"))
ENEMY_5_LASER_EXP_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot5", "shot5_exp_6.png"))
ENEMY_5_LASER_EXP_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot5", "shot5_exp_7.png"))

# ENEMY 6 SHIP/EXPLOTION
ENEMY_6_SHIP = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Ship6", "ship6.png"))
ENEMY_6_SHIP_EXP_1 = pygame.image.load(os.path.join
                                       ("Images/Enemy/Planet_B/Ships/Explotions/Explotion3", "Explotion3_1.png"))
ENEMY_6_SHIP_EXP_2 = pygame.image.load(os.path.join
                                       ("Images/Enemy/Planet_B/Ships/Explotions/Explotion3", "Explotion3_2.png"))
ENEMY_6_SHIP_EXP_3 = pygame.image.load(os.path.join
                                       ("Images/Enemy/Planet_B/Ships/Explotions/Explotion3", "Explotion3_3.png"))
ENEMY_6_SHIP_EXP_4 = pygame.image.load(os.path.join
                                       ("Images/Enemy/Planet_B/Ships/Explotions/Explotion3", "Explotion3_4.png"))
ENEMY_6_SHIP_EXP_5 = pygame.image.load(os.path.join
                                       ("Images/Enemy/Planet_B/Ships/Explotions/Explotion3", "Explotion3_5.png"))
ENEMY_6_SHIP_EXP_6 = pygame.image.load(os.path.join
                                       ("Images/Enemy/Planet_B/Ships/Explotions/Explotion3", "Explotion3_6.png"))
ENEMY_6_SHIP_EXP_7 = pygame.image.load(os.path.join
                                       ("Images/Enemy/Planet_B/Ships/Explotions/Explotion3", "Explotion3_7.png"))
ENEMY_6_SHIP_EXP_8 = pygame.image.load(os.path.join
                                       ("Images/Enemy/Planet_B/Ships/Explotions/Explotion3", "Explotion3_8.png"))
ENEMY_6_SHIP_EXP_9 = pygame.image.load(os.path.join
                                       ("Images/Enemy/Planet_B/Ships/Explotions/Explotion3", "Explotion3_9.png"))
ENEMY_6_SHIP_EXP_10 = pygame.image.load(os.path.join
                                        ("Images/Enemy/Planet_B/Ships/Explotions/Explotion3", "Explotion3_10.png"))

# ENEMY 6 LASERS
ENEMY_6_LASER_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot6", "shot6_1.png"))
ENEMY_6_LASER_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot6", "shot6_2.png"))
ENEMY_6_LASER_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot6", "shot6_3.png"))
ENEMY_6_LASER_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot6", "shot6_4.png"))
ENEMY_6_LASER_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot6", "shot6_5.png"))
ENEMY_6_LASER_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot6", "shot6_6.png"))
ENEMY_6_LASER_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot6", "shot6_7.png"))
ENEMY_6_LASER_8 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot6", "shot6_8.png"))
ENEMY_6_LASER_9 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot6", "shot6_assett.png"))
ENEMY_6_LASER_EXP_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot6", "shot6_exp1.png"))
ENEMY_6_LASER_EXP_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot6", "shot6_exp2.png"))
ENEMY_6_LASER_EXP_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot6", "shot6_exp3.png"))
ENEMY_6_LASER_EXP_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot6", "shot6_exp4.png"))
ENEMY_6_LASER_EXP_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot6", "shot6_exp5.png"))
ENEMY_6_LASER_EXP_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot6", "shot6_exp6.png"))
ENEMY_6_LASER_EXP_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot6", "shot6_exp7.png"))
ENEMY_6_LASER_EXP_8 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Ships/Shots/Shot6", "shot6_exp8.png"))


class Enemy(Ship):
    ENEMY_MAP = {
        "enemy_1": (
            [ENEMY_SHIP_1, EXPLOSION1_1, EXPLOSION1_2, EXPLOSION1_3, EXPLOSION1_4, EXPLOSION1_5, EXPLOSION1_6,
             EXPLOSION1_7, EXPLOSION1_8, EXPLOSION1_9, EXPLOSION1_10],  # ENEMY 1 SHIP/ EXPLOSION
            [
                ENEMY_1_1_LASER_EXP, ENEMY_1_2_LASER_EXP, ENEMY_1_3_LASER_EXP,
                ENEMY_1_4_LASER_EXP, ENEMY_1_5_LASER_EXP]),  # ENEMY 1 LASER

        "enemy_2": (
            [ENEMY_SHIP_2, EXPLOSION3_1, EXPLOSION3_2, EXPLOSION3_3, EXPLOSION3_4, EXPLOSION3_5, EXPLOSION3_6,
             EXPLOSION3_7, EXPLOSION3_8, EXPLOSION3_9, EXPLOSION3_10],  # ENEMY 2 SHIP/ EXPLOSION
            [ENEMY_2_1_LASER, ENEMY_2_2_LASER, ENEMY_2_3_LASER, ENEMY_2_4_LASER,
             ENEMY_2_5_LASER, ENEMY_2_6_LASER, ENEMY_2_7_LASER, ENEMY_2_1_LASER_EXP, ENEMY_2_2_LASER_EXP,
             ENEMY_2_3_LASER_EXP, ENEMY_2_4_LASER_EXP, ENEMY_2_5_LASER_EXP]),  # ENEMY 2 LASER

        "enemy_3": (
            [ENEMY_SHIP_3, EXPLOSION3_1, EXPLOSION3_2, EXPLOSION3_3, EXPLOSION3_4, EXPLOSION3_5, EXPLOSION3_6,
             EXPLOSION3_7, EXPLOSION3_8, EXPLOSION3_9, EXPLOSION3_10],  # ENEMY 3 SHIP/ EXPLOSION
            [ENEMY_3_1_LASER, ENEMY_3_2_LASER, ENEMY_3_3_LASER, ENEMY_3_4_LASER, ENEMY_3_1_LASER_EXP,
             ENEMY_3_2_LASER_EXP, ENEMY_3_3_LASER_EXP, ENEMY_3_4_LASER_EXP]),  # ENEMY 3 LASER

        "enemy_4": (
            [ENEMY_SHIP_4, EXPLOSION4_1, EXPLOSION4_2, EXPLOSION4_3, EXPLOSION4_4, EXPLOSION4_5, EXPLOSION4_6,
             EXPLOSION4_7, EXPLOSION4_8, EXPLOSION4_9, EXPLOSION4_10],  # ENEMY 4 SHIP/ EXPLOSION
            [ENEMY_4_1_LASER, ENEMY_4_2_LASER, ENEMY_4_3_LASER, ENEMY_4_4_LASER, ENEMY_4_5_LASER, ENEMY_4_5_LASER,
             ENEMY_4_1_LASER_EXP, ENEMY_4_2_LASER_EXP, ENEMY_4_3_LASER_EXP, ENEMY_4_4_LASER_EXP,
             ENEMY_4_5_LASER_EXP, ENEMY_4_6_LASER_EXP, ENEMY_4_7_LASER_EXP, ENEMY_4_8_LASER_EXP]),  # ENEMY 4 LASER

        "enemy_5": (
            [ENEMY_SHIP_5, EXPLOSION5_1, EXPLOSION5_2, EXPLOSION5_3, EXPLOSION5_4, EXPLOSION5_5,
             EXPLOSION5_6, EXPLOSION5_7, EXPLOSION5_8, EXPLOSION5_9, EXPLOSION5_10],  # ENEMY 5/ EXPLOSION
            [ENEMY_5_1_LASER, ENEMY_5_2_LASER, ENEMY_5_3_LASER, ENEMY_5_4_LASER, ENEMY_5_5_LASER, ENEMY_5_6_LASER,
             ENEMY_5_1_LASER_EXP, ENEMY_5_2_LASER_EXP, ENEMY_5_3_LASER_EXP, ENEMY_5_4_LASER_EXP,
             ENEMY_5_5_LASER_EXP, ENEMY_5_6_LASER_EXP, ENEMY_5_7_LASER_EXP, ENEMY_5_8_LASER_EXP]),  # ENEMY 5 LASER

        # ENEMY SHIPS PLANET A END

        "enemy_1_b": (
            [ENEMY_1_SHIP, ENEMY_1_EXPLOSION_1, ENEMY_1_EXPLOSION_2, ENEMY_1_EXPLOSION_3, ENEMY_1_EXPLOSION_4,
             ENEMY_1_EXPLOSION_5, ENEMY_1_EXPLOSION_6, ENEMY_1_EXPLOSION_7, ENEMY_1_EXPLOSION_8,
             ENEMY_1_EXPLOSION_9, ENEMY_1_EXPLOSION_10],  # SHIP1/EXPLOSION
            [ENEMY_1_LASER_1, ENEMY_1_LASER_2, ENEMY_1_LASER_3,
             ENEMY_1_LASER_4, ENEMY_1_LASER_5, ENEMY_1_LASER_6,
             ENEMY_1_LASER_7, ENEMY_1_LASER_EXP_1,
             ENEMY_1_LASER_EXP_2, ENEMY_1_LASER_EXP_3,
             ENEMY_1_LASER_EXP_4, ENEMY_1_LASER_EXP_5]),  # LASER1

        "enemy_2_b": (
            [ENEMY_2_SHIP, ENEMY_1_EXPLOSION_1, ENEMY_1_EXPLOSION_2, ENEMY_1_EXPLOSION_3, ENEMY_1_EXPLOSION_4,
             ENEMY_1_EXPLOSION_5, ENEMY_1_EXPLOSION_6, ENEMY_1_EXPLOSION_7, ENEMY_1_EXPLOSION_8,
             ENEMY_1_EXPLOSION_9, ENEMY_1_EXPLOSION_10],
            [ENEMY_2_LASER_1, ENEMY_2_LASER_2, ENEMY_2_LASER_3, ENEMY_2_LASER_4, ENEMY_2_LASER_5,
             ENEMY_2_LASER_6, ENEMY_2_LASER_EXP_1, ENEMY_2_LASER_EXP_2,
             ENEMY_2_LASER_EXP_3, ENEMY_2_LASER_EXP_3,
             ENEMY_2_LASER_EXP_4, ENEMY_2_LASER_EXP_5, ENEMY_2_LASER_EXP_6, ENEMY_2_LASER_EXP_7]),
        "enemy_3_b": (
            [ENEMY_3_SHIP, ENEMY_1_EXPLOSION_1, ENEMY_1_EXPLOSION_2, ENEMY_1_EXPLOSION_3, ENEMY_1_EXPLOSION_4,
             ENEMY_1_EXPLOSION_5, ENEMY_1_EXPLOSION_6, ENEMY_1_EXPLOSION_7, ENEMY_1_EXPLOSION_8,
             ENEMY_1_EXPLOSION_9, ENEMY_1_EXPLOSION_10],
            [ENEMY_3_LASER_1, ENEMY_3_LASER_2, ENEMY_3_LASER_3,
             ENEMY_3_LASER_4, ENEMY_3_LASER_5, ENEMY_3_LASER_6, ENEMY_3_LASER_7,
             ENEMY_3_LASER_EXP_1, ENEMY_3_LASER_EXP_2, ENEMY_3_LASER_EXP_3,
             ENEMY_3_LASER_EXP_4, ENEMY_3_LASER_EXP_5, ENEMY_3_LASER_EXP_6,
             ENEMY_3_LASER_EXP_7]),
        "enemy_4_b": (
            [ENEMY_4_SHIP, ENEMY_1_EXPLOSION_1, ENEMY_1_EXPLOSION_2, ENEMY_1_EXPLOSION_3, ENEMY_1_EXPLOSION_4,
             ENEMY_1_EXPLOSION_5, ENEMY_1_EXPLOSION_6, ENEMY_1_EXPLOSION_7, ENEMY_1_EXPLOSION_8,
             ENEMY_1_EXPLOSION_9, ENEMY_1_EXPLOSION_10],
            [ENEMY_4_LASER_1, ENEMY_4_LASER_2, ENEMY_4_LASER_3, ENEMY_4_LASER_4, ENEMY_4_LASER_5,
             ENEMY_4_LASER_6, ENEMY_4_LASER_7, ENEMY_4_LASER_8, ENEMY_4_LASER_EXP_1, ENEMY_4_LASER_EXP_2,
             ENEMY_4_LASER_EXP_3, ENEMY_4_LASER_EXP_4, ENEMY_4_LASER_EXP_5, ENEMY_4_LASER_EXP_6]),
        "enemy_5_b": (
            [ENEMY_5_SHIP, ENEMY_5_SHIP_EXP_1, ENEMY_5_SHIP_EXP_2, ENEMY_5_SHIP_EXP_3, ENEMY_5_SHIP_EXP_4,
             ENEMY_5_SHIP_EXP_5, ENEMY_5_SHIP_EXP_6, ENEMY_5_SHIP_EXP_7, ENEMY_5_SHIP_EXP_8,
             ENEMY_5_SHIP_EXP_9, ENEMY_5_SHIP_EXP_10],
            [ENEMY_5_LASER_1, ENEMY_5_LASER_2, ENEMY_5_LASER_3, ENEMY_5_LASER_4, ENEMY_5_LASER_5,
             ENEMY_5_LASER_6, ENEMY_5_LASER_7, ENEMY_5_LASER_8, ENEMY_5_LASER_EXP_1, ENEMY_5_LASER_EXP_2,
             ENEMY_5_LASER_EXP_3, ENEMY_5_LASER_EXP_4, ENEMY_5_LASER_EXP_5, ENEMY_5_LASER_EXP_6, ENEMY_5_LASER_EXP_7]),
        "enemy_6_b":
            ([ENEMY_6_SHIP, ENEMY_6_SHIP_EXP_1, ENEMY_6_SHIP_EXP_2, ENEMY_6_SHIP_EXP_3, ENEMY_6_SHIP_EXP_4,
              ENEMY_6_SHIP_EXP_5, ENEMY_6_SHIP_EXP_6, ENEMY_6_SHIP_EXP_7, ENEMY_6_SHIP_EXP_8,
              ENEMY_6_SHIP_EXP_9, ENEMY_6_SHIP_EXP_10],
             [ENEMY_6_LASER_1, ENEMY_6_LASER_2, ENEMY_6_LASER_3, ENEMY_6_LASER_4, ENEMY_6_LASER_5, ENEMY_6_LASER_6,
              ENEMY_6_LASER_7, ENEMY_6_LASER_8, ENEMY_6_LASER_9, ENEMY_6_LASER_EXP_1, ENEMY_6_LASER_EXP_2,
              ENEMY_6_LASER_EXP_3, ENEMY_6_LASER_EXP_4, ENEMY_6_LASER_EXP_5, ENEMY_6_LASER_EXP_6,
              ENEMY_6_LASER_EXP_7, ENEMY_6_LASER_EXP_8])


    }

    def __init__(self, x, y, img_choice):
        super().__init__(x, y)
        self.max_health = 10
        self.health = self.max_health
        self.health_y = 0
        self.health_x = 0
        self.shoot_x = 0  # For the X-axis of the laser
        self.shoot_y = 0  # For the Y-axis of the laser
        self.enemy_vel = 0  # Movement speed for the enemies
        self.choice_img = None  # This is for knowing which enemy image to change when health < 0
        self.index_ship_img = 0  # This is for indexing the explosion images when health < 0
        self.index_laser_img = 0  # This is for indexing the laser explosion image when it collides with player

        self.ship_img = self.ENEMY_MAP[img_choice][0][self.index_ship_img]
        self.laser_img = self.ENEMY_MAP[img_choice][1][self.index_laser_img]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def draw(self, window):
        super().draw(window)

    def move_lasers(self, vel):
        """
        Moving the enemy laser downwards (Y-axis)
        :param vel: Int
        :return: None
        """
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)

    def change_collide_laser(self, window, obj):
        """
        CHANGES THE ENEMY LASER IMAGE WHEN COLLISION IS TRUE
        :param window: WIN
        :param obj: Player
        :return: None
        """
        self.index_laser_img += 1
        try:
            self.laser_img = self.ENEMY_MAP[self.choice_img][1][self.index_laser_img]
        except Exception as e:

            print("IN FILE {ENEMY} [EXCEPTION] AT l-332: ", e)

        window.blit(self.laser_img, (obj.x, obj.y - 20))

    def shoot(self):
        """
        Creates a laser
        :return: None
        """
        laser = Laser(int(self.x + self.ship_img.get_width() / 2 + self.shoot_x),
                      self.y + self.ship_img.get_height() + self.shoot_y,
                      self.laser_img)
        self.lasers.append(laser)

    def move(self):
        self.y += self.enemy_vel
