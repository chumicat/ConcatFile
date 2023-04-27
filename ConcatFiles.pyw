import re
import sys
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

# Variable Define
FILENAME_PATTERN = ".*/Log_([0-9]+)\..*"
TIMESTAMP_PATTERN = "%d%m%Y"

if __name__ == '__main__':
    # GUI for open/save Dialog
    root = tk.Tk()
    root.withdraw()
    
    run = True
    while run:
        try:
            source_fullpaths = filedialog.askopenfilenames()
            if not source_fullpaths:
                sys.exit()
            target_fullpath = filedialog.asksaveasfilename(
                confirmoverwrite = True,
                defaultextension = "",
                filetypes=[("Text File", "*.txt"), ("Extensible Markup Languaage", "*.xml")]
            )
            if not target_fullpath:
                sys.exit()

            # filenames.sort(key=lambda date: datetime.strptime(date, "%m-%Y"))
            items = [(source_fullpath, re.search(FILENAME_PATTERN, source_fullpath).group(1)) \
                for source_fullpath in source_fullpaths]
            items.sort(key=lambda date: datetime.strptime(date[1], TIMESTAMP_PATTERN))
            with open(target_fullpath, "w", encoding="utf-8") as target_file:
                for item in items:
                    with open(item[0], "r", encoding="utf-8") as source_file:
                        target_file.write(f"Date: {item[1]}\n")
                        target_file.write(source_file.read())
                        target_file.write("\n")
            tk.messagebox.showinfo("Info", "Merge Success")
        except AttributeError:
            tk.messagebox.showerror("Error", f"Error occured:\nInput filename should match:\n{FILENAME_PATTERN}")
        run = tk.messagebox.askyesno("Continue?", "Start Next Merge?")
    sys.exit()
