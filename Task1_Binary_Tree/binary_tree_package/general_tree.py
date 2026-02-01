"""
Bonus Feature: General Tree Implementation (N-ary Tree)
A Node class that can create trees with any number of children per node.
"""

import yaml
from typing import Optional, Any, List


class GeneralNode:
    """
    A General Node class for creating n-ary trees (trees with any number of children).
    
    Attributes:
        value: The value stored in the node
        children: List of child nodes
    """
    
    def __init__(self, value: Any):
        """
        Initialize a new general node.
        
        Args:
            value: The value to store in the node
        """
        self.value = value
        self.children: List['GeneralNode'] = []
    
    def add_child(self, child: 'GeneralNode') -> None:
        """Add a child node."""
        self.children.append(child)
    
    def __repr__(self):
        return f"GeneralNode({self.value})"


def create_general_tree(value: Any) -> GeneralNode:
    """
    Create a new general tree with a root node.
    
    Args:
        value: The value for the root node
        
    Returns:
        A new GeneralNode object as the root of the tree
    """
    return GeneralNode(value)


def add_child_by_path(root: Optional[GeneralNode], path: List[int], value: Any) -> bool:
    """
    Add a child node to the general tree using a path of child indices.
    
    Args:
        root: The root node of the tree
        path: A list of integers indicating which child to follow at each level
              (e.g., [0, 2] means first child, then third child of that)
        value: The value for the new node
        
    Returns:
        True if node was added successfully, False otherwise
    """
    if root is None:
        return False
    
    current = root
    
    # Navigate to the parent position
    for i, child_index in enumerate(path):
        if child_index >= len(current.children):
            print(f"Cannot add node: invalid child index {child_index} at level {i}")
            return False
        current = current.children[child_index]
    
    # Add the new child
    current.add_child(GeneralNode(value))
    return True


def add_child_direct(node: GeneralNode, value: Any) -> GeneralNode:
    """
    Add a child directly to a node and return the child.
    
    Args:
        node: The parent node
        value: The value for the new child
        
    Returns:
        The newly created child node
    """
    child = GeneralNode(value)
    node.add_child(child)
    return child


def delete_general_tree(root: Optional[GeneralNode]) -> None:
    """
    Delete the entire general tree.
    
    Args:
        root: The root node of the tree to delete
    """
    if root is None:
        return
    
    # Post-order traversal to delete all nodes
    for child in root.children:
        delete_general_tree(child)
    
    root.children.clear()


def print_general_tree(root: Optional[GeneralNode], prefix: str = "", is_root: bool = True) -> None:
    """
    Print the general tree in a visual format.
    
    Args:
        root: The root node of the tree
        prefix: Prefix string for formatting (used in recursion)
        is_root: Whether this is the root node (used in recursion)
    """
    if root is None:
        return
    
    # Print current node
    if is_root:
        print(f"Root: {root.value}")
    else:
        print(f"{prefix}{root.value}")
    
    # Print children
    if root.children:
        for i, child in enumerate(root.children):
            is_last_child = (i == len(root.children) - 1)
            connector = "└── " if is_last_child else "├── "
            extension = "    " if is_last_child else "│   "
            
            if is_root:
                new_prefix = connector
                next_prefix = extension
            else:
                new_prefix = prefix + connector
                next_prefix = prefix + extension
            
            print(f"{new_prefix}{child.value}")
            
            # Recursively print grandchildren
            if child.children:
                for j, grandchild in enumerate(child.children):
                    is_last_grandchild = (j == len(child.children) - 1)
                    print_general_tree(grandchild, next_prefix, False)


def edit_general_node_value(root: Optional[GeneralNode], old_value: Any, new_value: Any) -> bool:
    """
    Edit the value of a node in the general tree.
    
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
    
    # Search in all children
    for child in root.children:
        if edit_general_node_value(child, old_value, new_value):
            return True
    
    return False


def find_node(root: Optional[GeneralNode], value: Any) -> Optional[GeneralNode]:
    """
    Find a node with the specified value.
    
    Args:
        root: The root node of the tree
        value: The value to search for
        
    Returns:
        The node if found, None otherwise
    """
    if root is None:
        return None
    
    if root.value == value:
        return root
    
    for child in root.children:
        result = find_node(child, value)
        if result is not None:
            return result
    
    return None


def build_general_tree_from_yaml(yaml_file: str) -> Optional[GeneralNode]:
    """
    Build a general tree from a YAML file.
    
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
        
        return _build_general_tree_recursive(data)
    
    except FileNotFoundError:
        print(f"Error: File '{yaml_file}' not found")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None


def _build_general_tree_recursive(data: dict) -> Optional[GeneralNode]:
    """
    Helper function to recursively build general tree from dictionary.
    
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
    
    node = GeneralNode(value)
    
    # Recursively build children
    children_data = data.get('children', [])
    if isinstance(children_data, list):
        for child_data in children_data:
            child_node = _build_general_tree_recursive(child_data)
            if child_node is not None:
                node.add_child(child_node)
    
    return node


def write_general_tree_to_yaml(root: Optional[GeneralNode], yaml_file: str) -> bool:
    """
    Write a general tree to a YAML file.
    
    Args:
        root: The root node of the tree
        yaml_file: Path to the output YAML file
        
    Returns:
        True if successful, False otherwise
    """
    try:
        tree_dict = _general_tree_to_dict(root)
        
        with open(yaml_file, 'w') as file:
            yaml.dump(tree_dict, file, default_flow_style=False, sort_keys=False)
        
        return True
    
    except Exception as e:
        print(f"Error writing to YAML file: {e}")
        return False


def _general_tree_to_dict(node: Optional[GeneralNode]) -> Optional[dict]:
    """
    Helper function to convert general tree to dictionary format.
    
    Args:
        node: The node to convert
        
    Returns:
        Dictionary representation of the node and its children
    """
    if node is None:
        return None
    
    node_dict = {'value': node.value}
    
    if node.children:
        node_dict['children'] = [_general_tree_to_dict(child) for child in node.children]
    
    return node_dict


# Export all public functions
__all__ = [
    'GeneralNode',
    'create_general_tree',
    'add_child_by_path',
    'add_child_direct',
    'delete_general_tree',
    'print_general_tree',
    'edit_general_node_value',
    'find_node',
    'build_general_tree_from_yaml',
    'write_general_tree_to_yaml'
]
