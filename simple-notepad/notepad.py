import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

class MainApplication(tk.Frame):

    def __init__(self, *args, **kwargs): #,parent
        tk.Frame.__init__(self, *args, **kwargs) #,parent
        # self.parent = parent

        window.title("Word Editor")
        window.rowconfigure(1, minsize=800, weight=1)
        window.columnconfigure(0, minsize=800, weight=1)

        self.tkvar = tk.StringVar(window)
        self.choices = {'Default Font', 'Times New Roman', 'Century', 'Comic Sans MS', 'Agency FB'}
        self.tkvar.set('Default Font')  # set the default option
        self.bolded = False
        self.font = 'Default Font'
        self.size = 12
        self.txt_edit = tk.Text(window, font=(self.font, self.size))

        fr_buttons = tk.Frame(window)
        btn_open = tk.Button(fr_buttons, text="Open",command=self.openFile)
        btn_save = tk.Button(fr_buttons, text="Save As...",command = self.saveFile)
        btn_bold = tk.Button(fr_buttons, text="Bold",command=self.bold)
        btn_clear = tk.Button(fr_buttons, text="Clear Formatting",command=self.clear)
        popupMenu = tk.OptionMenu(fr_buttons, self.tkvar, *self.choices)

        btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_save.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        btn_bold.grid(row=0, column=2, sticky="ew", padx=5, pady=5)
        popupMenu.grid(row=0, column=3)
        btn_clear.grid(row=0, column=4, sticky="ew", padx=5, pady=5)

        fr_buttons.grid(row=0, column=0)
        self.txt_edit.grid(row=1, column=0, sticky="nsew")
        self.tkvar.trace('w', self.change_font)

    def openFile(self):
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if not filepath:
            return
        self.txt_edit.delete("1.0", tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            self.txt_edit.insert(tk.END, text)
        window.title(f"Simple Text Editor - {filepath}")

    def saveFile(self):
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = self.txt_edit.get("1.0", tk.END)
            output_file.write(text)
        window.title(f"Simple Text Editor - {filepath}")

    def bold(self):
        if self.bolded == False:
            text = self.txt_edit.get(index1=1.0, index2=100.0)
            self.txt_edit = tk.Text(window, font=(self.font, 11, 'bold'))
            self.txt_edit.grid(row=1, column=0, sticky="nsew")
            self.txt_edit.insert(1.0, text)
            self.bolded = True

        elif self.bolded == True:
            text = self.txt_edit.get(index1=1.0, index2=100.0)
            self.txt_edit = tk.Text(window, font=(self.font, 11))
            self.txt_edit.grid(row=1, column=0, sticky="nsew")
            self.txt_edit.insert(1.0, text)
            self.bolded = False

    def clear(self):

        text = self.txt_edit.get(index1=1.0, index2=100.0)
        self.txt_edit = tk.Text(window, font=('freemono', 11))
        self.txt_edit.grid(row=1, column=0, sticky="nsew")
        self.txt_edit.insert(1.0, text)
        self.bolded = False

    def change_font(self,*args):
        if self.bolded == True:
            bold = 'bold'
        else:
            bold = ''
        self.font = self.tkvar.get()
        text = self.txt_edit.get(index1=1.0, index2=100.0)
        self.txt_edit = tk.Text(window, font=(self.font, 11,bold))
        self.txt_edit.grid(row=1, column=0, sticky="nsew")
        self.txt_edit.insert(1.0, text)

if __name__ == "__main__":
    window = tk.Tk()
    MainApplication(window).grid()
    window.mainloop()
