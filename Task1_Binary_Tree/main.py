"""
FOSSEEE - Binary Tree Package
This script demonstrates all features of the binary tree package.
"""

from binary_tree_package import *

if __name__ == "__main__":
    # Test 1: Creating a Basic tree and printing the values 
    print("=" * 60)
    print("TEST 1: Basic Tree Creation")
    print("=" * 60)
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print_tree(root)
    print()
    
    # Test 2: Creating a tree and adding nodes by path
    print("=" * 60)
    print("TEST 2: Creating Tree with add_node_by_path")
    print("=" * 60)
    root = Node(10)
    print("Initial tree:")
    print_tree(root)
    
    # Add the nodes
    print("\nAdding nodes:")
    add_node_by_path(root, "L", 5)
    add_node_by_path(root, "R", 15)
    add_node_by_path(root, "LL", 3)
    add_node_by_path(root, "LR", 7)
    add_node_by_path(root, "RL", 12)
    add_node_by_path(root, "RR", 18)
    
    print("\nTree after additions:")
    print_tree(root)
    print()
    
    # Test 3: Building the tree from YAML file
    print("=" * 60)
    print("TEST 3: Building Tree from YAML File")
    print("=" * 60)
    yaml_file = "test.yaml"
    print(f"Building tree from '{yaml_file}':")
    yaml_tree_root = build_tree_from_yaml(yaml_file)
    if yaml_tree_root:
        print("\nTree built from YAML:")
        print_tree(yaml_tree_root)
    else:
        print("Failed to build tree from YAML")
    print()
    
    # Test 4: Editing the node values
    print("=" * 60)
    print("TEST 4: Editing Node Values")
    print("=" * 60)
    print("Original tree:")
    print_tree(root)
    print("\nEditing value 7 to 8:")
    edit_node_value(root, 7, 8)
    print_tree(root)
    print()
    
    # Test 5: Writing the tree to YAML
    print("=" * 60)
    print("TEST 5: Writing Tree to YAML File")
    print("=" * 60)
    output_file = "output_tree.yaml"
    success = write_tree_to_yaml(root, output_file)
    if success:
        print(f"Successfully wrote tree to '{output_file}'")
        print("\nVerifying by reading it back:")
        verification_root = build_tree_from_yaml(output_file)
        if verification_root:
            print_tree(verification_root)
    else:
        print("Failed to write tree to YAML")
    print()
    
    # Test 6: Printing the tree range
    print("=" * 60)
    print("TEST 6: Print Nodes in Range")
    print("=" * 60)
    print("Tree:")
    print_tree(root)
    print("\nNodes with values between 5 and 15:")
    print_tree_range(root, 5, 15)
    print("\n")
    
    # Test 7: Deleting the node
    print("=" * 60)
    print("TEST 7: Deleting a Node")
    print("=" * 60)
    print("Tree before deletion:")
    print_tree(root)
    print("\nDeleting node with value 5:")
    root = delete_node(root, 5)
    print("Tree after deletion:")
    print_tree(root)
    print()
    
    # Test 8: Deleting the entire tree
    print("=" * 60)
    print("TEST 8: Deleting Entire Tree")
    print("=" * 60)
    test_root = Node(100)
    test_root.left = Node(50)
    test_root.right = Node(150)
    print("Tree before deletion:")
    print_tree(test_root)
    print("\nDeleting entire tree...")
    delete_tree(test_root)
    print("Tree deleted (all references cleared)")
    print()
    
    print("=" * 60)
    print("ALL TESTS COMPLETED SUCCESSFULLY!")
    print("=" * 60)
