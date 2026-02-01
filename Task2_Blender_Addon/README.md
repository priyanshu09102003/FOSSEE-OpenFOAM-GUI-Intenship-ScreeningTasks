# FOSSEE Blender Addon - Cube Array Generator and Mesh Merger

A Blender addon for generating cube arrays and merging meshes with common faces.

## Features Implemented

### ✅ Feature Set 1: Cube Array Generation
1. **UI Panel with Input Box** - Enter number N (natural number < 20)
2. **Range Validation** - Pop-up error if N > 20: "The number is out of range"
3. **2D Array Distribution** - Distributes N cubes (side=1) in optimal m×n grid
4. **Separate Collection** - Cubes organized in "FOSSEE_Cubes" collection
5. **Delete Selected** - Button to delete selected cubes
6. **Overlap Avoidance** - Optional feature to avoid placing cubes on existing objects

### ✅ Feature Set 2: Mesh Merging
1. **Merge Button** - Merges selected meshes into single mesh
2. **Common Face Detection** - Automatically detects meshes with shared faces
3. **Intelligent Merging** - Merges common vertices and deletes interior faces
4. **Validation** - Shows error if selected meshes don't have common faces

## Installation Instructions

### Prerequisites
- **Blender 3.0 or higher** (Download from https://www.blender.org/download/)
- Works on Windows, Mac, and Linux

### Step-by-Step Installation

#### Method 1: Install as ZIP (Recommended)

1. **Locate the addon file**
   - Find `fossee_blender_addon.zip` (or create it - see below)

2. **Open Blender**
   - Launch Blender application

3. **Go to Preferences**
   - Click `Edit` → `Preferences` (or press `Ctrl+Alt+U` / `Cmd+,` on Mac)

4. **Install Addon**
   - Click the `Add-ons` tab
   - Click `Install...` button at the top
   - Navigate to and select `fossee_blender_addon.zip`
   - Click `Install Add-on`

5. **Enable the Addon**
   - Search for "FOSSEE" in the search box
   - Check the checkbox next to "Object: FOSSEE Cube Array Generator"
   - The addon is now active!

#### Method 2: Install Manually

1. **Find Blender's addon directory**
   - **Windows**: `C:\Users\[YourUsername]\AppData\Roaming\Blender Foundation\Blender\[Version]\scripts\addons\`
   - **Mac**: `/Users/[YourUsername]/Library/Application Support/Blender/[Version]/scripts/addons/`
   - **Linux**: `~/.config/blender/[Version]/scripts/addons/`

2. **Create addon folder**
   - Create a folder named `fossee_cube_tools`

3. **Copy the file**
   - Copy `__init__.py` into the `fossee_cube_tools` folder

4. **Restart Blender**

5. **Enable the addon**
   - Go to `Edit` → `Preferences` → `Add-ons`
   - Search for "FOSSEE"
   - Enable the addon

## How to Create ZIP File for Installation

```bash
# If you have the addon folder:
cd blender_addon
zip -r fossee_blender_addon.zip __init__.py

# Or rename the folder first:
mv blender_addon fossee_cube_tools
zip -r fossee_blender_addon.zip fossee_cube_tools/
```

## Usage Guide

### Accessing the Panel

1. Open Blender
2. In the 3D Viewport, press `N` to open the sidebar
3. Look for the **"FOSSEE Tools"** tab
4. Click on it to see the panel

### Feature Set 1: Generating Cube Arrays

1. **Enter Number of Cubes**
   - In the "Number of Cubes" field, enter a value (1-20)
   - Values > 20 will show error: "The number is out of range"

2. **Enable/Disable Overlap Avoidance** (Optional)
   - Check "Avoid Overlap" to prevent placing cubes on existing objects
   - Uncheck to allow placement anywhere

3. **Generate Cubes**
   - Click "Generate Cube Array" button
   - Cubes will be created in an optimal 2D grid pattern
   - All cubes are added to "FOSSEE_Cubes" collection

4. **Delete Cubes**
   - Select cubes in the viewport (Right-click or Box select with `B`)
   - Click "Delete Selected Cubes" button

### Feature Set 2: Merging Meshes

1. **Position Meshes**
   - Move cubes so they share at least one common face (touching faces)
   - You can use `G` to grab/move objects in Blender

2. **Select Meshes to Merge**
   - Select 2 or more mesh objects (Shift+Right-click to multi-select)
   - Meshes MUST have at least one common face

3. **Merge**
   - Click "Merge Selected Meshes" button
   - The addon will:
     - Detect common faces
     - Merge the meshes into one
     - Remove duplicate vertices
     - Delete interior faces

4. **Result**
   - You'll have a single merged mesh
   - Interior faces are removed automatically

## Examples

### Example 1: Generate 6 Cubes

```
1. Set "Number of Cubes" to 6
2. Click "Generate Cube Array"
Result: 2×3 or 3×2 grid of cubes
```

### Example 2: Merge Two Adjacent Cubes

```
1. Generate 2 cubes
2. Position them so they share a face (touching)
3. Select both cubes (Shift+Right-click)
4. Click "Merge Selected Meshes"
Result: Single merged cube with shared face removed
```

### Example 3: Test Range Validation

```
1. Set "Number of Cubes" to 25
2. Click "Generate Cube Array"
Result: Error message "The number is out of range"
```

## Technical Details

### Grid Calculation
- The addon calculates optimal m×n dimensions
- Tries to create square-ish grids
- Example: 12 cubes → 3×4 or 4×3 grid

### Collision Detection
- When "Avoid Overlap" is enabled:
  - Checks distance to existing cubes
  - Uses spiral search pattern for safe placement
  - Skips cube if no safe position found

### Mesh Merging Algorithm
1. Converts face centers to world space
2. Checks for overlapping face centers
3. Verifies normals are opposite (facing each other)
4. Joins objects
5. Removes duplicate vertices
6. Deletes interior faces

## Troubleshooting

### Addon doesn't appear in preferences
- Make sure you installed the correct `.zip` file
- Try Method 2 (manual installation)
- Check Blender version (need 3.0+)

### Can't find FOSSEE Tools tab
- Press `N` in 3D viewport to show sidebar
- Look in the sidebar tabs (might be on the right edge)

### Merge doesn't work
- Make sure meshes are actually touching (shared face)
- Select at least 2 mesh objects
- Try moving cubes closer together

### "Out of range" error with small numbers
- Check that you entered a number ≤ 20
- The field allows numbers > 20 to test the validation

### Overlap avoidance not working
- Make sure "Avoid Overlap" checkbox is enabled
- Try with fewer cubes
- May skip cubes if no space available

## File Structure

```
fossee_cube_tools/
└── __init__.py          # Main addon code
```

## Credits

Created for FOSSEE OpenFOAM GUI Internship - Spring 2026
Screening Task 2: Blender Addon Development

## License

MIT License - Free to use and modify
