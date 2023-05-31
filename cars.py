import random
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import numpy as np
from PIL import Image
from PIL import *

texture = None
def load_texture():
    global texture
    texture = glGenTextures(1) 
    glBindTexture(GL_TEXTURE_2D, texture)  
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)  
    image = Image.open("bus.png").convert("RGBA")
    flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)  
    img_data = flipped_image.tobytes()  
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, flipped_image.width, flipped_image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE , img_data)  


def drawPolygon(points, color):
    glBegin(GL_POLYGON)
    glColor4f(*color)
    
    for point in points:
        glVertex2f(point[0], point[1])
    glEnd()

def drawRectangle(points,color):
    glBegin(GL_QUADS)
    glColor4f(*color)
    
    for point in points:
        glVertex2f(point[0],point[1])
    glEnd()
    
    
def drawTriangle(points,color):
    glBegin(GL_TRIANGLES)
    glColor4f(*color) 
    for point in points:
        glVertex2f(point[0],point[1])
    glEnd()

def drawCircle(center,radius,color):        
    glBegin(GL_POLYGON)
    glColor4f(*color)
    Xcenter = center[0]
    Ycenter = center[1]
    r = radius
    for theta in np.arange(0, 2*math.pi, 0.01):
        x = Xcenter+ r*math.cos(theta)
        y = Ycenter+ r*math.sin(theta)
    
        glVertex2f(x, y)
    
    glEnd()


blueBuilding=[(10,100),(90,100),(90,270),(10,270)]
depthBlueBuilding=[(90,100),(95,110),(95,260),(90,270)]
purpleBuilding=[(98,120),(168,120),(168,270),(98,270)]
depthPurpleBuilding=[(168,120),(173,130),(173,260),(168,270)]
redBuilding=[(245,100),(330,100),(330,270),(245,270)]
depthRedBuilding=[(330,100),(335,110),(335,260),(330,270)]
tower=[(336,100),(375,100),(375,270),(336,270)]
towerHead=[(336,100),(355,80),(375,100)]
towerStick=[(355,80),(356,80),(356,60),(356,60)]
sherpaBuilding=[(520,100),(620,100),(620,270),(520,270)]
depthSherpaBuilding=[(620,100),(635,110),(635,260),(620,270)]
greenBuilding=[(375,130),(520,130),(520,270),(375,270)]
#purple building windows
purpleBuildingWindow1=[(103,200),(128,200),(128,215),(103,215)]
purpleBuildingWindow2=[((103+35+5),200),((128+35+5),200),((128+35+5),215),((103+35+5),215)]
purpleBuildingWindow3=[(103,170),(128,170),(128,185),(103,185)]
purpleBuildingWindow4=[((103+35+5),170),((128+35+5),170),((128+35+5),185),((103+35+5),185)]
purpleBuildingWindow5=[(103,140),(128,140),(128,155),(103,155)]
purpleBuildingWindow6=[((103+35+5),140),((128+35+5),140),((128+35+5),155),((103+35+5),155)] 
#red building windows   
redBuildingWindow1=[(255,188+5),(280,188+5),(280,208),(255,208)]
redBuildingWindow2=[((250+40+5),188+5),((275+40+5),188+5),((275+40+5),208),((250+40+5),208)]
redBuildingWindow3=[(255,158+5),(280,158+5),(280,178),(255,178)]
redBuildingWindow4=[((250+40+5),158+5),((275+40+5),158+5),((275+40+5),178),((250+40+5),178)]
redBuildingWindow5=[(255,128+5),(280,128+5),(280,148),(255,148)]
redBuildingWindow6=[((250+40+5),128+5),((275+40+5),128+5),((275+40+5),148),((250+40+5),148)]
redBuildingWindow7=[(255,98+5),(280,98+5),(280,118),(255,118)]
redBuildingWindow8=[((250+40+5),98+5),((275+40+5),98+5),((275+40+5),118),((250+40+5),118)]
#sherpa building windows
sherpaBuildingWindow1=[(525,188+5),(550,188+5),(550,208),(525,208)]
sherpaBuildingWindow2=[(520+40,188+5),(545+40,188+5),(545+40,208),(520+40,208)]
sherpaBuildingWindow3=[(515+80,188+5),(540+80,188+5),(540+80,208),(515+80,208)]
sherpaBuildingWindow4=[(525,158+5),(550,158+5),(550,178),(525,178)]
sherpaBuildingWindow5=[(520+40,158+5),(545+40,158+5),(545+40,178),(520+40,178)]
sherpaBuildingWindow6=[(515+80,158+5),(540+80,158+5),(540+80,178),(515+80,178)]
sherpaBuildingWindow7=[(525,128+5),(550,128+5),(550,148),(525,148)]
sherpaBuildingWindow8=[(520+40,128+5),(545+40,128+5),(545+40,148),(520+40,148)]
sherpaBuildingWindow9=[(515+80,128+5),(540+80,128+5),(540+80,148),(515+80,148)]
sherpaBuildingWindow10=[(525,98+5),(550,98+5),(550,118),(525,118)]
sherpaBuildingWindow11=[(520+40,98+5),(545+40,98+5),(545+40,118),(520+40,118)]
sherpaBuildingWindow12=[(515+80,98+5),(540+80,98+5),(540+80,118),(515+80,118)]
#tower windows
towerWindow1s=[((336+5),98+5),((340+30),98+5),((340+30),150),((336+5),150)]
#blue building windows
blueBuildingWindow1=[(15,188+5),(40,188+5),(40,208),(15,208)]
blueBuildingWindow2=[((15+35+5),188+5),((40+35+5),188+5),((40+35+5),208),((15+35+5),208)]
blueBuildingWindow3=[(15,158+5),(40,158+5),(40,178),(15,178)]
blueBuildingWindow4=[((15+35+5),158+5),((40+35+5),158+5),((40+35+5),178),((15+35+5),178)]
blueBuildingWindow5=[(15,128+5),(40,128+5),(40,148),(15,148)]
blueBuildingWindow6=[((15+35+5),128+5),((40+35+5),128+5),((40+35+5),148),((15+35+5),148)]
blueBuildingWindow7=[(15,98+5),(40,98+5),(40,118),(15,118)]
blueBuildingWindow8=[((15+35+5),98+5),((40+35+5),98+5),((40+35+5),118),((15+35+5),118)]
#green building windows
greenBuildingWindow1=[(380,150),(405,150),(405,180),(380,180)]
greenBuildingWindow2=[(415,150),(440,150),(440,180),(415,180)]
greenBuildingWindow3=[(450,150),(475,150),(475,180),(450,180)]
greenBuildingWindow4=[(485,150),(510,150),(510,180),(485,180)]
greenBuildingWindow5=[(380,190),(405,190),(405,220),(380,220)]
greenBuildingWindow6=[(415,190),(440,190),(440,220),(415,220)]
greenBuildingWindow7=[(450,190),(475,190),(475,220),(450,220)]
greenBuildingWindow8=[(485,190),(510,190),(510,220),(485,220)]
#tree
treeRoots=[(215,190),(220,190),(220,230),(215,230)] 
#blue car body
BlueCarBodys1=[(260-260,340),(500-260,340),(510-260,380),(260-260,380)]
BlueCarHeads2=[(290-260,340),(340-260,280),(440-260,280),(460-260,340)]
#doors
blueBuildingDoors=[(35,220),(65,220),(65,270),(35,270)]
purpleBuildingDoors=[(98+15+10,120+120),(168-15,120+120),(168-15,270),(98+15+10,270)]
redBuildingDoors=[((245+15+10),220),((245+15+40),220),((245+15+40),270),((245+15+10),270)]
towerDoors=[((336+7), 200),((340+27),200),((340+27),270),((336+7),270)]
greenBuildingDoors=[(410,240),(480,240),(480,270),(410,270)]
sherpaBuildingDoors=[(410+130+5,240),(480+130-5,240),(480+130-5,270),(410+130+5,270)]
#blue car windows
blueCarFrontWindow=[(383-260,285),( 435-260,285),(449-260,335),(383-260,335)]
blueCarRearWindow=[(298-260,335),( 340-260,285),(380-260,285),(380-260,335)]
#red car body
redCarBodys1=[(260,340),(430,340),(430,380),(260,380)]
redCarHeads2=[(260,340),(310,280),(410,280),(430,340)]
redEdges=[(430,340),(465,345),(465,380),(430,380)]
redCarFrontWindow=[(268,335),(310,285),(350,285),(350,335)]
redCarRearWindow=[(353,285),( 405,285),(419,335),(353,335)]
#road
lighterRectangulars=[(0,270),(800,270),(800,330),(0,330)]
darkerRectangulars=[(0,330),(800,330),(800,400),(0,400)]
#traffic lights
rectangularBase=[(660,140),(670,140),(670,325),(660,325)] 
rectangularHead=[(645,120),(685,120),(685,200),(645,200)]
#garden 
gardenRectangulars=[(0,150),(800,150),(800,270),(0,270)]
#sky
skyHigherRectangles=[(0,0),(800,0),(800,150),(0,150)]
#street light
streetLightRectangular=[(180,230),(190,230),(190,325),(180,325)] 
streetHeads=[(180,230),(195,220),(210,230)]
streetLights=[(195,230),(205,230),(205,250),(195,250)]
#aeroplane 
bodyPoints = [(640, 70), (660, 70), (660, 90), (640, 90)]
wingPoints = [(660, 80), (680, 80), (660, 90), (640, 90)]
tailPoints = [(640, 80), (640, 90), (630, 85)]
cockpitPoints = [(645, 80), (650, 80), (650, 85), (645, 85)]

#colors
BLACK = (0,0,0,0)
WHITE = (1,1,1,1)
CYAN = (4/255,228/255,226/255,1)
BLUE = (0/255,0/255,255/255,1)
DARK_BLUE = (14/255,53/255,97/255,1)
LIGHT_GREY = (126/255,127/255,126/255,1)
DARK_GREY = (50/255,52/255,50/255,1)
RED = (226/255, 48/255, 14/255,1)
GREEN = (2/255,128/255,1/255,1)
LIME = (0,229/255,3/255,1)
YELLOW = (255/255,255/255,0/255,1)
BROWN = (150/255,75/255,0/255,1)
PURPLE = (129/255, 1/255, 65/255,1)
DARK_BROWN = (124/255,1/255,0/255,1)
SHERPA_BLUE = (1/255,65/255,64/255,1)
GREY = (174/255,179/255,172/255,1)


sky = CYAN
sun = YELLOW
traffic_green = GREEN
traffic_red = BLACK

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(1200, 700)
glutInitWindowPosition(450,0)
glutCreateWindow("Car Design")

glClearColor(1.0, 0.9, 0.0, 1.0)
glPointSize(5)
glColor3f(1,0,0)

gluOrtho2D(0,700, 400,0)      
glClear(GL_COLOR_BUFFER_BIT)

def drawSky(color):
    drawRectangle(points=skyHigherRectangles,color=color)

# randomised
# def drawStarsAsPoints():
#     glPointSize(1.0)
#     glBegin(GL_POINTS) 
#     for _ in range(500):
#         x = random.uniform(0, 800)
#         y = random.uniform(0, 150) 
#         glColor3f(1,1,1) 
#         glVertex2f(x, y)
    
#     glEnd()

def drawStarsAsPoints():
    glPointSize(1.0)
    glBegin(GL_POINTS) 
    star_positions = [(430, 3), (667, 61), (380, 40), (760, 8), (21, 130), (700, 111), (249, 147), (380, 57), (445, 34), (365, 27), (484, 43), (491, 53), (587, 44), (494, 93), (57, 96), (593, 51), (496, 26), (638, 9), (786, 76), (674, 48), (651, 59), (560, 99), (582, 7), (763, 64), (29, 68), (762, 38), (384, 116), (360, 56), (220, 24), (347, 69), (98, 41), (504, 60), (600, 119), (290, 115), (778, 144), (586, 123), (192, 59), (102, 80), (389, 60), (318, 131), (656, 14), (200, 109), (116, 63), (129, 46), (383, 64), (683, 79), (463, 122), (688, 79), (208, 37), (502, 63), (511, 94), (579, 108), (700, 22), (375, 40), (415, 131), (303, 79), (170, 89), (502, 58), (3, 120), (383, 83), (17, 59), (486, 19), (165, 107), (331, 74), (576, 80), (352, 32), (518, 56), (39, 131), (736, 63), (295, 126), (346, 94), (215, 72), (315, 47), (39, 127), (214, 68), (750, 111), (412, 31), (593, 57), (785, 123), (306, 49), (322, 45), (181, 100), (558, 59), (186, 74), (102, 31), (319, 99), (695, 139), (622, 63), (682, 141), (298, 89), (625, 59), (274, 14), (39, 127), (732, 35), (311, 88), (34, 92), (206, 29), (377, 70), (738, 64), (733, 70), (625, 104), (449, 83), (601, 28), (248, 46), (747, 135), (457, 59), (474, 91), (433, 49), (665, 13), (663, 83), (207, 147), (436, 41), (163, 148), (643, 112), (500, 71), (485, 102), (774, 92), (312, 67), (240, 101), (93, 67), (776, 134), (315, 63), (139, 60), (625, 48), (647, 51), (612, 134), (189, 94), (93, 34), (45, 66), (263, 103), (150, 27), (542, 58), (51, 125), (474, 83), (571, 137), (49, 67), (127, 16), (486, 52), (292, 128), (499, 136), (532, 97), (710, 84), (101, 137), (638, 24), (219, 92), (772, 48), (497, 28), (724, 120), (758, 101), (751, 40), (44, 46), (141, 21), (339, 76), (504, 144), (64, 62), (216, 122), (569, 31), (700, 104), (369, 23), (55, 73), (32, 65), (561, 21), (257, 60), (101, 100), (434, 36), (631, 48), (454, 135), (100, 32), (46, 132), (486, 135), (206, 37), (504, 25), (359, 128), (741, 55), (85, 90), (316, 137), (188, 36), (456, 29), (513, 67), (230, 74), (628, 94), (738, 36), (795, 148), (784, 93), (659, 66), (204, 129), (340, 64), (194, 92), (622, 58), (131, 139), (425, 38), (328, 13), (540, 28), (384, 113), (414, 127), (99, 68), (156, 135), (104, 98), (16, 79), (73, 138), (232, 14), (770, 148), (800, 92), (614, 44), (123, 147), (775, 67), (11, 99), (409, 46), (346, 123), (195, 70), (531, 32), (212, 118), (512, 148), (290, 20), (388, 76), (381, 61), (333, 82), (64, 58), (429, 124), (647, 60), (315, 62), (68, 123), (789, 51), (708, 70), (424, 38), (778, 69), (113, 64), (183, 29), (285, 118), (226, 103), (625, 19), (180, 112), (197, 25), (161, 96), (781, 119), (460, 47), (286, 32), (733, 84), (715, 25), (774, 97), (94, 21), (220, 118), (428, 26), (744, 91), (47, 35), (145, 74), (238, 53), (786, 107), (769, 28), (777, 80), (678, 52), (551, 75), (53, 70), (316, 119), (88, 90), (118, 144), (533, 36), (533, 50), (328, 108), (338, 93), (778, 23), (684, 96), (714, 19), (699, 43), (622, 97), (703, 30), (289, 123), (609, 75), (759, 19), (482, 58), (444, 131), (86, 33), (207, 23), (791, 27), (18, 126), (203, 55), (192, 16), (302, 70), (324, 39), (674, 13), (751, 135), (322, 123), (733, 32), (149, 86), (448, 26), (123, 49), (132, 17), (208, 86), (576, 76), (569, 92), (678, 34), (570, 31), (214, 107), (88, 144), (196, 67), (393, 36), (421, 134), (181, 40), (683, 121), (441, 77), (215, 110), (239, 36), (29, 103), (751, 108), (227, 43), (456, 49), (529, 130), (683, 35), (750, 107), (780, 121), (779, 71), (759, 38), (781, 132), (72, 71), (68, 119), (781, 92), (252, 94), (4, 39), (672, 13), (289, 77), (174, 49), (367, 82), (407, 122), (772, 77), (715, 122), (719, 146), (764, 83), (728, 81), (128, 96), (348, 79), (668, 54), (28, 89), (124, 63), (775, 101), (38, 19), (547, 132), (742, 69), (315, 107), (187, 33), (587, 81), (316, 61), (487, 65), (55, 30), (602, 99), (601, 45), (384, 66), (39, 103), (327, 94), (499, 80), (198, 147), (155, 31), (440, 22), (329, 148), (334, 72), (763, 137), (154, 80), (449, 96), (8, 90), (321, 54), (786, 39), (180, 142), (617, 137), (77, 73), (763, 27), (261, 98), (94, 140), (137, 24), (210, 43), (642, 95), (750, 13), (774, 93), (751, 95), (396, 33), (724, 47), (731, 34), (64, 66), (532, 105), (311, 54), (217, 96), (497, 42), (763, 38), (792, 145), (772, 135), (502, 148), (513, 42), (712, 87), (98, 72), (276, 50), (614, 140), (618, 13), (747, 23), (785, 70), (72, 92), (785, 61), (776, 85), (14, 142), (481, 17), (402, 40), (120, 38), (308, 52), (357, 46), (559, 56), (574, 91), (120, 54), (620, 139), (748, 129), (26, 146), (788, 97), (779, 120), (624, 19), (782, 48), (488, 63), (348, 146), (139, 52), (142, 12), (548, 118), (506, 92), (756, 83), (551, 14), (344, 57), (711, 42), (739, 102), (455, 69), (273, 57), (782, 119), (51, 135), (201, 137), (737, 146), (518, 146), (784, 78), (439, 144), (248, 104), (488, 79), (73, 98), (303, 83), (716, 32), (72, 23), (734, 26), (327, 81), (84, 39), (770, 54), (666, 117), (584, 16), (766, 142), (367, 110), (141, 62), (240, 123), (438, 64), (93, 29), (751, 109), (540, 65), (687, 92), (453, 80), (238, 63), (799, 92), (84, 47), (242, 127), (31, 87), (603, 62), (367, 96), (363, 81), (157, 95), (397, 54), (321, 55), (500, 120), (790, 31), (342, 85), (726, 88), (732, 47), (569, 32), (39, 69), (721, 100), (67, 24), (196, 55), (58, 135), (36, 42), (571, 138), (707, 44), (688, 59), (224, 121), (395, 76), (799, 83), (542, 70), (216, 83), (749, 12), (220, 46), (361, 70), (455, 41), (258, 49), (720, 117), (598, 90), (202, 18), (418, 32), (262, 103), (236, 57), (350, 68), (484, 86), (772, 34), (449, 67), (708, 92), (187, 85), (303, 141), (119, 41), (605, 111), (533, 38), (482, 39), (542, 75), (249, 50), (312, 140), (625, 132), (265, 39), (422, 148), (769, 24), (518, 135), (674, 35), (734, 78), (76, 130), (715, 111), (311, 116), (369, 148), (794, 66), (226, 86), (708, 100), (304, 51), (158, 56), (775, 54), (597, 118), (338, 77), (616, 87), (643, 11), (504, 73), (97, 47), (771, 25), (648, 96), (477, 54), (562, 26), (674, 106), (128, 45), (34, 32), (623, 92), (432, 109), (388, 50), (606, 136), (454, 123), (642, 133), (262, 85), (153, 103), (688, 116), (128, 93), (220, 111), (700, 97), (590, 74), (330, 32), (546, 80), (25, 84), (752, 140), (690, 48), (505, 37), (703, 41), (346, 132), (248, 93), (195, 72), (160, 54), (315, 66), (236, 46), (90, 109), (518, 100), (448, 25), (587, 67), (85, 30), (189, 118), (564, 36), (541, 54), (711, 62), (166, 14), (126, 127), (154, 47), (78, 90), (670, 50), (222, 29), (80, 139), (84, 112), (154, 52), (475, 48), (477, 92), (524, 102), (683, 130), (478, 35), (165, 32), (163, 35), (606, 19), (107, 41), (199, 141), (603, 132), (646, 14), (95, 60), (168, 56), (708, 137), (584, 29), (556, 79), (133, 86), (642, 12), (183, 96), (499, 146), (622, 95), (200, 118), (48, 98), (437, 124), (559, 53), (94, 86), (619, 38), (100, 147), (728, 80), (562, 135), (122, 17), (745, 137), (168, 56), (261, 106), (271, 50), (723, 112), (447, 48), (738, 138), (101, 59), (570, 91), (669, 94), (592, 108), (677, 46), (636, 59), (727, 55), (240, 91), (282, 57), (230, 91), (575, 41), (39, 48), (68, 129), (202, 64), (710, 86), (176, 49), (278, 88), (709, 123), (494, 86), (27, 101), (580, 39), (172, 96), (435, 131), (176, 95), (480, 58), (431, 137), (573, 32), (569, 146), (73, 104), (190, 100), (267, 57), (509, 29), (240, 135), (606, 85), (589, 82), (652, 88), (68, 112), (532, 100), (510, 52), (315, 30), (220, 100), (285, 104), (760, 62), (478, 67), (401, 91), (142, 132), (338, 42), (716, 44), (370, 32), (487, 138), (771, 79), (538, 37), (646, 34), (744, 64), (76, 19), (548, 101), (576, 60), (593, 38), (384, 118), (797, 63), (500, 138), (214, 143), (674, 46), (539, 102), (117, 28), (336, 23), (565, 53), (146, 62), (390, 110), (312, 67), (632, 22), (450, 19), (528, 87), (628, 89), (614, 26), (736, 86), (202, 120), (319, 78), (505, 81), (777, 108), (509, 117), (487, 38), (702, 84), (607, 35), (145, 81), (652, 84), (520, 42), (139, 123), (569, 138), (220, 108), (753, 65), (68, 24), (565, 35), (436, 77), (590, 49), (235, 93), (197, 144), (486, 55), (84, 79), (126, 87), (216, 96), (743, 30), (493, 93), (785, 23), (574, 25), (329, 100), (793, 132), (238, 67), (565, 94), (433, 65), (88, 29), (593, 98), (683, 29), (176, 104), (710, 39), (671, 42), (217, 100), (629, 130), (225, 41), (609, 108), (730, 97), (392, 112), (160, 87), (51, 120), (495, 52), (492, 112), (651, 98), (631, 34), (753, 43), (414, 24), (354, 92), (456, 72), (89, 117), (105, 77), (584, 135), (727, 41), (671, 82), (703, 132), (628, 100), (80, 59), (790, 64), (569, 22), (595, 63), (656, 130), (79, 76), (600, 71), (315, 120), (119, 36), (510, 141), (710, 26), (523, 25), (494, 28), (763, 55), (595, 67), (697, 87), (248, 142), (377, 122), (625, 47), (256, 39), (382, 82), (508, 143), (310, 106), (133, 48), (694, 75), (459, 19), (730, 96), (302, 53), (548, 84), (244, 81), (741, 51), (584, 54), (315, 119), (314, 95), (110, 95), (388, 71), (96, 102), (797, 137), (598, 84), (545, 86), (550, 47), (764, 72), (718, 66), (655, 139), (140, 26), (608, 84), (553, 85), (507, 119), (114, 75), (748, 123), (579, 62), (580, 148), (546, 75), (526, 51), (411, 100), (685, 37), (431, 94), (454, 84), (712, 42), (733, 82), (611, 78), (457, 75), (767, 75), (334, 121), (773, 62), (736, 19), (747, 78), (191, 47), (673, 72), (165, 80), (407, 94), (762, 108), (731, 69), (561, 120), (571, 90), (209, 136), (176, 26), (694, 49), (480, 109), (541, 86), (766, 129), (476, 100), (773, 136), (625, 83), (322, 69), (362, 37), (630, 139), (405, 85), (673, 31), (584, 45), (652, 62), (567, 126), (759, 135), (659, 104), (298, 96), (149, 33), (434, 22), (244, 53), (527, 82), (714, 28), (242, 119), (520, 39), (741, 72), (358, 65), (672, 85), (592, 24), (361, 126), (475, 50), (750, 25), (613, 88), (724, 141), (647, 130), (742, 56), (272, 72), (459, 98), (665, 96), (451, 91), (484, 45), (307, 62), (523, 115), (742, 74), (663, 121), (543, 132), (723, 53), (392, 44), (560, 53), (187, 85), (453, 36), (757, 100), (526, 98), (727, 32), (689, 103), (294, 35), (202, 141), (695, 54), (731, 112), (676, 69), (365, 45), (657, 56), (457, 110), (254, 78), (238, 42), (695, 108), (434, 38), (255, 58), (640, 49), (689, 83), (128, 119), (733, 101), (346, 78), (508, 47), (615, 29), (670, 44), (779, 28), (601, 53), (771, 100), (534, 111), (532, 66), (367, 66), (285, 78), (647, 142), (492, 46), (670, 119), (764, 22), (753, 100), (577, 82), (351, 39), (497, 23), (732, 133), (579, 44), (747, 34), (524, 144), (756, 91), (561, 42), (632, 123), (724, 46), (289, 105), (351, 67), (398, 43), (483, 64), (766, 101), (646, 97), (490, 79), (131, 50), (693, 68), (611, 65), (586, 71), (515, 26), (605, 83), (589, 130), (414, 93), (125, 105), (727, 102), (526, 26), (337, 96), (528, 131), (455, 110), (135, 57), (546, 53), (139, 44), (589, 91), (570, 80), (331, 38), (222, 112), (686, 36), (486, 77), (686, 52), (432, 33), (136, 120), (763, 32), (640, 70), (370, 40), (601, 71), (600, 91), (144, 67), (644, 102), (432, 84), (221, 93), (188, 76), (456, 35), (608, 119), (352, 132), (675, 138), (689, 23), (762, 35), (550, 72), (619, 30), (650, 66), (595, 46), (163, 72), (738, 63), (688, 51), (519, 98), (718, 80), (630, 86), (199, 50), (250, 37), (441, 40), (408, 122), (435, 140), (589, 36), (427, 68), (390, 112), (299, 62), (716, 82)]
    
    for position in star_positions:
        x, y = position
        glColor3f(1, 1, 1) 
        glVertex2f(x, y)
    
    glEnd()


# def drawStars():
#     size = 10.0
#     outer_radius = 0.4 * size
#     inner_radius = 0.2 * size
#     num_points = 5
#     for _ in range(50):
#         x = random.uniform(0, 800)  
#         y = random.uniform(0, 150)
#         glColor3f(1.0, 1.0, 1.0)
#         glBegin(GL_TRIANGLE_FAN)
#         glVertex2f(x, y)
#         angle = 2 * math.pi / num_points
#         for i in range(num_points * 2):
#             theta = i * angle
#             radius = outer_radius if i % 2 == 0 else inner_radius
#             point_x = x + radius * math.cos(theta)
#             point_y = y + radius * math.sin(theta)
#             glVertex2f(point_x, point_y)
#         glEnd()

def drawStars():
    size = 10.0
    outer_radius = 0.4 * size
    inner_radius = 0.2 * size
    num_points = 5
    star_positions = [(430, 3), (667, 61), (380, 40), (760, 8), (21, 130), (700, 111), (249, 147), (380, 57), (445, 34), (365, 27), (484, 43), (491, 53), (587, 44), (494, 93), (57, 96), (593, 51), (496, 26), (638, 9), (786, 76), (674, 48), (651, 59), (560, 99), (582, 7), (763, 64), (29, 68), (762, 38), (384, 116), (360, 56), (220, 24), (347, 69), (98, 41), (504, 60), (600, 119), (290, 115), (778, 144), (586, 123), (192, 59), (102, 80), (389, 60), (318, 131), (656, 14), (200, 109), (116, 63), (129, 46), ]

    for position in star_positions:
        ppx, ppy = position
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(ppx, ppy)
        angle = 2 * math.pi / num_points
        for i in range(num_points * 2):
            theta = i * angle
            radius = outer_radius if i % 2 == 0 else inner_radius
            point_x = ppx + radius * math.cos(theta)
            point_y = ppy + radius * math.sin(theta)
            glVertex2f(point_x, point_y)
        glEnd()

def drawGarden():
    drawRectangle(points=gardenRectangulars,color=LIME)

def drawDoors():
    drawRectangle(points=blueBuildingDoors,color=BLACK)
    drawRectangle(points=purpleBuildingDoors,color=BLACK)
    drawRectangle(points=redBuildingDoors,color=BLACK)
    drawRectangle(points=towerDoors,color=BLACK)
    drawRectangle(points=greenBuildingDoors, color=BLACK)
    drawRectangle(points=sherpaBuildingDoors, color=BLACK)
    
def drawBlueBuildingWindows():

    drawRectangle(points= blueBuildingWindow1, color=BLACK)
    drawRectangle(points= blueBuildingWindow2, color=BLACK)
    drawRectangle(points= blueBuildingWindow3, color=BLACK)
    drawRectangle(points= blueBuildingWindow4, color=BLACK)
    drawRectangle(points= blueBuildingWindow5, color=BLACK)
    drawRectangle(points= blueBuildingWindow6, color=BLACK)
    drawRectangle(points= blueBuildingWindow7, color=BLACK)
    drawRectangle(points= blueBuildingWindow8, color=BLACK)

def drawSherpaBuildingWindows():
    drawRectangle(points=sherpaBuildingWindow1, color=BLACK)
    drawRectangle(points=sherpaBuildingWindow2, color=BLACK)
    drawRectangle(points=sherpaBuildingWindow3, color=BLACK)
    drawRectangle(points=sherpaBuildingWindow4, color=BLACK)
    drawRectangle(points=sherpaBuildingWindow5, color=BLACK)
    drawRectangle(points=sherpaBuildingWindow6, color=BLACK)
    drawRectangle(points=sherpaBuildingWindow7, color=BLACK)
    drawRectangle(points=sherpaBuildingWindow8, color=BLACK)
    drawRectangle(points=sherpaBuildingWindow9, color=BLACK)
    drawRectangle(points=sherpaBuildingWindow10, color=BLACK)
    drawRectangle(points=sherpaBuildingWindow11, color=BLACK)
    drawRectangle(points=sherpaBuildingWindow12, color=BLACK)


def drawPurpleBuildingWindows():
    drawRectangle(points=purpleBuildingWindow1,color=BLACK)
    drawRectangle(points=purpleBuildingWindow2,color=BLACK)
    drawRectangle(points=purpleBuildingWindow3,color=BLACK)
    drawRectangle(points=purpleBuildingWindow4,color=BLACK)
    drawRectangle(points=purpleBuildingWindow5,color=BLACK)
    drawRectangle(points=purpleBuildingWindow6,color=BLACK)
    
def drawRedBuildingWindows():
    drawRectangle(points=redBuildingWindow1,color=BLACK)
    drawRectangle(points=redBuildingWindow2,color=BLACK)   
    drawRectangle(points=redBuildingWindow3,color=BLACK)
    drawRectangle(points=redBuildingWindow4,color=BLACK)
    drawRectangle(points=redBuildingWindow5,color=BLACK)
    drawRectangle(points=redBuildingWindow6,color=BLACK)
    drawRectangle(points=redBuildingWindow7,color=BLACK)
    drawRectangle(points=redBuildingWindow8,color=BLACK)

def drawTowerWindows():
    drawRectangle(points=towerWindow1s, color=BLACK)

def drawGreenBuildingWindows():
    drawRectangle(points=greenBuildingWindow1, color=BLACK)
    drawRectangle(points=greenBuildingWindow2, color=BLACK)
    drawRectangle(points=greenBuildingWindow3, color=BLACK)
    drawRectangle(points=greenBuildingWindow4, color=BLACK)
    drawRectangle(points=greenBuildingWindow5, color=BLACK)
    drawRectangle(points=greenBuildingWindow6, color=BLACK)
    drawRectangle(points=greenBuildingWindow7, color=BLACK)
    drawRectangle(points=greenBuildingWindow8, color=BLACK)




def drawBuildings():
    drawRectangle(points=blueBuilding,color=BLUE)
    drawRectangle(points=depthBlueBuilding,color=BLUE)
    drawRectangle(points=purpleBuilding,color=PURPLE)
    drawRectangle(points=depthPurpleBuilding,color=PURPLE)
    drawRectangle(points=redBuilding,color=RED)
    drawRectangle(points=depthRedBuilding,color=RED)
    drawRectangle(points=tower,color=DARK_BROWN)
    drawTriangle(points=towerHead,color=DARK_BROWN)
    drawRectangle(points=towerStick,color=DARK_BROWN)
    drawRectangle(points=greenBuilding,color=GREEN )
    drawRectangle(points=sherpaBuilding,color=SHERPA_BLUE)    
    drawRectangle(points=depthSherpaBuilding,color=SHERPA_BLUE)


def drawBlueCar():    
    drawRectangle(points = BlueCarBodys1, color=BLUE)
    drawRectangle(points = BlueCarHeads2, color=BLUE)
    drawCircle(center = (340-260,380), radius = 15 , color=BLACK)
    drawCircle(center = (450-260,380) , radius = 15, color = BLACK)
    drawRectangle(points=blueCarRearWindow,color=BLACK)
    drawRectangle(points=blueCarFrontWindow,color=BLACK)

def drawRedCar(): 
    drawRectangle(points=redEdges,color=RED)
    drawRectangle(points = redCarBodys1, color=RED)
    drawRectangle(points = redCarHeads2, color=RED)
    drawCircle(center = (310,380), radius = 15 , color = BLACK)
    drawCircle(center = (410,380) , radius = 15, color = BLACK)
    drawRectangle(points=redCarFrontWindow,color=BLACK)
    drawRectangle(points=redCarRearWindow,color=BLACK)



    
def drawTrafficLight(cred, cgreen):
    drawRectangle(points=rectangularBase,color=BLACK)
    drawRectangle(points=rectangularHead,color=GREY)
    drawCircle(center=(665,135),radius=11,color=cred)
    drawCircle(center=(665,160),radius=11,color=YELLOW)
    drawCircle(center=(665,185),radius=11,color=cgreen)

def drawStreetLight():
    drawRectangle(points=streetLightRectangular,color=BLACK)
    drawTriangle(points=streetHeads,color=BLACK)
    drawRectangle(points=streetLights,color=(1,1,1,1))


def drawTree():
    drawRectangle(points=treeRoots,color=BROWN)
    drawCircle(center=(210,190),radius=15,color=GREEN)
    drawCircle(center=(225,190),radius=15,color=GREEN)
    drawCircle(center=(217,170),radius=15,color=GREEN)
    drawCircle(center=(217,152),radius=10,color=GREEN)
    

def drawRoad():
    drawRectangle(points=lighterRectangulars,color=LIGHT_GREY)      
    drawRectangle(points=darkerRectangulars,color=DARK_GREY)

def drawSun(color):
    drawCircle(center=(40,40),radius=20,color=color)


def drawMoon():
    drawCircle(center=(40,40),radius=20,color=WHITE)

def drawClouds():
    drawCircle(center=(200,40),radius=10,color=WHITE)
    drawCircle(center=(200 + 20,40),radius=17,color=WHITE)
    drawCircle(center=(200 + 40,40),radius=17,color=WHITE)
    drawCircle(center=(200 + 60,40),radius=17,color=WHITE)
    drawCircle(center=(200 + 80,40),radius=10,color=WHITE)
    drawCircle(center=(100 ,40),radius=10,color=WHITE)
    drawCircle(center=(100 + 20 ,40),radius=17,color=WHITE)
    drawCircle(center=(100 + 40 ,40),radius=17,color=WHITE)
    drawCircle(center=(100 + 60 ,40),radius=10,color=WHITE)
    drawCircle(center=(200 + 300,40),radius=10,color=WHITE)
    drawCircle(center=(200 + 20 + 300,40),radius=17,color=WHITE)
    drawCircle(center=(200 + 40 + 300,40),radius=17,color=WHITE)
    drawCircle(center=(200 + 60 + 300,40),radius=17,color=WHITE)
    drawCircle(center=(200 + 80 + 300,40),radius=10,color=WHITE)
    drawCircle(center=(100 + 300,40),radius=10,color=WHITE)
    drawCircle(center=(100 + 20 + 300,40),radius=17,color=WHITE)
    drawCircle(center=(100 + 40 + 300,40),radius=17,color=WHITE)
    drawCircle(center=(100 + 60 + 300,40),radius=10,color=WHITE)


def drawAeroplane():
    drawPolygon(points=bodyPoints,color= GREY)
    drawPolygon(points=wingPoints,color= LIGHT_GREY)
    drawPolygon(points=tailPoints,color= DARK_GREY)
    drawPolygon(points=cockpitPoints,color= BLUE)


def drawBus():
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glColor4f(1.0, 1.0, 1.0, 1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex2f(455, 500)
    glTexCoord2f(1.0, 0.0)
    glVertex2f(850, 500)
    glTexCoord2f(1.0, 1.0)
    glVertex2f(850, 100)
    glTexCoord2f(0.0, 1.0)
    glVertex2f(455, 100)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    glDisable(GL_BLEND)


def scene(key,x,y):
    global stop, sky, sun,traffic_green, traffic_red
    if key == b'm':
        sky = CYAN
        sun = YELLOW
        # glClear(GL_COLOR_BUFFER_BIT)
    if key == b'n':
        sky = BLACK
        sun = WHITE
        # glClear(GL_COLOR_BUFFER_BIT)
    if key == b's':
        stop = True
        traffic_green = BLACK
        traffic_red = RED
    if key == b'g':
        stop = False
        traffic_red = BLACK
        traffic_green = GREEN
    # glutPostRedisplay()

def morningScene():
    # glClear(GL_COLOR_BUFFER_BIT)
    glutPostRedisplay()

    drawSky(sky)
    drawSun(sun)
    
    drawGarden()
    drawRoad()
    if sky == BLACK:
        # drawStarsAsPoints()
        drawStars()
    drawBuildings()
    drawTree()
    drawTrafficLight(traffic_red,traffic_green)
    drawStreetLight()
    drawDoors()
    drawBlueBuildingWindows()
    drawPurpleBuildingWindows()
    drawRedBuildingWindows()
    drawTowerWindows()
    drawGreenBuildingWindows()
    drawSherpaBuildingWindows()

    move()
    glutSwapBuffers()

stop = False
x_pos = [0,0]
aero_pos_x = 0
aero_pos_y = 0

def move():
    glPushMatrix()
    glTranslatef(x_pos[0], 0, 0 )
    if(sky == CYAN):
        drawClouds()
    glPopMatrix()
    

    glPushMatrix()
    glTranslatef(aero_pos_x, aero_pos_y, 0 )
    drawAeroplane()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(x_pos[1], 0, 0 )
    drawBlueCar()
    drawRedCar()
    drawBus()
    glPopMatrix()


def update_move():
    global x_pos, aero_pos_x, aero_pos_y
    x_pos[0] += 2 #cloud speed
    if x_pos[0] >= 650:
        x_pos[0] = -450
    if not stop:
        x_pos[1] += 2 #car speed
        if x_pos[1] >= 750:
            x_pos[1] = -850
    aero_pos_x -= 2
    aero_pos_y -= 0.5
    if aero_pos_y == -90:
        aero_pos_x = 100
        aero_pos_y = 100
        
def idle():
    update_move()
    glutPostRedisplay()

glutDisplayFunc(morningScene)
glutKeyboardFunc(scene)
load_texture()
glutIdleFunc(idle)
glutMainLoop()
