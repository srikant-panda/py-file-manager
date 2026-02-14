
py-file-manager/
│
├── main.py
├── README.md
│
└── Operations/
    ├── __init__.py
    └── operation.py

# Py File Manager 🗂️🐍

A simple **Linux-style CLI File Manager** built using Python.  
This project mimics common Linux terminal commands like `cd`, `ls`, `pwd`, `mkdir`, `touch`, `rm`, and `cp` using Python’s built-in modules (`os` and `shutil`).

This project is mainly built for learning filesystem operations and command parsing in Python.

---

## 🚀 Features

✅ Supports basic terminal-like commands:

- `pwd` → show current working directory  
- `cd <path>` → change directory  
- `ls` → list files/folders (hides hidden files)
- `ls -a` → list all files including hidden ones  
- `mkdir <dir>` → create directories  
- `mkdir -p <path>` → create recursive directories  
- `touch <file>` → create file  
- `touch -f <file>` → force replace file  
- `rm <file>` → delete a file  
- `rm -r <dir>` → remove empty directory  
- `rm -rf <dir>` → remove non-empty directory recursively  
- `cp <src> <dst>` → copy file or directory  

---

## 📂 Project Structure



py-file-manager/
│
├── main.py # CLI shell program (command parser)
├── README.md # Project documentation
│
└── Operations/
├── init.py # Package initializer
└── operation.py # Core filesystem functions (os/shutil wrappers)


---

## 🛠️ Requirements

- Python 3.x  
- Works best on Linux

No external libraries required.

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/srikant-panda/py-file-manager.git
cd py-file-manager


Run the file manager:

python3 main.py

🧪 Example Commands
pwd
ls
ls -a
cd Downloads
mkdir testFolder
touch file.txt
rm file.txt
cp file1.txt backup.txt
rm -rf testFolder

⚠️ Warning

This program can modify or delete real files/folders on your system.

Be careful with:

rm

rm -rf

Recommended: Test inside a safe folder.

🎯 Learning Purpose

This project was built to learn and practice:

Python os module

Python shutil module

File and directory handling

Exception handling (FileNotFoundError, PermissionError, etc.)

CLI command parsing

Building a mini terminal-like program

🚧 Future Improvements

Planned features:

Add mv command (move/rename)

Add cat command (read file content)

Add better path handling (.., ., ~)

Add history support

Add help command

Improve error messages

👨‍💻 Author

Built by Srikant Panda 🚀

📜 License

Open-source project for learning and experimentation.
