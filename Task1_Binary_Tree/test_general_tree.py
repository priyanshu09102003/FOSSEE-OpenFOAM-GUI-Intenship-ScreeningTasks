"""
Test script for General Tree (Bonus Feature)
This demonstrates the n-ary tree implementation.
"""

from binary_tree_package.general_tree import *

if __name__ == "__main__":
    print("=" * 60)
    print("BONUS FEATURE: GENERAL TREE (N-ARY TREE)")
    print("=" * 60)
    print()
    
    # Test 1: Create a simple general tree
    print("=" * 60)
    print("TEST 1: Creating a General Tree with Multiple Children")
    print("=" * 60)
    
    # Create a family tree example
    root = GeneralNode("Grandparent")
    
    # Add three children (parents)
    parent1 = add_child_direct(root, "Parent 1")
    parent2 = add_child_direct(root, "Parent 2")
    parent3 = add_child_direct(root, "Parent 3")
    
    # Add children to Parent 1 (two children)
    add_child_direct(parent1, "Child 1.1")
    add_child_direct(parent1, "Child 1.2")
    
    # Add children to Parent 2 (three children)
    add_child_direct(parent2, "Child 2.1")
    add_child_direct(parent2, "Child 2.2")
    add_child_direct(parent2, "Child 2.3")
    
    # Add child to Parent 3 (one child)
    add_child_direct(parent3, "Child 3.1")
    
    print("Family Tree:")
    print_general_tree(root)
    print()
    
    # Test 2: Add node by path
    print("=" * 60)
    print("TEST 2: Adding Node by Path")
    print("=" * 60)
    
    tree = GeneralNode(1)
    add_child_direct(tree, 2)
    add_child_direct(tree, 3)
    add_child_direct(tree, 4)
    
    # Add child to the first child (index 0)
    add_child_by_path(tree, [0], 5)
    add_child_by_path(tree, [0], 6)
    
    # Add child to the second child (index 1)
    add_child_by_path(tree, [1], 7)
    
    print("Tree structure:")
    print_general_tree(tree)
    print()
    
    # Test 3: Edit node value
    print("=" * 60)
    print("TEST 3: Editing Node Values")
    print("=" * 60)
    print("Before editing:")
    print_general_tree(tree)
    
    print("\nEditing value 7 to 77:")
    edit_general_node_value(tree, 7, 77)
    
    print("After editing:")
    print_general_tree(tree)
    print()
    
    # Test 4: YAML Integration
    print("=" * 60)
    print("TEST 4: YAML Integration for General Tree")
    print("=" * 60)
    
    # Write to YAML
    yaml_output = "general_tree_output.yaml"
    print(f"Writing tree to '{yaml_output}'...")
    write_general_tree_to_yaml(root, yaml_output)
    
    # Read from YAML
    print(f"\nReading tree back from '{yaml_output}':")
    yaml_tree = build_general_tree_from_yaml(yaml_output)
    if yaml_tree:
        print_general_tree(yaml_tree)
    print()
    
    # Test 5: Create a more complex organizational tree
    print("=" * 60)
    print("TEST 5: Complex Organizational Tree")
    print("=" * 60)
    
    ceo = GeneralNode("CEO")
    
    # Direct reports to CEO
    cto = add_child_direct(ceo, "CTO")
    cfo = add_child_direct(ceo, "CFO")
    coo = add_child_direct(ceo, "COO")
    
    # Engineering team under CTO
    add_child_direct(cto, "Engineering Manager 1")
    add_child_direct(cto, "Engineering Manager 2")
    eng_mgr3 = add_child_direct(cto, "Engineering Manager 3")
    
    # Team under Engineering Manager 3
    add_child_direct(eng_mgr3, "Senior Engineer 1")
    add_child_direct(eng_mgr3, "Senior Engineer 2")
    add_child_direct(eng_mgr3, "Junior Engineer 1")
    
    # Finance team under CFO
    add_child_direct(cfo, "Accountant 1")
    add_child_direct(cfo, "Accountant 2")
    
    # Operations team under COO
    ops_mgr = add_child_direct(coo, "Operations Manager")
    add_child_direct(ops_mgr, "Operations Specialist 1")
    add_child_direct(ops_mgr, "Operations Specialist 2")
    
    print("Company Organizational Structure:")
    print_general_tree(ceo)
    print()
    
    # Test 6: Find node
    print("=" * 60)
    print("TEST 6: Finding a Node")
    print("=" * 60)
    
    found = find_node(ceo, "Engineering Manager 3")
    if found:
        print(f"Found node with value: {found.value}")
        print(f"Number of direct reports: {len(found.children)}")
        print("Direct reports:")
        for child in found.children:
            print(f"  - {child.value}")
    print()
    
    print("=" * 60)
    print("BONUS FEATURE TESTS COMPLETED SUCCESSFULLY!")
    print("=" * 60)
