# Testing Guide for FOSSEE Blender Addon

This guide will help you test the Blender addon step-by-step.

## Prerequisites

1. **Download Blender**
   - Go to https://www.blender.org/download/
   - Download Blender 3.6 or 4.0+ (latest LTS version)
   - Install it on your computer

2. **Install the Addon**
   - Follow instructions in README.md
   - Make sure the addon shows up in Preferences

---

## Test Sequence

### Test 1: Basic UI Functionality

**Goal:** Verify the panel appears correctly

**Steps:**
1. Open Blender (fresh start)
2. Press `N` to open right sidebar
3. Look for "FOSSEE Tools" tab
4. Click on it

**Expected Result:**
- ✅ Panel appears with two sections:
  - Feature Set 1: Cube Array
  - Feature Set 2: Mesh Merging
- ✅ Input field for "Number of Cubes"
- ✅ Checkbox for "Avoid Overlap"
- ✅ Three buttons visible

---

### Test 2: Generate Small Array (4 Cubes)

**Goal:** Test basic cube generation

**Steps:**
1. In "Number of Cubes" field, enter: `4`
2. Click "Generate Cube Array" button
3. Look at the 3D viewport

**Expected Result:**
- ✅ 4 cubes appear in a 2×2 grid
- ✅ Cubes are 1 unit in size
- ✅ Spaced evenly
- ✅ Collection "FOSSEE_Cubes" appears in Outliner (top-right)
- ✅ Info message: "Created 4 cubes in 2×2 array"

**Screenshot This!** 📸

---

### Test 3: Validate Range Error (N > 20)

**Goal:** Test error handling

**Steps:**
1. In "Number of Cubes" field, enter: `25`
2. Click "Generate Cube Array" button
3. Look at the top of the window for error message

**Expected Result:**
- ✅ Error popup appears
- ✅ Message reads: "The number is out of range"
- ✅ No cubes are created

**Screenshot This!** 📸

---

### Test 4: Generate Larger Array (12 Cubes)

**Goal:** Test optimal grid calculation

**Steps:**
1. Delete previous cubes: Select all (`A`), Delete (`X` → Delete)
2. In "Number of Cubes" field, enter: `12`
3. Click "Generate Cube Array" button

**Expected Result:**
- ✅ 12 cubes appear in 3×4 or 4×3 grid
- ✅ Grid is roughly square-shaped
- ✅ All cubes in FOSSEE_Cubes collection

**Screenshot This!** 📸

---

### Test 5: Delete Selected Cubes

**Goal:** Test delete functionality

**Steps:**
1. Select a few cubes:
   - Hold Shift and Right-click on cubes
   - OR press `B` for box select, drag around some cubes
2. Click "Delete Selected Cubes" button

**Expected Result:**
- ✅ Selected cubes disappear
- ✅ Remaining cubes stay in place
- ✅ Info message: "Deleted X object(s)"

---

### Test 6: Merge Two Adjacent Cubes

**Goal:** Test mesh merging with common face

**Steps:**
1. Delete all objects (`A` to select all, `X` to delete)
2. Generate 2 cubes (set N=2)
3. Move cubes so they touch:
   - Select one cube
   - Press `G` to grab/move
   - Move it to touch the other cube (faces aligned)
   - Press `Enter` to confirm
4. Select BOTH cubes (Shift+Right-click each one)
5. Click "Merge Selected Meshes" button

**Expected Result:**
- ✅ Two cubes merge into one object
- ✅ The shared interior face is removed
- ✅ Looks like a single rectangular block
- ✅ Info message: "Merged 2 meshes successfully"

**Screenshot This!** 📸

---

### Test 7: Merge Error (No Common Face)

**Goal:** Test error when meshes don't touch

**Steps:**
1. Delete all objects
2. Generate 2 cubes (they'll be separated)
3. Select both cubes (don't move them together)
4. Click "Merge Selected Meshes" button

**Expected Result:**
- ✅ Error message appears
- ✅ Message: "Selected meshes do not have common faces"
- ✅ Cubes remain separate

---

### Test 8: Overlap Avoidance

**Goal:** Test optional collision detection

**Steps:**
1. Delete all objects
2. Create a manual cube: Add → Mesh → Cube
3. Move it to position (0, 0, 0)
4. In addon panel:
   - Set "Number of Cubes" to 4
   - ✅ Enable "Avoid Overlap" checkbox
5. Click "Generate Cube Array"

**Expected Result:**
- ✅ New cubes avoid the existing cube
- ✅ Cubes placed in positions without collision
- ✅ May see warning if some cubes can't be placed

---

### Test 9: Merge Three Cubes

**Goal:** Test merging multiple meshes

**Steps:**
1. Delete all objects
2. Generate 3 cubes
3. Arrange them in a line, touching:
   ```
   [Cube1][Cube2][Cube3]
   ```
   - Use `G` to move cubes
   - Align them so they share faces
4. Select all 3 cubes
5. Click "Merge Selected Meshes"

**Expected Result:**
- ✅ All 3 cubes merge into one long block
- ✅ Interior faces removed
- ✅ Looks like a single 1×1×3 block


---

### Test 10: Maximum Valid Input (N = 20)

**Goal:** Test upper boundary

**Steps:**
1. Delete all objects
2. Set "Number of Cubes" to: `20`
3. Click "Generate Cube Array"

**Expected Result:**
- ✅ 20 cubes generated successfully
- ✅ Arranged in 4×5 or 5×4 grid
- ✅ No error message

---

## Blender Shortcuts Reference

- `N` - Toggle sidebar
- `A` - Select all
- `Alt+A` - Deselect all
- `G` - Grab/move selected object
- `X` - Delete menu
- `B` - Box select
- `Home` - Frame all objects
- `Shift+Right-click` - Add to selection
- `Middle Mouse` - Rotate view
- `Scroll Wheel` - Zoom

---

Good luck with testing! 
