import os
import shutil


def get_size(path: str) -> int:
    """Returns the total size of a file or directory in bytes."""
    total_size = 0
    if os.path.isfile(path):
        total_size = os.path.getsize(path)
    elif os.path.isdir(path):
        for dirpath, _, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if os.path.exists(fp):
                    total_size += os.path.getsize(fp)
    return total_size


def format_size(size_in_bytes: float) -> str:
    """Converts bytes to a readable format (B, KB, MB, GB, TB)."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024
    return f"{size_in_bytes:.2f} TB"


def clear_cache():
    home_dir = os.path.expanduser("~")
    cache_directory = os.path.join(home_dir, "Library", "Caches")

    if not os.path.exists(cache_directory):
        print(f"The directory {cache_directory} does not exist.")
        return

    total_freed = 0

    for item in os.listdir(cache_directory):
        item_path = os.path.join(cache_directory, item)
        try:
            if not os.path.exists(item_path):
                continue

            item_size = get_size(item_path)

            if os.path.isdir(item_path):
                shutil.rmtree(item_path, ignore_errors=True)
            else:
                os.remove(item_path)

            total_freed += item_size

        except PermissionError:
            print(f"Permission denied: {item_path}")
        except Exception as e:
            print(f"Error deleting {item_path}: {e}")

    print(f"All contents of {cache_directory} have been deleted.")
    print(f"Freed space: {format_size(total_freed)}")


if __name__ == "__main__":
    clear_cache()
