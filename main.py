import tkinter as tk
from tkinter import ttk
from PIL import Image
from respone_in_ai import get_response_stream_generate_from_ChatGPT_API
import keyboard
from pynput.mouse import Controller as MouseController
import pyperclip
import threading
import pystray
from pystray import MenuItem as item

class TopLevelApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("W-GPT")
        self.root.withdraw()
        self.accumulated_content = ""
        self.is_ctrl_c_pressed = False
        style = ttk.Style()
        self.root.iconbitmap('./favicon.ico')
        self.root.protocol("WM_DELETE_WINDOW", self.hide_window)
        style.configure('TLabel', font=('Helvetica', 10), background='light grey')
        self.combobox = ttk.Combobox(self.root,values=["学术GPT", "翻译GPT", "代码GPT"])
        self.combobox.pack(padx=10, pady=10)
        self.combobox.bind("<<ComboboxSelected>>", self.on_combobox_select)
        self.combobox.set("学术GPT")
        # 使用 TTK Label
        self.label = ttk.Label(self.root, text="学术GPT", wraplength=500, style='TLabel')
        self.label.pack(padx=10, pady=10)

        self.root.configure(bg='light grey')
        self.root.attributes('-topmost', True)

        button_frame = ttk.Frame(self.root)
        button_frame.pack(padx=10, pady=10)

        # 创建并使用 grid 布局放置按钮
        self.copy_button = ttk.Button(button_frame, text="复制内容", command=self.copy_content)
        self.copy_button.grid(row=0, column=0, padx=5, pady=10)

        self.exit_button = ttk.Button(button_frame, text="退出程序", command=self.close_app)
        self.exit_button.grid(row=0, column=1, padx=5, pady=10)

    def run_in_thread(self, fn):
        thread = threading.Thread(target=fn)
        thread.start()

    def create_system_tray_icon(self):
        # 创建托盘图标
        icon = pystray.Icon("W-GPT")
        icon.menu = pystray.Menu(
            item("显示/隐藏窗口", self.toggle_window_visibility),
            item("退出", self.close_app_from_tray)
        )
        icon.icon = Image.open('./favicon.ico')
        icon.run()
    def toggle_window_visibility(self, icon, item):
        # 切换窗口的可见性
        if self.root.state() == "withdrawn":
            self.root.deiconify()
        else:
            self.root.withdraw()

    def close_app_from_tray(self, icon, item):
        # 从托盘退出应用
        icon.stop()
        self.root.destroy()
        exit()
    def hide_window(self):
        # 隐藏窗口而不是完全退出程序
        self.root.withdraw()
    def close_app(self):
        # 完全结束程序
        self.root.destroy()
        exit()

    def copy_content(self):
        content = self.label.cget("text")
        pyperclip.copy(content)

    def on_combobox_select(self):
        selected_option = self.combobox.get()
        if selected_option == "学术GPT":
            return 1
        elif selected_option == "翻译GPT":
            return 2
        elif selected_option == "代码GPT":
            return 3
    def show_copied_content(self):
        selected_text = pyperclip.paste()
        return selected_text

    def generate_content(self):
        type = self.on_combobox_select()
        print(type)
        gen = get_response_stream_generate_from_ChatGPT_API(self.show_copied_content(),type)
        for i in gen():
            yield i

    def update_content(self):
        try:
            content = next(self.content_generator)
            self.accumulated_content += content
            self.label.config(text=self.accumulated_content)
            self.root.after(10, self.update_content)
        except StopIteration:
            self.root.attributes('-topmost', False)
            pass  # 所有内容显示完毕

    def reset_ui_and_generate_new_content(self):
        self.show_window_at_mouse()
        self.accumulated_content = ""
        self.label.config(text=self.accumulated_content)
        self.content_generator = self.generate_content()
        self.update_content()

    def on_ctrl_c_pressed(self):
        if self.is_ctrl_c_pressed:
            self.reset_ui_and_generate_new_content()
            self.is_ctrl_c_pressed = False
        else:
            self.is_ctrl_c_pressed = True
            threading.Timer(0.5, self.reset_ctrl_c_flag).start()

    def reset_ctrl_c_flag(self):
        self.is_ctrl_c_pressed = False

    def show_window_at_mouse(self):
        self.root.attributes('-topmost', True)
        mouse = MouseController()
        x, y = mouse.position
        self.root.geometry(f"+{x}+{y + 50}")
        self.root.deiconify()

    def run(self):
        self.root.mainloop()

def main():
    app = TopLevelApp()
    keyboard.add_hotkey('ctrl+c', app.on_ctrl_c_pressed)
    # app.create_system_tray_icon() 当添加到系统时无法正常使用，就是无法触发快捷键，不知道为什么
    app.run()

if __name__ == "__main__":
    main()
