# Config: Data Structure to store directory tree
class Config:
    # Static variable to assign incremental id to each folder
    id = 1

    def __init__(self):
        # Directory tree represented as a dictionary
        self.tree = {}
        # Set to keep track of folder names for uniqueness
        self.name_set = set()


def print_directory_tree(config):
    """
    Function to print the current directory tree stored in the config object.
    """
    print(config.tree)


def load_directory_tree(config):
    """
    Function to initialize the directory tree with a root folder.
    """
    # Root folder dictionary with an empty list of children
    root_folder = {'id': 0, 'name': "root", 'children': []}
    # Set the root folder as the directory tree in the configuration
    config.tree = root_folder
    # Add "root" to the set of folder names, so that no other folder is created with name 'root'
    config.name_set.add("root")


def get_folder_by_path(config, folder_path):
    """
    Function to retrieve a folder from the directory tree given its path.
    Return none if folder doesn't exist.
    """

    if folder_path is None:
        return None
    # Split folder path using / and Check if a folder exists in given path iteratively.
    folders = folder_path.split('/')
    current_folder = config.tree
    for folder_name in folders:
        # Ignore if folder is blank string
        # (First/last part of path string due to slice method)
        if folder_name == '':
            continue
        found = False
        for child in current_folder['children']:
            if child['name'] == folder_name:
                current_folder = child
                found = True
                break
        if not found:
            return None
    return current_folder


def get_parent_and_name(folder_path):
    """
    Function to extract the parent path and folder name from a given folder path.
    Return '' if parent is root folder.
    """


    path_parts = folder_path.rsplit('/', 1)
    if len(path_parts) == 1:
        return '', folder_path
    else:
        return path_parts[0], path_parts[1]


def get_folder_path_using_name(config, folder_name):
    """
    Function to find the path of a folder in the directory tree given its name.
    """
    return get_folder_path_recursive(config.tree, folder_name, [])


def get_folder_path_recursive(folder, folder_name, path):
    """
    Recursive function to search for a folder in the directory tree and return its path.
    """
    if folder['name'] == folder_name:
        return '/'.join(path)
    for child in folder['children']:
        result = get_folder_path_recursive(child, folder_name, path + [child['name']])
        if result:
            return result
    return None


def add_folder_by_parent_path(config, parent_path, folder_name):
    """
    Function to add a new folder to the directory tree given its parent path and name.
    """
    # Check if folder with same name already exists
    if folder_name in config.name_set:
        print(f"Folder with name '{folder_name}' already exists. Kindly please use another unique name.")
        return
    # Create a new folder dictionary
    new_folder = {'id': Config.id, 'name': folder_name, 'children': []}
    # Increment the id variable to maintain uniqueness
    Config.id += 1
    # Find the parent folder in the directory tree
    parent = get_folder_by_path(config, parent_path)
    if parent:
        # Add the new folder to the parent's children list
        parent['children'].append(new_folder)
        # Add the folder name to the set of folder names for uniqueness
        config.name_set.add(folder_name)
    else:
        print(f"No folder found at path '{parent_path}'.")


def add_folder_by_parent_folder_name(config, parent_folder_name, folder_name):
    """
    Function to add a new folder to the directory tree given its parent folder's name and the new folder's name.
    """
    # Check if folder with same name already exists
    if folder_name in config.name_set:
        print(f"Folder with name '{folder_name}' already exists. Kindly please use another unique name.")
        return
    # Create a new folder dictionary
    new_folder = {'id': Config.id, 'name': folder_name, 'children': []}
    # Increment the id variable to maintain uniqueness
    Config.id += 1
    # Find the parent folder's path using its name
    parent_path = get_folder_path_using_name(config, parent_folder_name)
    # Find the parent folder in the directory tree
    parent = get_folder_by_path(config, parent_path)
    if parent:
        # Add the new folder to the parent's children list
        parent['children'].append(new_folder)
        # Add the folder name to the set of folder names for uniqueness
        config.name_set.add(folder_name)
    else:
        print(f"No folder found with name '{parent_folder_name}'.")


def remove_folder_by_path(config, folder_path):
    """
    Function to remove a folder from the directory tree given its path.
    """
    parent_path, folder_name = get_parent_and_name(folder_path)
    # Check if folder with given name exists
    if folder_name not in config.name_set:
        print(f"Folder with name '{folder_name}' does not exist.")
        return
    # Find the parent folder in the directory tree
    parent = get_folder_by_path(config, parent_path)
    if parent:
        for folder in parent['children']:
            if folder['name'] == folder_name:
                # Remove the folder from the parent's children list
                parent['children'].remove(folder)
                # Remove the folder name from the set of folder names
                # New folders with removed folder_names could be created
                config.name_set.remove(folder_name)
                return
        print(f"Folder '{folder_name}' not found.")
    else:
        print(f"Parent folder at path '{parent_path}' not found.")


def remove_folder_by_name(config, folder_name):
    """
    Function to remove a folder from the directory tree given its name.
    """
    # Check if folder with given name exists
    if folder_name not in config.name_set:
        print(f"Folder with name '{folder_name}' does not exist.")
        return
    # Find the folder's path using its name
    folder_path = get_folder_path_using_name(config, folder_name)
    # Extract the parent path and folder name
    parent_path, folder_name = get_parent_and_name(folder_path)
    # Find the parent folder in the directory tree
    parent = get_folder_by_path(config, parent_path)
    if parent:
        for folder in parent['children']:
            if folder['name'] == folder_name:
                # Remove the folder from the parent's children list
                parent['children'].remove(folder)
                # Remove the folder name from the set of folder names
                config.name_set.remove(folder_name)
                return
        print(f"Folder '{folder_name}' not found.")
    else:
        print(f"Folder '{folder_name}' not found.")


def update_folder_name_using_path(config, folder_path, new_name):
    """
    Function to update the name of a folder in the directory tree given its path.
    """
    # Find the folder in the directory tree
    folder = get_folder_by_path(config, folder_path)
    if folder:
        # Update the folder's name
        folder['name'] = new_name
    else:
        print(f"Folder with path '{folder_path}' not found.")


def update_folder_name_using_name(config, folder_name, new_name):
    """
    Function to update the name of a folder in the directory tree given its name.
    """
    # Find the folder's path using its name
    folder_path = get_folder_path_using_name(config, folder_name)

    # Find the folder in the directory tree
    folder = get_folder_by_path(config, folder_path)
    if folder:
        # Update the folder's name
        folder['name'] = new_name
    else:
        print(f"Folder '{folder_name}' not found.")
