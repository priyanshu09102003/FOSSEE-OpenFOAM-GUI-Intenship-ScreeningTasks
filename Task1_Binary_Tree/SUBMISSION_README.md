# FOSSEE OpenFOAM GUI Internship - Screening Task Submission

**Task:** Binary Tree Implementation and YAML Integration

**Submitted by:** [Priyanshu Paul]

---

##  Task Completion Status

###  Feature Set 1: Binary Tree Operations (COMPLETED)
-  Node class for creating binary trees
-  Helper function to create new binary tree
-  Helper function to add nodes to existing binary tree using path notation
-  Helper function to delete nodes (single or entire tree)
-  Helper function to print tree (entire tree or specific range)
-  Helper function to edit node values

###  Feature Set 2: YAML Integration (COMPLETED)
-  Function to parse YAML file and generate tree
-  Function to write binary tree data to YAML file

###  Bonus Feature: General Tree (N-ary Tree) (COMPLETED)
-  Modified Node class supporting N children per node
-  All helper functions adapted for general tree
-  YAML integration for general trees
-  Additional helper functions (find_node, add_child_direct)

---

##  Project Structure

```
binary_tree_package/
├── binary_tree_package/          # Main package
│   ├── __init__.py               # Binary tree implementation
│   └── general_tree.py           # Bonus: General tree implementation
├── main.py                       # Test script (as per task requirements)
├── test_general_tree.py          # Bonus feature test script
├── test.yaml                     # Sample YAML file (as provided in task)
├── setup.py                      # Package installation configuration
├── requirements.txt              # Dependencies
├── README.md                     # Package documentation
└── SUBMISSION_README.md          # This file
```

---

##  Installation and Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- PyYAML >= 5.1

### Step 2: Install the Package

**Option A: Development Mode (Recommended for testing)**
```bash
pip install -e .
```

**Option B: Regular Installation**
```bash
pip install .
```

---

##  Running the Tests

### Test 1: Main Binary Tree Features (As per Task Requirements)

```bash
python main.py
```

**Expected Output:**
- Test 1: Basic tree creation
- Test 2: Adding nodes by path
- Test 3: Building tree from YAML
- Test 4: Editing node values
- Test 5: Writing tree to YAML
- Test 6: Printing nodes in range
- Test 7: Deleting specific nodes
- Test 8: Deleting entire tree

### Test 2: Bonus Feature - General Tree

```bash
python test_general_tree.py
```

**Expected Output:**
- Demonstrates n-ary tree with multiple children per node
- Shows YAML integration for general trees
- Complex organizational tree example

---

##  Code Examples

### Example 1: Basic Binary Tree (From Task Requirements)

```python
from binary_tree_package import *

# Create tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Print tree
print_tree(root)
```

**Output:**
```
Root:1
 L---2
  L---4
  R---5
 R---3
```

### Example 2: Adding Nodes by Path

```python
root = Node(10)

# Add nodes using L (left) and R (right) notation
add_node_by_path(root, "L", 5)
add_node_by_path(root, "R", 15)
add_node_by_path(root, "LL", 3)
add_node_by_path(root, "LR", 7)
add_node_by_path(root, "RL", 12)
add_node_by_path(root, "RR", 18)

print_tree(root)
```

### Example 3: YAML Integration

**test.yaml:**
```yaml
value: 10
left:
  value: 5
  left:
    value: 3
  right:
    value: 7
right:
  value: 15
  right:
    value: 18
```

**Python code:**
```python
# Build from YAML
yaml_tree_root = build_tree_from_yaml("test.yaml")
print_tree(yaml_tree_root)

# Write to YAML
write_tree_to_yaml(yaml_tree_root, "output.yaml")
```

### Example 4: General Tree

```python
from binary_tree_package.general_tree import *

# Create organizational tree
ceo = GeneralNode("CEO")
cto = add_child_direct(ceo, "CTO")
cfo = add_child_direct(ceo, "CFO")

# Add multiple reports under CTO
add_child_direct(cto, "Eng Manager 1")
add_child_direct(cto, "Eng Manager 2")
add_child_direct(cto, "Eng Manager 3")

print_general_tree(ceo)
```

---

##  Key Features & Implementation Details

### 1. **Comprehensive Error Handling**
- File not found errors for YAML operations
- Invalid path errors for node addition
- Graceful handling of None values

### 2. **Well-Documented Code**
- Detailed docstrings for all functions
- Type hints for better code clarity
- Comments explaining complex logic

### 3. **Flexible API**
- Multiple ways to manipulate trees
- Support for both binary and n-ary trees
- Intuitive function names

### 4. **YAML Integration**
- Seamless conversion between tree and YAML
- Preserves tree structure
- Human-readable format

### 5. **Testing**
- Comprehensive test scripts
- Covers all required features
- Demonstrates edge cases

---


##  Technical Details

### Dependencies
- **PyYAML**: For YAML file parsing and generation
- **Python Standard Library**: typing, etc.

### Design Patterns Used
- **Recursive Traversal**: For tree operations
- **Type Hints**: For better code documentation
- **Module Organization**: Separate files for binary and general trees

### Code Quality
- Clean, readable code
- Consistent naming conventions
- Proper error handling
- Comprehensive documentation

---

##  Test Results

All tests pass successfully:

```
 Binary Tree Creation
 Node Addition by Path
 YAML Parsing
 YAML Writing
 Node Editing
 Node Deletion
 Tree Printing
 Range Printing
 General Tree 
```

---

##  Learning Outcomes

Through this task, I demonstrated:

1. **Data Structures**: Deep understanding of tree structures
2. **Python Programming**: Object-oriented design, recursion
3. **File I/O**: YAML parsing and generation
4. **Package Development**: Creating installable Python packages
5. **Testing**: Comprehensive test coverage
6. **Documentation**: Clear, professional documentation

---

## 📬 Contact Information

**Name:** [Priyanshu Paul]
**Email:** [paulpriyanshu704@gmail.com]
**GitHub:** [github.com/priyanshu09102003]

---

##  Acknowledgments

This project was completed as part of the FOSSEE OpenFOAM GUI Internship screening process at IIT Bombay.

---

##  License

MIT License - Feel free to use and modify as needed.

---

**Submission Date:** 2nd February 2026


