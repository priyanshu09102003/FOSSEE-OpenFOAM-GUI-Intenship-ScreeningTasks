# FOSSEE OpenFOAM GUI Internship - Complete Screening Task Submission

**Submitted by:** [Priyanshu Paul]  
**Email:** [paulpriyanshu704@gmail.com]  
**Institution:** [Vellore Institute of Technology, Bhopal Campus]  
**Program:** [B.E./B.Tech/M.Tech in Computer Science Engineering(Artificial Intelligence and Machine Learning)]

---

##  Submission Overview

This submission contains solutions for **BOTH required tasks** of the OpenFOAM GUI Internship screening:

###  Task 1: Binary Tree Implementation and YAML Integration
- Complete binary tree package with all required features
- YAML file integration for persistence
- General n-ary tree implementation
- Pip-installable Python package

### Task 2: Blender Addon Development
- Cube array generator with UI panel
- Input validation and error handling
- Mesh merging with common face detection
- **Bonus:** Collision avoidance system

---

##  Folder Structure

```
thisRepository/
├── README.md                          # This file
├── Task1_Binary_Tree/                 # Task 1 solution
│   ├── binary_tree_package/
│   │   ├── __init__.py               # Main binary tree code
│   │   └── general_tree.py           # Bonus: general tree
│   ├── main.py                       # Test script
│   ├── test_general_tree.py          # Other tests
│   ├── test.yaml                     # Sample YAML
│   ├── setup.py                      # Package setup
│   ├── requirements.txt              # Dependencies
│   ├── README.md                     # Task 1 documentation
│
│
└── Task2_Blender_Addon/               # Task 2 solution
    ├── __init__.py                   # Blender addon code
    ├── README.md                     # Installation & usage

```

---

##  Quick Start Guide

### Task 1: Binary Tree

```bash
cd Task1_Binary_Tree

# Install dependencies
pip install -r requirements.txt

# Install package
pip install -e .

# Run tests
python main.py

# Run feature tests
python test_general_tree.py
```

**Expected Output:** All 8 tests pass successfully

### Task 2: Blender Addon

1. Install Blender 3.0+ from https://www.blender.org/download/
2. Open Blender
3. Go to Edit → Preferences → Add-ons
4. Click "Install..." and select `Task2_Blender_Addon/__init__.py`
5. Enable "FOSSEE Cube Array Generator"
6. Press `N` in 3D viewport to access FOSSEE Tools panel

**See:** `Task2_Blender_Addon/TESTING_GUIDE.md` for detailed testing steps

---

## Features Implemented

### Task 1 Features

#### Required Features (100% Complete):
1. Node class for binary trees
2. Create binary tree function
3. Add node by path (L/R notation)
4. Delete node/tree functions
5. Print tree visualization
6. Edit node values
7. Parse YAML to tree
8. Write tree to YAML
9. Pip-installable package
10. Requirements.txt included

#### Other Features:
1. General n-ary tree (unlimited children)
2. Additional utility functions
3. Comprehensive error handling
4. Type hints throughout
5. Professional documentation

### Task 2 Features

#### Feature Set 1 (100% Complete):
1. UI Panel with input box for N (natural number)
2. Validation: Error popup if N > 20
3. Generate N cubes in optimal 2D array
4. Cubes organized in separate collection
5. Delete selected cubes button
6. Collision avoidance system

#### Feature Set 2 (100% Complete):
1. Merge selected meshes button
2. Common face detection algorithm
3. Merge common vertices
4. Delete interior faces
5. Error handling for non-adjacent meshes

---

## Testing Results

### Task 1: Binary Tree
-  All core features tested and working
-  Bonus general tree tested and working
-  YAML integration verified
-  Package installation successful
-  Output matches expected format

### Task 2: Blender Addon
-  UI panel appears correctly
-  Input validation works (N > 20 shows error)
-  Cube generation in optimal grids
-  Delete functionality works
-  Mesh merging works for adjacent cubes
-  Error shown for non-adjacent meshes
-  Collision avoidance works

---

##  Skills Demonstrated

### Programming Skills:
-  Python (advanced level)
-  Object-oriented programming
-  Data structures (trees, graphs)
-  Algorithms (recursion, traversal)
-  API development (Blender Python API)

### Software Engineering:
-  Package development (pip install)
-  Documentation (README, docstrings)
-  Version control (Git-ready structure)
-  Testing (comprehensive test scripts)
-  Error handling
-  Code organization

### Domain Knowledge:
-  Binary/n-ary tree operations
-  File I/O (YAML parsing)
-  3D geometry calculations
-  GUI development
-  Mesh operations

---

##  Implementation Highlights

### Task 1: Binary Tree

**Key Algorithms:**
- Recursive tree traversal (pre-order, in-order, post-order)
- Path-based node insertion using string notation
- YAML serialization/deserialization
- Range-based tree printing

**Code Quality:**
- Type hints for all functions
- Comprehensive docstrings
- Modular code organization
- Professional error messages

### Task 2: Blender Addon

**Key Algorithms:**
- Optimal grid dimension calculation (square-ish layouts)
- Collision detection with spiral search pattern
- Common face detection in 3D space
- Mesh merging with duplicate removal

**Technical Features:**
- Blender operator classes
- Property groups for UI
- BMesh operations for geometry
- World-space transformations

---

##  Approach & Methodology

### Task Selection Strategy:
I chose to complete both tasks to demonstrate comprehensive skills in:
1. Pure algorithmic problem-solving (Task 1)
2. GUI and 3D visualization (Task 2)

### Development Process:
1. **Planning:** Analyzed requirements carefully
2. **Implementation:** Built core features first
3. **Enhancement:** Added bonus features
4. **Testing:** Comprehensive testing for edge cases
5. **Documentation:** Clear instructions and examples

### Problem-Solving:
- **Task 1:** Focused on clean, recursive algorithms and proper data structure design
- **Task 2:** Emphasized user experience, error handling, and geometric accuracy

---

##  Submission Contents

As per submission guidelines, this archive contains:

1.  **Task Solutions:**
   - Task1_Binary_Tree/ folder with complete solution
   - Task2_Blender_Addon/ folder with complete solution

2.  **Documentation:**
   - README.md files for each task
   - Installation instructions
   - Testing guides
   - Code comments

3.  **Required Files:**
   - requirements.txt (Task 1)
   - All source code
   - Test scripts
   - Sample data files

---

##  System Requirements

### Task 1:
- Python 3.7+
- PyYAML library
- Any operating system

### Task 2:
- Blender 3.0+ (4.0+ recommended)
- Windows/Mac/Linux
- 4GB+ RAM

---

##  Time Investment

- **Task 1:** ~4 hours 
- **Task 2:** ~5 hours 
- **Documentation:** ~2 hours
- **Testing:** ~2 hours
- **Total:** ~13 hours

---

##  Learning Outcomes

Through these tasks, I demonstrated:

1. **Technical Proficiency:** Strong Python skills, understanding of APIs
2. **Problem Solving:** Algorithmic thinking, optimization
3. **Software Engineering:** Clean code, documentation, testing
4. **Attention to Detail:** Met all requirements, added bonuses
5. **Communication:** Clear documentation and instructions

---

##  Additional Notes

### Why I'm Interested:
I am passionate about making complex scientific tools accessible through better software design. The FOSSEE mission aligns with my belief in open-source education.

### What I Hope to Learn:
- Advanced GUI development with Blender API
- CFD tool architecture
- Large-scale scientific software development
- Collaborative open-source workflows

### Commitment:
I am available for the full 6-month internship duration and can dedicate 20-25 hours per week to meaningful contributions.

---

## 📞 Contact Information

**Name:** [Priyanshu Paul]  
**Email:** [paulpriyanshu704@gmail.com]  
**Phone:** [+91-6900507916]  
**GitHub:** [github.com/priyanshu09102003]  
**LinkedIn:** [linkedin.com/in/priyanshu-paul-59221228a]

---
## 📄 License

MIT License - Free to use and modify for educational purposes.

---

**Submission Date:** [2nd February 2026]

**For:** FOSSEE OpenFOAM GUI Internship - Spring 2026

**Submitted to:** contact-cfd@fossee.in

---

Thank you for considering my application. I am excited about the opportunity to contribute to the FOSSEE project and look forward to discussing my submission further.

**Best regards,**  
[Priyanshu Paul]
