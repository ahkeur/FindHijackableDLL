import os
import fnmatch
 
def find_dll_files(root_dir):
    """Recursively find all DLL files starting from root_dir."""
    dll_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in fnmatch.filter(files, '*.dll'):
            dll_files.append(os.path.join(root, file))
    return dll_files
 
def main():
    home_dir = os.path.expanduser('~')
 
    print(f"Searching for DLL files under {home_dir}")
    dll_files = find_dll_files(home_dir)
 
    if dll_files:
        print(f"Found {len(dll_files)} DLL files:")
        for file in dll_files:
            if "Downloads" in file:
                continue
            if "Desktop" in file:
                continue
            if "Documents" in file:
                continue
            if "Pictures" in file:
                continue
            if "Videos" in file:
                continue
            if "Music" in file:
                continue
            if "Public" in file:
                continue
            print(file)
    else:
        print("No DLL files found.")
 
if __name__ == "__main__":
    main()