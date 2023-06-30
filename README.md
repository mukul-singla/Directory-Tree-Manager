# Directory-Tree-Manager
This is a Python code snippet that implements a directory tree manager. It provides functions to add, get, update, and remove folders(CRUD operations) in a directory tree.


## Usage

The `Config` class represents the data structure to store the directory tree. It has the following attributes:

- `tree`: A dictionary representing the directory tree.
- `name_set`: A set to keep track of folder names for uniqueness.

The folders are created using given dictionary format: 
```python
new_folder = {'id': Config.id, 'name': folder_name, 'children': []}
```

To use the directory tree manager, follow these steps:

1. Import all files from config.py file and create a new instance of the `Config` class.

```python
from config import *
config = Config()
```

2. Load the directory tree by initializing it with a root folder.

```python
load_directory_tree(config)
```


3. Use the available functions to manage the directory tree:

- 'print_directory_tree(config)' : Print the current directory tree.
* 'add_folder_by_parent_path(config, parent_path, folder_name)' : Add a new folder to the directory tree given its parent folder's name and the new folder's name
+ 'add_folder_by_parent_folder_name(config, parent_folder_name, folder_name)' : Add a new folder to the directory tree given its parent folder's name and the new folder's name.
- 'remove_folder_by_path(config, folder_path)' : Remove a folder from the directory tree given its path.
* 'remove_folder_by_name(config, folder_name)' : Remove a folder from the directory tree given its name.
+ 'get_folder_by_path(config, folder_path)' : Fetch the folder in dictionary format with id, name and children dictionary.
- 'update_folder_name_using_path(config, folder_path, new_name)' : Update the name of a folder in the directory tree given its path.
* 'update_folder_name_using_name(config, folder_name, new_name)' : Update the name of a folder in the directory tree given its name.

Note: The functions assume that the directory tree is already loaded in the config object.

## Example
The example code can also be accessed using test.py file.
Here's an example that demonstrates how to use the directory tree manager:

```python
# import all files from config.py
from config import *

def main():
    config = Config()
    load_directory_tree(config)

    # Print initial directory tree
    print("Initial Directory Tree:")
    print_directory_tree(config)

    # Added folders F1,F4,F5 using parent folder name
    add_folder_by_parent_folder_name(config, 'root', 'F1')
    add_folder_by_parent_folder_name(config, 'F1', 'F4')
    add_folder_by_parent_folder_name(config, 'F1', 'F5')
    print("Directory tree after adding folders using parent name:")
    print_directory_tree(config)

    # Added folders F2,F3,F6,F7,F8 using parent folder name
    add_folder_by_parent_path(config, '/', 'F2')
    add_folder_by_parent_path(config, '/', 'F3')
    add_folder_by_parent_path(config, '/F3/', 'F6')
    add_folder_by_parent_path(config, '/F3/F6', 'F7')
    add_folder_by_parent_path(config, '/F3/F6/F7', 'F8')
    print("Directory tree after adding folders using parent path:")
    print_directory_tree(config)

    # Removed folders F3 and F8 using path and name respectively
    remove_folder_by_name(config,'F8')
    remove_folder_by_path(config,'/F2')
    print("Directory tree after removing folders F3 and F8:")
    print_directory_tree(config)

    # Updated name of folders F7 and F1 using name and path respectively
    update_folder_name_using_name(config,'F7','F7_updated')
    update_folder_name_using_path(config,'/F1','F1_updated')
    print("Directory tree after updating names of folders F7 and F1:")
    print_directory_tree(config)

    # Get folder F3 using path
    print("\n Folder F3:")
    print(get_folder_by_path(config,'/F3'))

    # Add another folders with existing folder names using parent folder name and path.
    add_folder_by_parent_path(config, '/', 'F6')
    add_folder_by_parent_folder_name(config,"F6","F5")

    # Remove folders with non-existing folder names using folder name and path.
    remove_folder_by_name(config,'F10')
    remove_folder_by_path(config,'/F9')

    #Update the name of non-existing folder using name and path.
    update_folder_name_using_name(config,'F7','F7_old')
    update_folder_name_using_path(config,'/F1','F1_old')

main()
```

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

You can copy this Git-formatted README and save it as `README.md` in your Git repository. Make sure to adjust the content and formatting as needed.



