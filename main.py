from pathlib import Path


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


def createfile():
    try:
        readfielandfolder()

        name = input(
            "Please tell your file name or path from root directory :- "
        )

        # Current project/root directory
        root = Path.cwd()

        # Create path from the project root
        p = root / name

        if not p.exists():

            # Create parent folders if they don't exist
            p.parent.mkdir(parents=True, exist_ok=True)

            with open(p, "w") as fs:
                data = input("What you want to write in this file :- ")
                fs.write(data)

            print("FILE CREATED SUCCESSFULLY")
        else:
            print("This file already exists")

    except Exception as err:
        print(f"An error occurred as {err}")


def readfile():
    readfielandfolder()
    print("run readfile")


def updatefile():
    readfielandfolder()
    print("run updatefile")


def deletefile():
    readfielandfolder()
    print("run deletefile")


print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deletion a file")

check = int(input("please tell your response :- "))

if check == 1:
    createfile()

elif check == 2:
    readfile()

elif check == 3:
    updatefile()

elif check == 4:
    deletefile()

else:
    print("Invalid response")
