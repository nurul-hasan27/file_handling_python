# File & Folder Handler CLI 🗂️

A simple, menu-driven Python command-line tool to **create, read, update, and delete**
both **files** and **folders** in the current directory — great for learning core
Python file-system operations (`pathlib`, `os`, `shutil`) and, alongside that,
practising professional Git/GitHub workflows.

## Features

- 📄 **File operations**
  - Create a file with content
  - Read a file's content
  - Update a file — rename it, overwrite it, or append to it
  - Delete a file
- 📁 **Folder operations**
  - Create a folder (including nested paths)
  - Read/list a folder's contents
  - Rename a folder
  - Delete a folder (with a confirmation prompt, since it removes everything inside)
- 🔍 Lists all existing files/folders before every operation, so you always know
  what's around before you type a name.
- 🛡️ Basic error handling everywhere via `try/except`.

## Requirements

- Python 3.8+
- No external dependencies — uses only the standard library
  (`pathlib`, `os`, `shutil`).

## Getting Started

```bash
git clone git@github.com:nurul-hasan27/file_handling_python.git
cd file_handling_python
python3 main.py
```

## Usage

Run the script and pick an option from the menu:

```
====== FILE & FOLDER HANDLER ======
 1. Create a file
 2. Read a file
 3. Update a file
 4. Delete a file
 5. Create a folder
 6. Read a folder
 7. Rename a folder
 8. Delete a folder
 0. Exit
====================================
```

Each option will prompt you for whatever it needs (a name, content to write, etc.).

## Project History

This project started as a **files-only** CLI. Folder support (create/read/rename/delete)
was added later to close [Issue #1](../../issues/1) — see the commit history and
closed pull requests for the full development story, built branch by branch.

## Roadmap / Ideas for Future Enhancements

- [ ] Copy/move files and folders
- [ ] Search for a file/folder by name pattern
- [ ] Add unit tests (`pytest`)
- [ ] Add a `--path` CLI argument instead of always using the current directory
- [ ] Package it as an installable CLI tool

## License

This project is open source and available under the [MIT License](LICENSE).