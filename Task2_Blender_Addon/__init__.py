"""
Blender Addon for Cube Array Generation and Mesh Merging
FOSSEE OpenFOAM GUI Internship - Screening Task 2

This addon provides following features:
- Feature Set 1: Generate N cubes in a 2D array with collision detection
- Feature Set 2: Merge meshes with common faces
"""

bl_info = {
    "name": "FOSSEE Cube Array Generator",
    "author": "Priyanshu Paul",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > FOSSEE Tools",
    "description": "Generate cube arrays and merge meshes with common faces",
    "category": "Object",
}

import bpy
import bmesh
import math
from mathutils import Vector


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_optimal_grid_dimensions(n):
    """
    Calculate optimal m x n grid dimensions for n cubes.
    Tries to make the grid as square as possible.
    
    Args:
        n: Total number of cubes
    
    Returns:
        tuple: (rows, cols) dimensions
    """
    if n <= 0:
        return (0, 0)
    
    # Try to make it as square as possible
    sqrt_n = int(math.sqrt(n))
    
    # Start from square root and work outward
    for cols in range(sqrt_n, n + 1):
        if n % cols == 0:
            rows = n // cols
            return (rows, cols)
    
    # If no perfect division, use ceiling
    cols = sqrt_n + 1
    rows = math.ceil(n / cols)
    return (rows, cols)


def check_collision(location, existing_cubes, cube_size=1.0, spacing=0.1):
    """
    Check if a cube at the given location would collide with existing cubes.
    
    Args:
        location: Vector location to check
        existing_cubes: List of existing cube objects
        cube_size: Size of the cube
        spacing: Minimum spacing between cubes
    
    Returns:
        bool: True if collision detected, False otherwise
    """
    min_distance = cube_size + spacing
    
    for cube in existing_cubes:
        distance = (Vector(cube.location) - location).length
        if distance < min_distance:
            return True
    
    return False


def find_safe_location(row, col, cube_size, spacing, existing_cubes, max_attempts=100):
    """
    Find a safe location for a cube, avoiding collisions.
    
    Args:
        row: Target row
        col: Target column
        cube_size: Size of the cube
        spacing: Spacing between cubes
        existing_cubes: List of existing cubes
        max_attempts: Maximum attempts to find safe location
    
    Returns:
        Vector: Safe location or None if not found
    """
    base_x = col * (cube_size + spacing)
    base_y = row * (cube_size + spacing)
    base_location = Vector((base_x, base_y, 0))
    
    # Try the base location first
    if not check_collision(base_location, existing_cubes, cube_size, spacing):
        return base_location
    
    # Try spiral pattern outward
    for attempt in range(1, max_attempts):
        offset = attempt * spacing
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            test_location = Vector((
                base_x + offset * math.cos(rad),
                base_y + offset * math.sin(rad),
                0
            ))
            if not check_collision(test_location, existing_cubes, cube_size, spacing):
                return test_location
    
    return None


def get_all_scene_cubes():
    """Get all cube objects in the scene (from mesh objects)."""
    return [obj for obj in bpy.context.scene.objects 
            if obj.type == 'MESH' and obj.data.name.startswith('Cube')]


def find_common_faces(mesh1, mesh2, tolerance=0.0001):
    """
    Find faces that are common between two meshes (overlapping faces).
    
    Args:
        mesh1: First mesh object
        mesh2: Second mesh object
        tolerance: Distance tolerance for considering faces as overlapping
    
    Returns:
        tuple: (common_faces_mesh1_indices, common_faces_mesh2_indices)
    """
    # Convert mesh data to world space
    mesh1_faces = []
    for face in mesh1.data.polygons:
        center = mesh1.matrix_world @ face.center
        normal = mesh1.matrix_world.to_3x3() @ face.normal
        mesh1_faces.append((center, normal, face.index))
    
    mesh2_faces = []
    for face in mesh2.data.polygons:
        center = mesh2.matrix_world @ face.center
        normal = mesh2.matrix_world.to_3x3() @ face.normal
        mesh2_faces.append((center, normal, face.index))
    
    common_mesh1 = []
    common_mesh2 = []
    
    # Check for overlapping faces
    for i, (center1, normal1, idx1) in enumerate(mesh1_faces):
        for j, (center2, normal2, idx2) in enumerate(mesh2_faces):
            # Check if centers are close
            distance = (center1 - center2).length
            
            # Check if normals are opposite (faces pointing at each other)
            normal_dot = normal1.dot(normal2)
            
            if distance < tolerance and normal_dot < -0.9:  # Opposite normals
                common_mesh1.append(idx1)
                common_mesh2.append(idx2)
    
    return (list(set(common_mesh1)), list(set(common_mesh2)))


# ============================================================================
# OPERATORS
# ============================================================================

class FOSSEE_OT_GenerateCubes(bpy.types.Operator):
    """Generate N cubes in a 2D array pattern"""
    bl_idname = "fossee.generate_cubes"
    bl_label = "Generate Cube Array"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        props = context.scene.fossee_props
        n = props.cube_count
        
        # Validate input
        if n <= 0:
            self.report({'ERROR'}, "Number must be greater than 0")
            return {'CANCELLED'}
        
        if n > 20:
            self.report({'ERROR'}, "The number is out of range")
            return {'CANCELLED'}
        
        # Calculate grid dimensions
        rows, cols = get_optimal_grid_dimensions(n)
        
        # Get existing cubes if collision avoidance is enabled
        existing_cubes = get_all_scene_cubes() if props.avoid_overlap else []
        
        # Create collection if needed
        collection_name = "FOSSEE_Cubes"
        if collection_name not in bpy.data.collections:
            collection = bpy.data.collections.new(collection_name)
            context.scene.collection.children.link(collection)
        else:
            collection = bpy.data.collections[collection_name]
        
        cube_size = 1.0
        spacing = 0.2
        cubes_created = 0
        
        # Generate cubes
        for i in range(n):
            row = i // cols
            col = i % cols
            
            # Find safe location
            if props.avoid_overlap and existing_cubes:
                location = find_safe_location(row, col, cube_size, spacing, existing_cubes)
                if location is None:
                    self.report({'WARNING'}, 
                              f"Could not place cube {i+1} without collision, skipping")
                    continue
            else:
                location = Vector((
                    col * (cube_size + spacing),
                    row * (cube_size + spacing),
                    0
                ))
            
            # Create cube
            bpy.ops.mesh.primitive_cube_add(size=cube_size, location=location)
            cube = context.active_object
            cube.name = f"Cube_{cubes_created + 1}"
            
            # Move to collection
            for coll in cube.users_collection:
                coll.objects.unlink(cube)
            collection.objects.link(cube)
            
            # Add to existing cubes list
            if props.avoid_overlap:
                existing_cubes.append(cube)
            
            cubes_created += 1
        
        self.report({'INFO'}, 
                   f"Created {cubes_created} cubes in {rows}x{cols} array")
        return {'FINISHED'}


class FOSSEE_OT_DeleteSelected(bpy.types.Operator):
    """Delete selected cubes"""
    bl_idname = "fossee.delete_selected"
    bl_label = "Delete Selected Cubes"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        selected = context.selected_objects
        
        if not selected:
            self.report({'WARNING'}, "No objects selected")
            return {'CANCELLED'}
        
        count = len(selected)
        bpy.ops.object.delete()
        
        self.report({'INFO'}, f"Deleted {count} object(s)")
        return {'FINISHED'}


class FOSSEE_OT_MergeMeshes(bpy.types.Operator):
    """Merge selected meshes with common faces"""
    bl_idname = "fossee.merge_meshes"
    bl_label = "Merge Selected Meshes"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        selected = [obj for obj in context.selected_objects if obj.type == 'MESH']
        
        if len(selected) < 2:
            self.report({'ERROR'}, "Select at least 2 mesh objects to merge")
            return {'CANCELLED'}
        
        # Check for common faces between all pairs
        merge_candidates = []
        for i in range(len(selected)):
            for j in range(i + 1, len(selected)):
                mesh1 = selected[i]
                mesh2 = selected[j]
                
                common1, common2 = find_common_faces(mesh1, mesh2)
                
                if common1 and common2:
                    merge_candidates.append((mesh1, mesh2, common1, common2))
        
        if not merge_candidates:
            self.report({'ERROR'}, 
                       "Selected meshes do not have common faces. "
                       "Meshes must be touching to merge.")
            return {'CANCELLED'}
        
        # Perform merge
        # Deselect all
        bpy.ops.object.select_all(action='DESELECT')
        
        # Select all meshes to merge
        for obj in selected:
            obj.select_set(True)
        
        # Set active object
        context.view_layer.objects.active = selected[0]
        
        # Join objects
        bpy.ops.object.join()
        merged_obj = context.active_object
        
        # Enter edit mode to clean up
        bpy.ops.object.mode_set(mode='EDIT')
        
        # Remove doubles (merge overlapping vertices)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles(threshold=0.0001)
        
        # Delete internal faces
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_interior_faces()
        bpy.ops.mesh.delete(type='FACE')
        
        # Back to object mode
        bpy.ops.object.mode_set(mode='OBJECT')
        
        self.report({'INFO'}, 
                   f"Merged {len(selected)} meshes successfully")
        return {'FINISHED'}


# ============================================================================
# PROPERTIES
# ============================================================================

class FOSSEEProperties(bpy.types.PropertyGroup):
    """Properties for FOSSEE addon"""
    
    cube_count: bpy.props.IntProperty(
        name="Number of Cubes",
        description="Number of cubes to generate (max 20)",
        default=4,
        min=1,
        max=50  # Allow > 20 to trigger error message
    )
    
    avoid_overlap: bpy.props.BoolProperty(
        name="Avoid Overlap",
        description="Avoid placing cubes on existing objects",
        default=True
    )


# ============================================================================
# UI PANEL
# ============================================================================

class FOSSEE_PT_MainPanel(bpy.types.Panel):
    """Main panel for FOSSEE tools"""
    bl_label = "FOSSEE Cube Tools"
    bl_idname = "FOSSEE_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'FOSSEE Tools'
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.fossee_props
        
        # Feature Set 1
        box = layout.box()
        box.label(text="Feature Set 1: Cube Array", icon='MESH_CUBE')
        
        box.prop(props, "cube_count")
        box.prop(props, "avoid_overlap")
        
        box.operator("fossee.generate_cubes", icon='ADD')
        box.operator("fossee.delete_selected", icon='TRASH')
        
        # Feature Set 2
        box = layout.box()
        box.label(text="Feature Set 2: Mesh Merging", icon='MOD_BOOLEAN')
        
        box.label(text="Select 2+ meshes with common faces")
        box.operator("fossee.merge_meshes", icon='MODIFIER')


# ============================================================================
# REGISTRATION
# ============================================================================

classes = (
    FOSSEEProperties,
    FOSSEE_OT_GenerateCubes,
    FOSSEE_OT_DeleteSelected,
    FOSSEE_OT_MergeMeshes,
    FOSSEE_PT_MainPanel,
)


def register():
    """Register addon classes and properties"""
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.fossee_props = bpy.props.PointerProperty(type=FOSSEEProperties)
    
    print("FOSSEE Cube Array Addon registered successfully")


def unregister():
    """Unregister addon classes and properties"""
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    del bpy.types.Scene.fossee_props
    
    print("FOSSEE Cube Array Addon unregistered")


if __name__ == "__main__":
    register()
