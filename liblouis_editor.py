import tkinter as tk
from tkinter import filedialog
import liblouis

class LiblouisTableEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Liblouis Table Editor")
        
        self.editor_frame = tk.Frame(self.root)
        self.editor_frame.pack(fill=tk.BOTH, expand=True)
        
        self.text_widget = tk.Text(self.editor_frame, wrap="word")
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.scrollbar = tk.Scrollbar(self.editor_frame, command=self.text_widget.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill='y')
        self.text_widget.config(yscrollcommand=self.scrollbar.set)
        
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)
        
        self.current_file = ""
    
    def open_file(self):
        self.current_file = filedialog.askopenfilename(filetypes=(("Liblouis tables", "*.utb"), ("All files", "*.*")))
        if self.current_file:
            with open(self.current_file, "r") as f:
                content = f.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)
                
    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w") as f:
                content = self.text_widget.get(1.0, tk.END)
                f.write(content)
                tk.messagebox.showinfo("Save", "File saved successfully.")
        else:
            self.save_file_as()
            
    def save_file_as(self):
        self.current_file = filedialog.asksaveasfilename(defaultextension=".utb", filetypes=(("Liblouis tables", "*.utb"), ("All files", "*.*")))
        if self.current_file:
            self.save_file()

if __name__ == "__main__":
    root = tk.Tk()
    app = LiblouisTableEditor(root)
    root.mainloop()
