"""
Binary Tree Package with YAML Integration
A comprehensive package for creating, manipulating, and persisting binary trees.
"""

import yaml
from typing import Optional, Any, List


class Node:
    """
    A Node class for creating binary trees.
    
    Attributes:
        value: The value stored in the node
        left: Reference to the left child node
        right: Reference to the right child node
    """
    
    def __init__(self, value: Any):
        """
        Initialize a new node.
        
        Args:
            value: The value to store in the node
        """
        self.value = value
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
    
    def __repr__(self):
        return f"Node({self.value})"


def create_binary_tree(value: Any) -> Node:
    """
    Create a new binary tree with a root node.
    
    Args:
        value: The value for the root node
        
    Returns:
        A new Node object as the root of the tree
    """
    return Node(value)


def add_node_by_path(root: Optional[Node], path: str, value: Any) -> bool:
    """
    Add a node to the binary tree using a path string.
    
    Args:
        root: The root node of the tree
        path: A string of 'L' and 'R' characters indicating the path
              (e.g., "LR" means left then right)
        value: The value for the new node
        
    Returns:
        True if node was added successfully, False otherwise
    """
    if root is None:
        return False
    
    if not path:
        return False
    
    current = root
    
    # Navigate to the parent position
    for i, direction in enumerate(path[:-1]):
        if direction == 'L':
            if current.left is None:
                print(f"Cannot add node: path broken at position {i}")
                return False
            current = current.left
        elif direction == 'R':
            if current.right is None:
                print(f"Cannot add node: path broken at position {i}")
                return False
            current = current.right
        else:
            print(f"Invalid direction '{direction}' in path")
            return False
    
    # Add the new node at the final position
    final_direction = path[-1]
    if final_direction == 'L':
        if current.left is not None:
            print(f"Warning: Overwriting existing left child with value {current.left.value}")
        current.left = Node(value)
        return True
    elif final_direction == 'R':
        if current.right is not None:
            print(f"Warning: Overwriting existing right child with value {current.right.value}")
        current.right = Node(value)
        return True
    else:
        print(f"Invalid final direction '{final_direction}'")
        return False


def delete_node(root: Optional[Node], value: Any) -> Optional[Node]:
    """
    Delete a node with the specified value from the binary tree.
    
    Args:
        root: The root node of the tree
        value: The value to delete
        
    Returns:
        The root of the modified tree
    """
    if root is None:
        return None
    
    # If this is the node to delete
    if root.value == value:
        # Node with no children
        if root.left is None and root.right is None:
            return None
        # Node with only right child
        if root.left is None:
            return root.right
        # Node with only left child
        if root.right is None:
            return root.left
        # Node with two children - replace with minimum value from right subtree
        min_node = _find_min(root.right)
        root.value = min_node.value
        root.right = delete_node(root.right, min_node.value)
        return root
    
    # Recursively delete from subtrees
    root.left = delete_node(root.left, value)
    root.right = delete_node(root.right, value)
    return root


def delete_tree(root: Optional[Node]) -> None:
    """
    Delete the entire binary tree.
    
    Args:
        root: The root node of the tree to delete
    """
    if root is None:
        return
    
    # Post-order traversal to delete all nodes
    delete_tree(root.left)
    delete_tree(root.right)
    root.left = None
    root.right = None


def _find_min(node: Node) -> Node:
    """Helper function to find the minimum value node in a tree."""
    current = node
    while current.left is not None:
        current = current.left
    return current


def print_tree(root: Optional[Node], prefix: str = "Root:", is_left: bool = False) -> None:
    """
    Print the binary tree in a visual format.
    
    Args:
        root: The root node of the tree
        prefix: Prefix string for formatting (used in recursion)
        is_left: Whether this is a left child (used in recursion)
    """
    if root is None:
        return
    
    print(f"{prefix}{root.value}")
    
    # Print children
    if root.left is not None or root.right is not None:
        if root.left is not None:
            print_tree(root.left, " L---", True)
        else:
            print(" L---None")
        
        if root.right is not None:
            print_tree(root.right, " R---", False)
        else:
            print(" R---None")


def print_tree_range(root: Optional[Node], min_value: Any, max_value: Any) -> None:
    """
    Print nodes in the tree within a specified value range.
    
    Args:
        root: The root node of the tree
        min_value: Minimum value to print
        max_value: Maximum value to print
    """
    if root is None:
        return
    
    # In-order traversal to print nodes in range
    print_tree_range(root.left, min_value, max_value)
    
    if min_value <= root.value <= max_value:
        print(root.value, end=" ")
    
    print_tree_range(root.right, min_value, max_value)


def edit_node_value(root: Optional[Node], old_value: Any, new_value: Any) -> bool:
    """
    Edit the value of a node in the binary tree.
    
    Args:
        root: The root node of the tree
        old_value: The current value to find
        new_value: The new value to set
        
    Returns:
        True if the value was found and updated, False otherwise
    """
    if root is None:
        return False
    
    if root.value == old_value:
        root.value = new_value
        return True
    
    # Search in left and right subtrees
    found_left = edit_node_value(root.left, old_value, new_value)
    found_right = edit_node_value(root.right, old_value, new_value)
    
    return found_left or found_right


def build_tree_from_yaml(yaml_file: str) -> Optional[Node]:
    """
    Build a binary tree from a YAML file.
    
    Args:
        yaml_file: Path to the YAML file
        
    Returns:
        The root node of the constructed tree, or None if file cannot be read
    """
    try:
        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)
        
        if data is None:
            return None
        
        return _build_tree_recursive(data)
    
    except FileNotFoundError:
        print(f"Error: File '{yaml_file}' not found")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None


def _build_tree_recursive(data: dict) -> Optional[Node]:
    """
    Helper function to recursively build tree from dictionary.
    
    Args:
        data: Dictionary containing node data
        
    Returns:
        The constructed node
    """
    if data is None:
        return None
    
    if not isinstance(data, dict):
        return None
    
    # Create the current node
    value = data.get('value')
    if value is None:
        return None
    
    node = Node(value)
    
    # Recursively build left and right subtrees
    left_data = data.get('left')
    if left_data is not None:
        node.left = _build_tree_recursive(left_data)
    
    right_data = data.get('right')
    if right_data is not None:
        node.right = _build_tree_recursive(right_data)
    
    return node


def write_tree_to_yaml(root: Optional[Node], yaml_file: str) -> bool:
    """
    Write a binary tree to a YAML file.
    
    Args:
        root: The root node of the tree
        yaml_file: Path to the output YAML file
        
    Returns:
        True if successful, False otherwise
    """
    try:
        tree_dict = _tree_to_dict(root)
        
        with open(yaml_file, 'w') as file:
            yaml.dump(tree_dict, file, default_flow_style=False, sort_keys=False)
        
        return True
    
    except Exception as e:
        print(f"Error writing to YAML file: {e}")
        return False


def _tree_to_dict(node: Optional[Node]) -> Optional[dict]:
    """
    Helper function to convert tree to dictionary format.
    
    Args:
        node: The node to convert
        
    Returns:
        Dictionary representation of the node and its children
    """
    if node is None:
        return None
    
    node_dict = {'value': node.value}
    
    if node.left is not None:
        node_dict['left'] = _tree_to_dict(node.left)
    
    if node.right is not None:
        node_dict['right'] = _tree_to_dict(node.right)
    
    return node_dict


# Export all public functions
__all__ = [
    'Node',
    'create_binary_tree',
    'add_node_by_path',
    'delete_node',
    'delete_tree',
    'print_tree',
    'print_tree_range',
    'edit_node_value',
    'build_tree_from_yaml',
    'write_tree_to_yaml'
]
