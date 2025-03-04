import os
import shutil

def clear_cache():
    home_dir = os.path.expanduser("~")
    cache_directory = os.path.join(home_dir, "Library", "Caches")

    if os.path.exists(cache_directory):
        for item in os.listdir(cache_directory):
            item_path = os.path.join(cache_directory, item)
            try:
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path) 
                else:
                    os.remove(item_path) 
            except Exception as e:
                print(f"Error deleting {item_path}: {e}")
        print(f"All contents of {cache_directory} have been successfully deleted.")
    else:
        print(f"The directory {cache_directory} does not exist.")

clear_cache()
