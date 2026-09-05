from pathlib import Path
import os

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


def readfile():
    try:
        readfielandfolder()

        name = input(
            "Enter the file name or file path from root directory :- "
        )

        root = Path.cwd()
        p = root / name

        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print(data)

            print("Readed successfully")
        else:
            print("The file does not exist")

    except Exception as err:
        print(f"An error occurred as {err}")


def updatefile():
    try:

        readfielandfolder()

        name = input(
            "Enter the file name or file path from root directory :- "
        )

        root = Path.cwd()
        p = root / name

        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file :- ")
            print("press 2 for overwriting the data of your file")
            print("press 3 for appending some content in your file")

            res = int(input("tell your response :- "))

            if res == 1:
                name2 = input(
                    "Enter your new file name or file path from root directory :- "
                )

                p2 = root / name2
                p.rename(p2)

                print("File renamed successfully")

            if res == 2:
                with open(p, "w") as fs:
                    data = input(
                        "tell what you want to write this is overwrite the data :- "
                    )
                    fs.write(data)

                print("File data overwritten successfully")

            if res == 3:
                with open(p, "a") as fs:
                    data = input("tell what you want to append :- ")
                    fs.write(" " + data)

                print("Content appended successfully")

        else:
            print("The file does not exist")

    except Exception as err:
        print(f"An error occurred as {err}")


def deletefile():
    try:
        readfielandfolder()

        name = input(
            "Enter the file name or file path from root directory :- "
        )

        root = Path.cwd()
        p = root / name

        if p.exists() and p.is_file():
            os.remove(p)

            print("File removed successfully")

        else:
            print("No such file exists")

    except Exception as err:
        print(f"An error occurred as {err}")


print("press 1 for creating a file or folder")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deletion a file")

check = int(input("please tell your response :- "))

if check == 1:
    createfileorfolder()

elif check == 2:
    readfile()

elif check == 3:
    updatefile()

elif check == 4:
    deletefile()

else:
    print("Invalid response")
