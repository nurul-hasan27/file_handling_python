from pathlib import Path
import os
import shutil

def show_tree(path, prefix=""):
    path = Path(path)

    items = sorted(
        [item for item in path.iterdir() if item.name != ".git"],
        key=lambda x: (x.is_file(), x.name.lower())
    )

    for i, item in enumerate(items):
        is_last = i == len(items) - 1

        connector = "└── " if is_last else "├── "
        name = item.name + "/" if item.is_dir() else item.name 

        print(prefix + connector + name)

        if item.is_dir():
            new_prefix = prefix + ("    " if is_last else "│   ")
            show_tree(item, new_prefix)


def readfielandfolder():
    path = Path(".")

    print(path.resolve().name + "/")
    show_tree(path)


def createfileorfolder():
    try:
        readfielandfolder()

        name = input(
            "Please tell your file (or folder with '/' at end) path from root directory :- "
        )

        root = Path.cwd()

        # Check whether the user wants to create a folder
        is_folder = name.endswith("/")

        # Remove the trailing slash before creating the path
        clean_name = name.rstrip("/\\")

        if not clean_name:
            print("Invalid name")
            return

        p = (root / clean_name).resolve()

        # Make sure the path stays inside the project root
        if root.resolve() not in p.parents and p != root.resolve():
            print("Invalid path. Please enter a path inside the root directory.")
            return

        if p.exists():
            print("This file or folder already exists")
            return

        if is_folder:
            p.mkdir(parents=True, exist_ok=True)

            print("FOLDER CREATED SUCCESSFULLY")

        else:
            p.parent.mkdir(parents=True, exist_ok=True)

            with open(p, "w") as fs:
                data = input("What you want to write in this file :- ")
                fs.write(data)

            print("FILE CREATED SUCCESSFULLY")

    except Exception as err:
        print(f"An error occurred as {err}")


def readfileorfolder():
    try:
        readfielandfolder()

        name = input(
            "Enter the file name or file path from root directory :- "
        )

        root = Path.cwd().resolve()
        p = (root / name).resolve()

        # Make sure the path stays inside the project root
        if root not in p.parents and p != root:
            print("Invalid path. Please enter a path inside the root directory.")
            return

        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print(data)

            print("Readed successfully")

        elif p.exists() and p.is_dir():
            print("The given path is a folder. Please enter a file path.")

        else:
            print("The file does not exist")

    except Exception as err:
        print(f"An error occurred as {err}")


def updatefileorfolder():
    try:

        readfielandfolder()

        name = input(
            "Enter the file or folder path from root directory :- "
        )

        root = Path.cwd().resolve()
        p = (root / name).resolve()

        # Make sure the path stays inside the root directory
        if root not in p.parents and p != root:
            print("Invalid path. Please enter a path inside the root directory.")
            return

        if p.exists() and p.is_file():

            # ================= FILE UPDATE =================

            print("press 1 for changing the name of your file :- ")
            print("press 2 for overwriting the data of your file")
            print("press 3 for appending some content in your file")

            res = int(input("tell your response :- "))

            if res == 1:
                name2 = input(
                    "Enter your new file name or file path from root directory :- "
                )

                p2 = (root / name2).resolve()

                # Make sure the new path stays inside root
                if root not in p2.parents and p2 != root:
                    print(
                        "Invalid path. Please enter a path inside the root directory."
                    )
                    return

                p2.parent.mkdir(parents=True, exist_ok=True)

                p.rename(p2)

                print("File renamed successfully")

            elif res == 2:
                with open(p, "w") as fs:
                    data = input(
                        "tell what you want to write this is overwrite the data :- "
                    )
                    fs.write(data)

                print("File data overwritten successfully")

            elif res == 3:
                with open(p, "a") as fs:
                    data = input("tell what you want to append :- ")
                    fs.write(" " + data)

                print("Content appended successfully")

            else:
                print("Invalid response")

        elif p.exists() and p.is_dir():

            # ================= FOLDER UPDATE =================

            print("press 1 for changing the name of your folder :- ")

            res = int(input("tell your response :- "))

            if res == 1:
                name2 = input(
                    "Enter your new folder name or folder path from root directory :- "
                )

                p2 = (root / name2).resolve()

                # Make sure the new path stays inside root
                if root not in p2.parents and p2 != root:
                    print(
                        "Invalid path. Please enter a path inside the root directory."
                    )
                    return

                # Create parent folders if needed
                p2.parent.mkdir(parents=True, exist_ok=True)

                p.rename(p2)

                print("Folder renamed successfully")

            else:
                print("Invalid response")

        else:
            print("The file or folder does not exist")

    except Exception as err:
        print(f"An error occurred as {err}")


def deletefileorfolder():
    try:
        readfielandfolder()

        name = input(
            "Enter the file or folder path from root directory :- "
        )

        root = Path.cwd().resolve()
        p = (root / name).resolve()

        # Make sure the path stays inside the root directory
        if root not in p.parents and p != root:
            print("Invalid path. Please enter a path inside the root directory.")
            return

        if p.exists() and p.is_file():

            # ================= FILE DELETE =================

            os.remove(p)

            print("File removed successfully")

        elif p.exists() and p.is_dir():

            # ================= FOLDER DELETE =================

            print("The given path is a folder.")
            print(
                "WARNING: Deleting this folder will permanently delete "
                "the folder and all files/subfolders inside it."
            )

            res = input(
                "Do you want to recursively delete this folder permanently? "
                "(yes/no) :- "
            )

            if res.lower() == "yes":
                shutil.rmtree(p)

                print("Folder and all its contents removed permanently")

            else:
                print("Folder deletion cancelled")

        else:
            print("No such file or folder exists")

    except Exception as err:
        print(f"An error occurred as {err}")


print("press 1 for creating a file or folder")
print("press 2 for reading a file or folder")
print("press 3 for updating a file or folder")
print("press 4 for deletion a file or folder")

check = int(input("please tell your response :- "))

if check == 1:
    createfileorfolder()

elif check == 2:
    readfileorfolder()

elif check == 3:
    updatefileorfolder()

elif check == 4:
    deletefileorfolder()

else:
    print("Invalid response")
