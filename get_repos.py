import subprocess
import os

def clone_repo(clone_url, destination_folder):
    command = ["git", "clone", clone_url, destination_folder]
    subprocess.run(command, check=True)

def main():
    clone_url = "https://github.com/e9t/nsmc.git"  # 클론할 레포지토리의 URL
    destination_folder = "nsmc"  # 클론할 폴더 이름

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    print(f"Cloning {destination_folder} from {clone_url}...")
    try:
        clone_repo(clone_url, destination_folder)
        print(f"Successfully cloned {destination_folder}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone {destination_folder}: {e}")

if __name__ == "__main__":
    main()
