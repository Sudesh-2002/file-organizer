import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
from organizer import organize_folder

BG        = "#1e1e2e"
SURFACE   = "#2a2a3e"
ACCENT    = "#7c6af7"
ACCENT_HV = "#6a58e0"
TEXT      = "#cdd6f4"
SUBTEXT   = "#6c7086"
SUCCESS   = "#a6e3a1"
ERROR     = "#f38ba8"
WARNING   = "#f9e2af"


class FileOrganizerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Organizer")
        self.geometry("680x600")
        self.resizable(True, True)
        self.configure(bg=BG)

        # ✅ App icon (Windows .ico)
        try:
            self.iconbitmap("assets/icon.ico")
        except Exception:
            pass

        # ── ADDITION: Top header icon image (PNG support) ──
        try:
            self.header_icon = tk.PhotoImage(file="assets/icon.png")
        except Exception:
            self.header_icon = None

        self._selected_folder = tk.StringVar(value="")
        self._running = False
        self._build_ui()

    def _build_ui(self):
        header = tk.Frame(self, bg=ACCENT, height=56)
        header.pack(fill="x")

        # ✅ UPDATED: icon image added instead of feather/emoji style
        if self.header_icon:
            tk.Label(
                header,
                image=self.header_icon,
                bg=ACCENT
            ).pack(side="left", padx=(16, 8), pady=8)

        tk.Label(
            header,
            text="File Organizer",
            bg=ACCENT,
            fg="white",
            font=("Segoe UI", 16, "bold")
        ).pack(side="left", padx=10, pady=12)

        # ── Folder picker ──
        picker_frame = tk.Frame(self, bg=SURFACE, pady=16, padx=20)
        picker_frame.pack(fill="x", padx=20, pady=(18, 0))

        tk.Label(
            picker_frame, text="Select a folder to organise",
            bg=SURFACE, fg=TEXT,
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w")

        row = tk.Frame(picker_frame, bg=SURFACE)
        row.pack(fill="x", pady=(8, 0))

        self._folder_entry = tk.Entry(
            row, textvariable=self._selected_folder,
            bg="#12121e", fg=TEXT,
            insertbackground=TEXT,
            relief="flat", font=("Segoe UI", 10)
        )
        self._folder_entry.config(state="readonly")
        self._folder_entry.pack(side="left", fill="x", expand=True, ipady=6, padx=(0, 10))

        self._browse_btn = tk.Button(
            row, text="Browse…",
            bg=ACCENT, fg="white",
            activebackground=ACCENT_HV, activeforeground="white",
            relief="flat", font=("Segoe UI", 10, "bold"),
            padx=14, pady=4, cursor="hand2",
            command=self._browse
        )
        self._browse_btn.pack(side="right")

        # ── Progress bar ──
        prog_frame = tk.Frame(self, bg=BG)
        prog_frame.pack(fill="x", padx=20, pady=(14, 0))

        style = ttk.Style(self)
        style.theme_use("default")
        style.configure("TProgressbar", troughcolor=SURFACE, background=ACCENT, thickness=6)

        self._progress = ttk.Progressbar(prog_frame, mode="indeterminate")
        self._progress.pack(fill="x")

        bottom = tk.Frame(self, bg=BG, pady=14)
        bottom.pack(fill="x", padx=20, side="bottom")

        self._status_lbl = tk.Label(
            bottom, text="No folder selected.",
            bg=BG, fg=SUBTEXT, font=("Segoe UI", 9)
        )
        self._status_lbl.pack(side="left")

        self._clear_btn = tk.Button(
            bottom, text="Clear Log",
            bg=SURFACE, fg=SUBTEXT,
            activebackground=BG, activeforeground=TEXT,
            relief="flat", font=("Segoe UI", 9),
            padx=10, pady=4, cursor="hand2",
            command=self._clear_log
        )
        self._clear_btn.pack(side="right", padx=(8, 0))

        self._organise_btn = tk.Button(
            bottom, text="⚡  Organise",
            bg=ACCENT, fg="white",
            activebackground=ACCENT_HV, activeforeground="white",
            relief="flat", font=("Segoe UI", 10, "bold"),
            padx=18, pady=6, cursor="hand2",
            state="disabled",
            command=self._start_organise
        )
        self._organise_btn.pack(side="right")

        log_frame = tk.Frame(self, bg=BG)
        log_frame.pack(fill="both", expand=True, padx=20, pady=(14, 0))

        tk.Label(
            log_frame, text="Activity Log",
            bg=BG, fg=SUBTEXT, font=("Segoe UI", 9)
        ).pack(anchor="w")

        text_container = tk.Frame(log_frame, bg=SURFACE, bd=0)
        text_container.pack(fill="both", expand=True, pady=(4, 0))

        scrollbar = tk.Scrollbar(text_container, bg=SURFACE, troughcolor=SURFACE)
        scrollbar.pack(side="right", fill="y")

        self._log = tk.Text(
            text_container,
            bg=SURFACE, fg=TEXT,
            insertbackground=TEXT,
            relief="flat",
            font=("Courier New", 9),
            state="disabled",
            wrap="word",
            yscrollcommand=scrollbar.set,
            padx=10, pady=8
        )
        self._log.pack(fill="both", expand=True)
        scrollbar.config(command=self._log.yview)

        self._log.tag_config("ok",      foreground=SUCCESS)
        self._log.tag_config("err",     foreground=ERROR)
        self._log.tag_config("warn",    foreground=WARNING)
        self._log.tag_config("info",    foreground=SUBTEXT)
        self._log.tag_config("summary", foreground=ACCENT,
                              font=("Segoe UI", 9, "bold"))

    def _browse(self):
        folder = filedialog.askdirectory(title="Choose a folder to organise")
        if folder:
            self._selected_folder.set(folder)
            self._folder_entry.config(state="normal")
            self._folder_entry.delete(0, "end")
            self._folder_entry.insert(0, folder)
            self._folder_entry.config(state="readonly")
            self._organise_btn.config(state="normal")
            self._set_status(f"Ready — {folder}")
            self._log_write(f"📁  Folder selected: {folder}\n", "info")

    def _start_organise(self):
        if self._running:
            return
        folder = self._selected_folder.get()
        if not folder:
            messagebox.showwarning("No folder", "Please select a folder first.")
            return
        ok = messagebox.askyesno(
            "Confirm",
            f"Organise all files in:\n\n{folder}\n\nThis will move files into sub-folders. Continue?"
        )
        if not ok:
            return
        self._running = True
        self._organise_btn.config(state="disabled", text="Working…")
        self._browse_btn.config(state="disabled")
        self._progress.start(12)
        self._set_status("Organising…")
        self._log_write("\n── Starting ──────────────────────────\n", "info")
        thread = threading.Thread(target=self._run_organiser, args=(folder,), daemon=True)
        thread.start()

    def _run_organiser(self, folder):
        try:
            summary = organize_folder(folder, callback=self._thread_safe_log)
            self.after(0, self._on_done, summary)
        except Exception as e:
            self.after(0, self._on_error, str(e))

    def _on_done(self, summary):
        self._progress.stop()
        self._running = False
        self._organise_btn.config(state="normal", text="⚡  Organise")
        self._browse_btn.config(state="normal")
        self._log_write("\n── Summary ───────────────────────────\n", "info")
        if summary:
            for category, count in sorted(summary.items()):
                self._log_write(
                    f"   {category:<15} {count} file{'s' if count != 1 else ''} moved\n",
                    "summary"
                )
            total = sum(summary.values())
            self._log_write(f"\n   Total: {total} file{'s' if total != 1 else ''} organised ✓\n", "ok")
        else:
            self._log_write("   Nothing to move — folder may already be organised.\n", "warn")
        self._set_status("Done ✓")

    def _on_error(self, message):
        self._progress.stop()
        self._running = False
        self._organise_btn.config(state="normal", text="⚡  Organise")
        self._browse_btn.config(state="normal")
        self._log_write(f"\n❌  Error: {message}\n", "err")
        self._set_status("Error — see log.")
        messagebox.showerror("Error", message)

    def _thread_safe_log(self, message: str):
        tag = "err" if message.startswith("❌") else \
              "warn" if message.startswith("⚠") else "ok"
        self.after(0, self._log_write, message + "\n", tag)

    def _log_write(self, message: str, tag: str = ""):
        self._log.config(state="normal")
        self._log.insert("end", message, tag)
        self._log.see("end")
        self._log.config(state="disabled")

    def _clear_log(self):
        self._log.config(state="normal")
        self._log.delete("1.0", "end")
        self._log.config(state="disabled")

    def _set_status(self, text: str):
        self._status_lbl.config(text=text)