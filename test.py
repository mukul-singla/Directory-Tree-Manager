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
