# coding=UTF-8
# this is GUI Decorator
import tkinter as tk


def display_info(func):
    def wrapper(*args, **kwargs):
        root = tk.Tk()
        root.title('输出文本:')

        text = tk.Text(root)
        text.grid(row=0, column=1)
        tk.Button(root, text='关闭', command=quit).grid(row=1, column=1)

        msg = func(*args, **kwargs)
        print('msg is {}'.format(msg))

        if msg:
            if isinstance(msg, (list, tuple)):
                for index, line in enumerate(msg):
                    text.insert(tk.END, 'line' + str(index+1) + ': \n' + str(line) + '\n\n')
            else:
                text.insert(tk.END, str(msg) + '\n')

            # 让GUI始终处于居中位置
            root.update_idletasks()
            x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
            y = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
            root.geometry('+%d+%d' % (x, y))
            root.mainloop()
    return wrapper


@display_info
def temp_info():
    return 'Hello world!', 'evan'


if __name__ == '__main__':
    temp_info()
