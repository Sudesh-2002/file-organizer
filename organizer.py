import os
import shutil
from pathlib import Path

# --- File type mapping ---
FILE_CATEGORIES = {
    "Images":     [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico", ".tiff"],
    "Videos":     [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v"],
    "Audio":      [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"],
    "Documents":  [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv", ".odt"],
    "Archives":   [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
    "Code":       [".py", ".js", ".ts", ".html", ".css", ".java", ".cpp", ".c", ".h", ".json", ".xml", ".yaml", ".yml", ".sh", ".bat"],
    "Executables":[".exe", ".msi", ".apk", ".dmg", ".pkg"],
    "Fonts":      [".ttf", ".otf", ".woff", ".woff2"],
    "Others":     []
}

def get_category(extension: str) -> str:
    ext = extension.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"


def organize_folder(folder_path: str, callback=None) -> dict:
    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"Invalid folder path: {folder_path}")

    summary = {}
    errors  = []

    # Collect only top-level files (skip subfolders and hidden files)
    files = [f for f in folder.iterdir() if f.is_file() and not f.name.startswith(".")]

    if not files:
        if callback:
            callback("⚠️  No files found in the selected folder.")
        return summary

    for file in files:
        category    = get_category(file.suffix)
        target_dir  = folder / category

        try:
            target_dir.mkdir(exist_ok=True)

            dest = target_dir / file.name

            # Avoid overwriting — append a counter if name already exists
            counter = 1
            while dest.exists():
                stem = file.stem
                dest = target_dir / f"{stem}_{counter}{file.suffix}"
                counter += 1

            shutil.move(str(file), str(dest))

            summary[category] = summary.get(category, 0) + 1

            if callback:
                callback(f"✅  {file.name}  →  {category}/")

        except Exception as e:
            error_msg = f"❌  Failed to move {file.name}: {e}"
            errors.append(error_msg)
            if callback:
                callback(error_msg)

    # Report errors at the end
    if errors and callback:
        callback(f"\n⚠️  {len(errors)} error(s) occurred during organising.")

    return summary