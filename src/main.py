import os
import shutil


def main():
    copy_static_directory()

def copy_static_directory():
    current_dir = os.getcwd()
    public_dir = os.path.join(current_dir,"public")
    static_dir = os.path.join(current_dir,"static")

    print(f"starting copy of: {static_dir} into {public_dir}...")
    
    # Create a clean Public directory
    if os.path.exists(public_dir):
        print(f"deleting: {public_dir}...")
        shutil.rmtree(public_dir)    

    recursive_copy(static_dir, public_dir)
    print(f"finished copying: {static_dir} into {public_dir}.")

def recursive_copy(source, destination):
    print(f"creating: {destination}...")
    os.mkdir(destination)

    print(f"copying contents of directory: {source} into {destination}...")
    dir_contents = os.listdir(source)
    for dir_content in dir_contents:
        source_content_path = os.path.join(source,dir_content)
        destination_content_path = os.path.join(destination,dir_content)
        if(os.path.isfile(source_content_path)):
            print(f"copying file: {source_content_path} into {destination_content_path}")
            shutil.copy(source_content_path, destination_content_path)
        else:
            recursive_copy(source_content_path, destination_content_path)
    

if __name__ == "__main__":
    main()