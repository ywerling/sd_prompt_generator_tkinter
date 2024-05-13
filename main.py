import tkinter as tk

class SDPromptGeneratorApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # create the tkinter UI basic structure
        self.config(padx=400, pady=300)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.rowconfigure(2, weight=1)

        # put widget on UI
        self.canvas = tk.Canvas(width=200, height=150, bg="#f7f5dd", highlightthickness=0)
        self.canvas.grid(row=1, column=1)
        # self.start_button = tk.Button(width=10, height=1, text="Select Image", command=ask_directory)
        # self.start_button.grid(column=0, row=0)
        self.image_location = tk.Entry(width=35)
        self.image_location.grid(column=1, row=0)


if __name__ == "__main__":
    window = tk.Tk()
    window.title="Stable Diffusion Prompt Generating Application"
    SDPromptGeneratorApp(window)
    window.mainloop()