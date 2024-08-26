'''
Basis Plane Animator
basic-plane-animator.py
'''

import bpy
import bmesh
import math

# Initialize lists of tuples

#START

#SET plane positions AS xyz values as tuples
positions = (0,0,3), (0,0,3), (0,0,3), (0,0,3), (0,0,3), (0,0,3), (0,0,3), (0,0,3), (0,0,3),                                     (80, 0, 4), (160, 0, 30), (240, 0, 60), (320, 0, 100), (340, 0, 100), (360, 0, 100), (380, 0, 100), (400, 0, 100), (420, 0, 100), (440, 0, 100), (460, 0, 100), (480, 0, 100), (500, 10, 100), (520, 0, 100), (540, -10, 100), (560, 0, 100), (580, 0, 100), (600, 0, 100),            (620, 0, 100), (640, 0, 100), (660, 0, 100), (680, 0, 100), (720, 0, 150), (760, 0, 200), (780, 10, 190), (770, 10, 180), (760, 0, 170), (770, -10, 160), (780, -10, 150), (790, 0, 140), (780, 10, 130), (770, 10, 120), (760, 0, 110), (770, -10, 100),      (780, -10, 90), (790, 0, 80),     (780, 10, 70), (770, 10, 60), (760, 0, 50),        (770, -10, 40), (780, -10, 30), (790, 0, 20), (820, 0, 10), (870, 0, 6), (925, 0, 3)
            #1                                                                                                                    2           3             4            5              6              7              8              9              10             11             12             13             14             15             16             17             18             19                         20             21             22             23             24             25             26 descent       27             28             29               30               31             32              33              34             35                     36             37                38             39             40                   41              42              43            44           45              END
            
#SET all rotations AS xyz values as tuples
rotations = (0, 6, 180), (0, 6, 180), (0, 6, 180), (0, 6, 180), (0, 6, 180), (0, 6, 180), (0, 6, 180), (0, 6, 180), (0, 6, 180), (0, 6, 180), (0, 30, 180), (0, 30, 180), (0, 15, 180), (0, 0, 180), (0, 0, 180), (0, 0, 180), (0, 0, 180), (0, 0, 180), (0, 0, 180),         (0, 0, 180), (0, 0, 180), (20, 0, 180), (0, 0, 180), (-20, 0, 180), (0, 0, 180),               (0, 0, 180), (0, 0, 180),                 (0, 0, 180), (0, 0, 180), (0, 0, 180), (0, 0, 180),         (0, 45, 180), (0, 0, 180), (45, -70, 180), (90, -70, 180), (135, -70, 180), (180, -70, 180), (225, -70, 180), (270, -70, 180), (315, -70, 180), (360, -70, 180), (405, -70, 180), (450, -70, 180), (495, -70, 180), (540, -70, 180), (585, -70, 180), (630, -70, 180), (675, -70, 180), (720, -70, 180), (765, -70, 180), (720, -70, 180), (720, -30, 180), (720, -15, 180), (720, 6, 180)
            #1                                                                                                                    2           3              4            5              6           7            8            9            10           11                   12           13           14           15           16           17                          18           19                           20           21           22           23                   24            25           26              27              28               29               30               31               32               33               34               35               36               37               38               39               40               41               42               43               44              45                 END
 
stunt_one_positions = (310, 14, 101), (330, 14, 101), (350, 14, 101), (370, 14, 101), (390, 14, 101), (410, 14, 101), (430, 14, 101), (430, 0, 115), (450, 0, 115), (470, 0, 115), (490, 0, 115), (510, 0, 115), (550, -12, 96), (570, -12, 96), (590, -12, 96), (610, -12, 96), (620, 20, 110), (630, 20, 110)
                     #1               2               3                4              5                6               7              8              9              10             11             12             13              14              15              16              17              18
stunt_one_rotations = (90, 0, 246), (90, 10, 246), (90, 0, 246),       (90, -10, 246), (90, 0, 246), (90, 5, 246),       (90, 0, 246), (75, 0, 270), (75, 0, 270), (75, 0, 270), (75, 0, 270), (75, 0, 270),        (100, 10, 290), (100, 0, 290), (100, -5, 290), (100, 0, 290), (80, -10, 240), (80, 0, 240)
                     #1             2             3                    4             5             6                   7            8             9             10            11            12                   13             14             15              16            17            18

stunt_two_positions = (769, 0, 275), (769, 0, 270), (769, 0, 265), (769, 0, 260), (774, 0, 255), (774, 0, 250), (774, 0, 245), (774, 0, 240), (774, 0, 235), (774, 0, 230), (774, 0, 225), (774, 0, 220), (774, 0, 215), (774, 0, 210), (774, 0, 185), (774, 0, 175), (774, 0, 165), (774, 0, 155)
                      #1             2              3              4              5               6             7               8             9              10             11             12             13             14             15             16             17             18
stunt_two_rotations = (0, 0, -90), (0, 0, -90), (0, 0, -90), (0, 0, -90),         (0, 0, -90), (0, 0, -90), (0, 0, -90), (0, 0, -90), (0, 0, -90), (0, 0, -90), (0, 0, -90),               (0, 0, -90), (0, 0, -90), (0, 0, -90), (0, 0, -90), (0, 0, -90), (0, 0, -90),             (10, 0, -90)
                      #1            2           3            4                    5             6            7            8           9            10           11                         12           13           14           15           16           17                       18

# Initialize object references

plane = bpy.data.objects['Airplane']

ground_cam = bpy.data.objects['Start/End Cam']

stunt_one_cam = bpy.data.objects['Stunt 1 Cam']

stunt_two_cam = bpy.data.objects['Stunt 2 Cam']

#Animate ground cam from starting position to end position 
def animate_ground_cam():
    
    bpy.context.scene.frame_set(300)
    
    ground_cam.location = (102, -20, 1)
    ground_cam.rotation_euler = (
        math.radians(98),
        math.radians(0.8),
        math.radians(64)
        )
    
    ground_cam.keyframe_insert(data_path = 'location', index=-1)
    ground_cam.keyframe_insert(data_path = 'rotation_euler', index=0)
    ground_cam.keyframe_insert(data_path = 'rotation_euler', index=1)
    ground_cam.keyframe_insert(data_path = 'rotation_euler', index=2)
    
    bpy.context.scene.frame_set(330)
    
    ground_cam.location = (954, 15, 1)
    ground_cam.rotation_euler = (
        math.radians(98),
        math.radians(0.8),
        math.radians(106)
        )
    
    ground_cam.keyframe_insert(data_path = 'location', index=-1)
    ground_cam.keyframe_insert(data_path = 'rotation_euler', index=0)
    ground_cam.keyframe_insert(data_path = 'rotation_euler', index=1)
    ground_cam.keyframe_insert(data_path = 'rotation_euler', index=2)
    
    pass

def animate_stunt_one_cam():
    frame_num = 390
    
       
    for index, position in enumerate(stunt_one_positions):
        
        bpy.context.scene.frame_set(frame_num)
        
        # Record locations for camera coords 
        stunt_one_cam.location = position
        
        #Record rotation angles in XYZ Euler
        stunt_one_cam.rotation_euler = (math.radians(stunt_one_rotations[index][0]), math.radians(stunt_one_rotations[index][1]), math.radians(stunt_one_rotations[index][2]))
            
        #Record keyframes camera
        stunt_one_cam.keyframe_insert(data_path = 'location', index=-1)
        stunt_one_cam.keyframe_insert(data_path = 'rotation_euler', index=0)
        stunt_one_cam.keyframe_insert(data_path = 'rotation_euler', index=1)
        stunt_one_cam.keyframe_insert(data_path = 'rotation_euler', index=2)
            
        frame_num += 30
    
    pass

def animate_stunt_two_cam():
    frame_num = 960
    
       
    for index, position in enumerate(stunt_two_positions):
        
        bpy.context.scene.frame_set(frame_num)
        
        # Record locations for camera coords 
        stunt_two_cam.location = position
        
        #Record rotation angles in XYZ Euler
        stunt_two_cam.rotation_euler = (math.radians(stunt_two_rotations[index][0]), math.radians(stunt_two_rotations[index][1]), math.radians(stunt_two_rotations[index][2]))
            
        #Record keyframes camera
        stunt_two_cam.keyframe_insert(data_path = 'location', index=-1)
        stunt_two_cam.keyframe_insert(data_path = 'rotation_euler', index=0)
        stunt_two_cam.keyframe_insert(data_path = 'rotation_euler', index=1)
        stunt_two_cam.keyframe_insert(data_path = 'rotation_euler', index=2)
            
        frame_num += 30
    
    pass

# Animate Plane
def set_keyframes():
    frame_num = 0
    
       
    for index, position in enumerate(positions):
        
        bpy.context.scene.frame_set(frame_num)
        
        # Record locations for plane coords 
        plane.location = position
        
        #Record rotation angles in XYZ Euler
        plane.rotation_euler = (
            math.radians(rotations[index][0]),
            math.radians(rotations[index][1]),
            math.radians(rotations[index][2])
            )
            
        #Record keyframes plane
        plane.keyframe_insert(data_path = 'location', index=-1)
        plane.keyframe_insert(data_path = 'rotation_euler', index=0)
        plane.keyframe_insert(data_path = 'rotation_euler', index=1)
        plane.keyframe_insert(data_path = 'rotation_euler', index=2)
            
        frame_num += 30
    
    pass

'''
When I implemented this function I used arithmetic instead of locations, so it 
became very frustrating when running the script multiple times as vertices would
leave from their standard positions.

Looking back I should've just done this the same way as the plane since it doesn't 
affect the end location.
'''
def set_tree_keyframes():
    Icosphere = bpy.context.object

    Icosphere.name = 'Icosphere6'
    
    # Deslecting all objects
    # bpy.ops.object.select_all(action='DESELECT')

    # Selecting by name a specific object in the Outliner
    bpy.data.objects[Icosphere.name].select_set(True)

    # Setting the mode to Edit
    bpy.ops.object.mode_set(mode='EDIT')

    # Choose the vertices type for mesh editing
    bpy.ops.mesh.select_mode(type='VERT')

    # deselect all verts
    bpy.ops.mesh.select_all(action='DESELECT')

    # Copy mesh of cube_vert_edited into variable vert_mesh in editable form
    vert_mesh = bmesh.from_edit_mesh(Icosphere.data)

    # Confirm that the bm data-mesh object is whole and not broken
    vert_mesh.verts.ensure_lookup_table()

    # Selects the desired vertex to animate
    vert_mesh.verts[0].select = True
    
    #Exactly the length for ten seconds 
    for frame_basis in range(16):
    
        # Exposes the coord values of vertex at index 5 of the cube_vert_edited.vertices[] list
        x, y, z = Icosphere.data.vertices[0].co
        
        # For every even numbered frame_basis
        if frame_basis % 2 == 0:
            # Perform arithmetic on the values
            Icosphere.data.vertices[0].co = (x, y, z + 1)
        
        else:     
            # Perform arithmetic on the values
            Icosphere.data.vertices[0].co = (x, y, z - 1)
    
    
        # Insert a key frame of the state of vertex coord values ever 10 frames after the 100th frame
        Icosphere.data.vertices[0].keyframe_insert('co', frame = frame_basis * 15)
    
        pass

    # Restore back to object mode
    bpy.ops.object.mode_set(mode='OBJECT')

    # Deslect all
    bpy.ops.object.select_all(action = 'DESELECT')

def main():
    
    #set_tree_keyframes()
    animate_stunt_one_cam()
    animate_stunt_two_cam()
    animate_ground_cam()
    set_keyframes()
    
    pass

main()

'''
# Insets keyframe at 0. That data path 'co' stands for coordinate
cube_vert_edited.data.vertices[5].keyframe_insert('co', frame = 0)

# Transfer the whole coordinate value tuple into x, y, z variables
x, y, z = cube_vert_edited.data.vertices[5].co

# Perform arithmetic on the values
cube_vert_edited.data.vertices[5].co = (x + 3, y, z)

# Insets keyframe at 50. That data path 'co' stands for coordinate
cube_vert_edited.data.vertices[5].keyframe_insert('co', frame = 50)

# Directly change just one coordinate value
cube_vert_edited.data.vertices[5].co.z = 3

# Insets keyframe at 100. That data path 'co' stands for coordinate
cube_vert_edited.data.vertices[5].keyframe_insert('co', frame = 100)
'''