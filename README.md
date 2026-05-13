<div align="center">

```
  ███████╗██╗ ██╗     ███████╗
  ██╔════╝██║ ██║     ██╔════╝
█████╗  ██║ ██║     █████╗
██╔══╝  ██║ ██║     ██╔══╝
  ██║     ██║ ███████╗███████╗
  ╚═╝     ╚═╝ ╚══════╝╚══════╝
O R G A N I Z E R
```

**Stop drowning in a sea of random files.**  
One click. Every file in its place.

[![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-7c6af7?style=flat-square)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-MIT-a6e3a1?style=flat-square)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078d4?style=flat-square&logo=windows)](https://www.microsoft.com/windows)

</div>

---

## ⚡ What Is This?

**File Organizer** is a sleek desktop app that scans a messy folder and instantly sorts every file into neat sub-folders by type — Images, Videos, Documents, Code, and more.

No terminal. No configuration. No nonsense.

> *You pick a folder. You click Organise. It's done.*

---

<div align="center">
  <img width="48%" alt="File Organizer - Main Window" src="https://github.com/user-attachments/assets/2e2f7228-1507-4b00-92f9-d6593369d88c" />
  &nbsp;
  <img width="48%" alt="File Organizer - After Organising" src="https://github.com/user-attachments/assets/f7f36f01-30f3-4d1f-a466-c21d904f09ab" />
</div>


## 📦 File Categories

| Folder | Extensions |
|---|---|
| 🖼️ **Images** | `.jpg` `.jpeg` `.png` `.gif` `.bmp` `.svg` `.webp` `.ico` `.tiff` |
| 🎬 **Videos** | `.mp4` `.mkv` `.avi` `.mov` `.wmv` `.flv` `.webm` `.m4v` |
| 🎵 **Audio** | `.mp3` `.wav` `.flac` `.aac` `.ogg` `.wma` `.m4a` |
| 📄 **Documents** | `.pdf` `.doc` `.docx` `.xls` `.xlsx` `.ppt` `.pptx` `.txt` `.csv` |
| 🗜️ **Archives** | `.zip` `.rar` `.7z` `.tar` `.gz` `.bz2` `.xz` |
| 💻 **Code** | `.py` `.js` `.ts` `.html` `.css` `.java` `.cpp` `.json` `.yaml` |
| ⚙️ **Executables** | `.exe` `.msi` `.apk` `.dmg` `.pkg` |
| 🔤 **Fonts** | `.ttf` `.otf` `.woff` `.woff2` |
| 📁 **Others** | Everything else |

---

## 🚀 Getting Started

### Option A — Run from source

```bash
# 1. Clone the repo
git clone https://github.com/you/file-organizer.git
cd file-organizer

# 2. (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch
python main.py
```

### Option B — Download the installer *(coming soon)*

Download `FileOrganizerSetup.exe` from [Releases](../../releases) and run it.  
No Python required.

---

## 🏗️ Project Structure

```
file-organizer/
│
├── main.py              ← Entry point — launches the GUI
├── organizer.py         ← Core logic — file detection & moving
├── gui.py               ← Tkinter GUI — all visual components
│
├── assets/
│   └── icon.ico         ← App icon (taskbar + title bar)
│
├── requirements.txt     ← Python dependencies
└── README.md            ← You are here
```

---

## 🔨 Build Your Own `.exe`

### Step 1 — Install PyInstaller

```bash
pip install pyinstaller
```

### Step 2 — Bundle

```bash
pyinstaller --onefile --windowed --icon=assets/icon.ico main.py
```

### Step 3 — Find your executable

```
dist/
└── main.exe   ✅  ready to share
```

> **Tip:** Add `--name "File Organizer"` to rename the output binary.

---

### Wrap in an Installer (Inno Setup)

1. Download & install **[Inno Setup](https://jrsoftware.org/isinfo.php)**
2. Create a new script pointing to `dist/main.exe`
3. Compile → get `FileOrganizerSetup.exe`

Your users get a proper install wizard, Start Menu shortcut, and uninstaller.

---

## 🛡️ Safety Guarantees

- ✅ **Only moves top-level files** — sub-folders are never touched
- ✅ **Never overwrites** — duplicate filenames get `_1`, `_2` suffixes
- ✅ **Skips hidden files** — dotfiles left untouched
- ✅ **Confirms before acting** — dialog prompt before any changes
- ✅ **Full error log** — every failure is reported in the Activity Log

---

## 🧩 Requirements

```
Python     >= 3.10
Pillow     >= 9.0      # for icon rendering (pip install pillow)
tkinter                # built into Python — no install needed
```

`requirements.txt`:
```
Pillow>=9.0
pyinstaller>=5.0
```

---

## 🗺️ Roadmap

- [ ] Undo last organisation
- [ ] Custom rules (user-defined categories)
- [ ] Recursive mode (organise sub-folders too)
- [ ] macOS & Linux support
- [ ] Dark / light theme toggle
- [ ] Drag-and-drop folder support

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you'd like to change.

```bash
# Fork → clone → branch → PR
git checkout -b feature/my-cool-feature
```

---

## 📜 License

MIT © 2025 — free to use, modify, and distribute.

---

<div align="center">

*Built with Python + Tkinter · Zero bloat · 100% offline*

**If this saved your sanity, drop a ⭐**

</div>
