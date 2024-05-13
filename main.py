import tkinter as tk
import clipboard as cb
import random as rd

import image_parameters as ip

TEXT_COLOR = 'black'
TEXT_FONT = 'arial.ttf'
TEXT_SIZE = 12

class SDPromptGeneratorApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # create the tkinter UI basic structure
        self.config(padx=600, pady=800)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=4)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)

        # put widget on UI
        # self.canvas = tk.Canvas(width=200, height=150, bg="#f7f5dd", highlightthickness=0)
        # self.canvas.grid(row=1, column=1)
        # self.start_button = tk.Button(width=10, height=1, text="Select Image", command=ask_directory)
        # self.start_button.grid(column=0, row=0)
        self.subject_label = tk.Label(self.parent,
                                           text="Subject:",
                                           font=(TEXT_FONT, TEXT_SIZE))
        self.subject_label.grid(row=0, column=0)
        self.background_label = tk.Label(self.parent,
                                           text="Background:",
                                           font=(TEXT_FONT, TEXT_SIZE))
        self.background_label.grid(row=1, column=0)
        self.style_label = tk.Label(self.parent,
                                           text="Style:",
                                           font=(TEXT_FONT, TEXT_SIZE))
        self.style_label.grid(row=2, column=0)
        self.angle_label = tk.Label(self.parent,
                                           text="Angle:",
                                           font=(TEXT_FONT, TEXT_SIZE))
        self.angle_label.grid(row=3, column=0)
        self.lighting_label = tk.Label(self.parent,
                                           text="Lighting:",
                                           font=(TEXT_FONT, TEXT_SIZE))
        self.lighting_label.grid(row=4, column=0)
        self.palette_label = tk.Label(self.parent,
                                           text="Palette:",
                                           font=(TEXT_FONT, TEXT_SIZE))
        self.palette_label.grid(row=5, column=0)
        self.effect_label = tk.Label(self.parent,
                                           text="Special Effect:",
                                           font=(TEXT_FONT, TEXT_SIZE))
        self.effect_label.grid(row=6, column=0)
        self.feature_label = tk.Label(self.parent,
                                           text="Additional Features:",
                                           font=(TEXT_FONT, TEXT_SIZE))
        self.feature_label.grid(row=7, column=0)

        self.subject_entry = tk.Entry(self.parent)
        self.subject_entry.grid(row=0, column=1)
        self.background_entry = tk.Entry(self.parent)
        self.background_entry.grid(row=1, column=1)

        # print(ip.style_list[1])

        self.style_list = ip.style_list
        self.style_var = tk.StringVar()
        self.style_var.set(ip.NONE_STRING)
        self.style_menu = tk.OptionMenu(self.parent,self.style_var,*self.style_list)
        self.style_menu.grid(row=2, column=1)

        self.angle_list = ip.camera_angle_list
        self.angle_var = tk.StringVar()
        self.angle_var.set(ip.NONE_STRING)
        self.angle_menu = tk.OptionMenu(self.parent,self.angle_var,*self.angle_list)
        self.angle_menu.grid(row=3, column=1)

        self.light_list = ip.lighting_list
        self.light_var = tk.StringVar()
        self.light_var.set(ip.NONE_STRING)
        self.light_menu = tk.OptionMenu(self.parent,self.light_var,*self.light_list)
        self.light_menu.grid(row=4, column=1)

        self.color_list = ip.color_palette_list
        self.color_var = tk.StringVar()
        self.color_var.set(ip.NONE_STRING)
        self.color_menu = tk.OptionMenu(self.parent,self.color_var,*self.color_list)
        self.color_menu.grid(row=5, column=1)

        self.misc_list = ip.additional_features_list
        self.misc_var = tk.StringVar()
        self.misc_var.set(ip.NONE_STRING)
        self.misc_menu = tk.OptionMenu(self.parent,self.misc_var,*self.misc_list)
        self.misc_menu.grid(row=6, column=1)

        self.effect_list = ip.special_effects_list
        self.effect_var = tk.StringVar()
        self.effect_var.set(ip.NONE_STRING)
        self.effect_menu = tk.OptionMenu(self.parent,self.effect_var,*self.effect_list)
        self.effect_menu.grid(row=7, column=1)

        self.generate_button = tk.Button(self.parent,text="Generate Prompt", command=self.GeneratePrompt)
        self.generate_button.grid(row=1, column=2)

        self.copy_button = tk.Button(self.parent,text="Copy to Clipboard", command=self.CopyPrompt)
        self.copy_button.grid(row=2, column=2)

        self.random_button = tk.Button(self.parent,text="Randomize", command=self.Randomize)
        self.random_button.grid(row=3, column=2)

        self.clear_button = tk.Button(self.parent,text="Clear", command=self.Clear)
        self.clear_button.grid(row=4, column=2)

        self.prompt_text = tk.Text(self.parent, height=8)
        self.prompt_text.grid(row=2, column=3)

    # def style_func(self,value):
    #     return value

    def GeneratePrompt(self):
        # print("Generate Prompt")
        # self.prompt_text.insert('1.0',"test")
        subject_text=self.subject_entry.get()
        if len(subject_text)>0:
            subject_text+=", "
        self.prompt_text.insert(tk.END,subject_text)

        background_text = self.background_entry.get()
        if len(background_text) > 0:
            background_text += " in the background"
        self.prompt_text.insert(tk.END, background_text)

        style_text = self.style_var.get()
        if style_text != ip.NONE_STRING:
            style_text += " of "
            self.prompt_text.insert('1.0', style_text)

        angle_text = self.angle_var.get()
        if angle_text != ip.NONE_STRING:
            angle_text = ", " + angle_text
            self.prompt_text.insert(tk.END, angle_text)

        light_text = self.light_var.get()
        if light_text != ip.NONE_STRING:
            light_text = ", " + light_text
            self.prompt_text.insert(tk.END, light_text)

        color_text = self.color_var.get()
        if color_text != ip.NONE_STRING:
            color_text = ", " + color_text
            self.prompt_text.insert(tk.END, color_text)

        effect_text = self.effect_var.get()
        if effect_text != ip.NONE_STRING:
            effect_text = ", " + effect_text
            self.prompt_text.insert(tk.END, effect_text)

        misc_text = self.misc_var.get()
        if misc_text != ip.NONE_STRING:
            misc_text = ", " + misc_text
            self.prompt_text.insert(tk.END, misc_text)



    def CopyPrompt(self):
        text_to_copy = self.prompt_text.get('1.0', tk.END)
        cb.copy(text_to_copy)
        # print("Copy Prompt to Clipboard")

    def Randomize(self):
        # print("Randomize")
        self.style_var.set(rd.choice(self.style_list))
        self.angle_var.set(rd.choice(self.angle_list))
        self.light_var.set(rd.choice(self.light_list))
        self.angle_var.set(rd.choice(self.angle_list))
        self.color_var.set(rd.choice(self.color_list))
        self.effect_var.set(rd.choice(self.effect_list))
        self.misc_var.set(rd.choice(self.misc_list))

    def Clear(self):
        # print("Clear")
        self.prompt_text.delete('1.0', tk.END)



if __name__ == "__main__":
    window = tk.Tk()
    window.title = "Stable Diffusion Prompt Generating Application"
    SDPromptGeneratorApp(window)
    window.mainloop()
