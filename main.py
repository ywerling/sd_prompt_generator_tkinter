import tkinter as tk
import clipboard as cb
import random as rd

import image_parameters as ip

# hard coded UI parameters
TEXT_COLOR = 'black'
TEXT_FONT = 'arial.ttf'
TEXT_SIZE = 12


class SDPromptGeneratorApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure_ui()
        self.create_widgets()

        # create the tkinter UI basic structure
    def configure_ui(self):
        self.config(padx=25, pady=25)

        # columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=4)

        # rows
        for i in range(8):
            self.rowconfigure(i, weight=1)

        # if the rows need various weights uncomment and adjust
        # self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, weight=1)
        # self.rowconfigure(2, weight=1)
        # self.rowconfigure(3, weight=1)
        # self.rowconfigure(4, weight=1)
        # self.rowconfigure(5, weight=1)
        # self.rowconfigure(6, weight=1)
        # self.rowconfigure(7, weight=1)

    def create_widgets(self):
        # create labels
        self.subject_label = tk.Label(self.parent,
                                      text="Subject:",
                                      font=(TEXT_FONT, TEXT_SIZE),
                                      anchor='w',
                                      justify="left")
        self.subject_label.grid(row=0, column=0)
        self.background_label = tk.Label(self.parent,
                                         text="Background:",
                                         font=(TEXT_FONT, TEXT_SIZE),
                                         justify="left")
        self.background_label.grid(row=1, column=0)
        self.style_label = tk.Label(self.parent,
                                    text="Style:",
                                    font=(TEXT_FONT, TEXT_SIZE),
                                    justify="left")
        self.style_label.grid(row=2, column=0)
        self.angle_label = tk.Label(self.parent,
                                    text="Angle:",
                                    font=(TEXT_FONT, TEXT_SIZE),
                                    justify="left")
        self.angle_label.grid(row=3, column=0)
        self.lighting_label = tk.Label(self.parent,
                                       text="Lighting:",
                                       font=(TEXT_FONT, TEXT_SIZE),
                                       justify="left")
        self.lighting_label.grid(row=4, column=0)
        self.palette_label = tk.Label(self.parent,
                                      text="Palette:",
                                      font=(TEXT_FONT, TEXT_SIZE),
                                      justify="left")
        self.palette_label.grid(row=5, column=0)
        self.effect_label = tk.Label(self.parent,
                                     text="Special Effect:",
                                     font=(TEXT_FONT, TEXT_SIZE),
                                     justify="left")
        self.effect_label.grid(row=6, column=0)
        self.feature_label = tk.Label(self.parent,
                                      text="Additional Features:",
                                      font=(TEXT_FONT, TEXT_SIZE),
                                      justify="left")
        self.feature_label.grid(row=7, column=0)

        # create  text entry boxes
        self.subject_entry = tk.Entry(self.parent)
        self.subject_entry.grid(row=0, column=1)
        self.background_entry = tk.Entry(self.parent)
        self.background_entry.grid(row=1, column=1)

        # create drop down boxes
        self.style_list = ip.STYLE_LIST
        self.style_var = tk.StringVar()
        self.style_var.set(ip.NONE_STRING)
        self.style_menu = tk.OptionMenu(self.parent, self.style_var, *self.style_list)
        self.style_menu.grid(row=2, column=1)

        self.angle_list = ip.CAMERA_ANGLE_LIST
        self.angle_var = tk.StringVar()
        self.angle_var.set(ip.NONE_STRING)
        self.angle_menu = tk.OptionMenu(self.parent, self.angle_var, *self.angle_list)
        self.angle_menu.grid(row=3, column=1)

        self.light_list = ip.LIGHTING_LIST
        self.light_var = tk.StringVar()
        self.light_var.set(ip.NONE_STRING)
        self.light_menu = tk.OptionMenu(self.parent, self.light_var, *self.light_list)
        self.light_menu.grid(row=4, column=1)

        self.color_list = ip.COLOR_PALETTE_LIST
        self.color_var = tk.StringVar()
        self.color_var.set(ip.NONE_STRING)
        self.color_menu = tk.OptionMenu(self.parent, self.color_var, *self.color_list)
        self.color_menu.grid(row=5, column=1)

        self.misc_list = ip.ADDITIONAL_FEATURES_LIST
        self.misc_var = tk.StringVar()
        self.misc_var.set(ip.NONE_STRING)
        self.misc_menu = tk.OptionMenu(self.parent, self.misc_var, *self.misc_list)
        self.misc_menu.grid(row=6, column=1)

        self.effect_list = ip.SPECIAL_EFFECTS_LIST
        self.effect_var = tk.StringVar()
        self.effect_var.set(ip.NONE_STRING)
        self.effect_menu = tk.OptionMenu(self.parent, self.effect_var, *self.effect_list)
        self.effect_menu.grid(row=7, column=1)

        # create buttons
        self.generate_button = tk.Button(self.parent, text="Generate Prompt", command=self.generate_prompt)
        self.generate_button.grid(row=1, column=2)

        self.copy_button = tk.Button(self.parent, text="Copy to Clipboard", command=self.copy_prompt)
        self.copy_button.grid(row=2, column=2)

        self.random_button = tk.Button(self.parent, text="Randomize", command=self.randomize)
        self.random_button.grid(row=3, column=2)

        self.clear_button = tk.Button(self.parent, text="Clear", command=self.clear)
        self.clear_button.grid(row=4, column=2)

        # create prompt editor
        self.prompt_text = tk.Text(self.parent, height=8)
        self.prompt_text.grid(row=2, column=3)

    # def style_func(self,value):
    #     return value

    def generate_prompt(self):
        self.clear()

        # start with the subject
        subject_text = self.subject_entry.get()
        if len(subject_text) > 0:
            subject_text += ", "
        self.prompt_text.insert(tk.END, subject_text)

        # specify the background
        background_text = self.background_entry.get()
        if len(background_text) > 0:
            background_text += " in the background"
        self.prompt_text.insert(tk.END, background_text)

        # if present the prompt starts with the style
        style_text = self.style_var.get()
        if style_text != ip.NONE_STRING:
            style_text += " of "
            self.prompt_text.insert('1.0', style_text)

        # if present add the camera angle
        angle_text = self.angle_var.get()
        if angle_text != ip.NONE_STRING:
            angle_text = ", " + angle_text
            self.prompt_text.insert(tk.END, angle_text)

        # if present add the light condition
        light_text = self.light_var.get()
        if light_text != ip.NONE_STRING:
            light_text = ", " + light_text
            self.prompt_text.insert(tk.END, light_text)

        # if present add the color palette
        color_text = self.color_var.get()
        if color_text != ip.NONE_STRING:
            color_text = ", " + color_text
            self.prompt_text.insert(tk.END, color_text)

        # if present add a special effect
        effect_text = self.effect_var.get()
        if effect_text != ip.NONE_STRING:
            effect_text = ", " + effect_text
            self.prompt_text.insert(tk.END, effect_text)

        # if present add additional prompt information
        misc_text = self.misc_var.get()
        if misc_text != ip.NONE_STRING:
            misc_text = ", " + misc_text
            self.prompt_text.insert(tk.END, misc_text)

    def copy_prompt(self):
        # copy the prompt text to the Windows clipboard
        text_to_copy = self.prompt_text.get('1.0', tk.END)
        cb.copy(text_to_copy)

    def randomize(self):
        # set the drop-down items to random elements
        self.style_var.set(rd.choice(self.style_list))
        self.angle_var.set(rd.choice(self.angle_list))
        self.light_var.set(rd.choice(self.light_list))
        self.angle_var.set(rd.choice(self.angle_list))
        self.color_var.set(rd.choice(self.color_list))
        self.effect_var.set(rd.choice(self.effect_list))
        self.misc_var.set(rd.choice(self.misc_list))

    def clear(self):
        # clear the prompt text
        self.prompt_text.delete('1.0', tk.END)


if __name__ == "__main__":
    window = tk.Tk()
    window.title = "Stable Diffusion Prompt Generating Application"
    SDPromptGeneratorApp(window)
    window.mainloop()
