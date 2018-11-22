from tkinter import Label,Tk,StringVar,messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Entry,Button
from md5校验.md5_test import md5_check,change_md5


class App(object):
    def __init__(self):
        self.w=Tk()
        self.w.title('md5校验与修改')
        self.w.geometry('360x400')
        self.make_res()
        self.res_config()
        self.w.mainloop()

    def make_res(self):
        self.E_var=StringVar()
        self.L_file=Label(self.w,fg='red')
        self.E_file=Entry(self.w,textvariable=self.E_var)
        self.B_choose=Button(self.w,text='选择')
        self.L_md5_message=Label(self.w,bg='#C6E2FF')
        self.L_md5_info=Label(self.w,text='MD5:',fg='#B03060')
        self.L_sha1_message=Label(self.w,bg='#C6E2FF')
        self.L_sha1_info=Label(self.w,text='SHA1:',fg='#1874CD')
        self.B_change=Button(self.w,text='修改MD5')
        self.L_new_md5_message = Label(self.w, bg='#C6E2FF')
        self.L_new_md5_info = Label(self.w, text='MD5:', fg='#B03060')
        self.L_new_sha1_message = Label(self.w, bg='#C6E2FF')
        self.L_new_sha1_info = Label(self.w, text='SHA1:', fg='#1874CD')
        self.L_new_message=Label(self.w,bg='#7EC0EE')
        self.L_new_info=Label(self.w,text='复制:',fg='red')
        self.res_place()#设置坐标

    def res_place(self):
        self.L_file.place(x=50,y=5,width=200,height=30)
        self.E_file.place(x=50,y=40,width=230,height=30)
        self.B_choose.place(x=300,y=40,width=50,height=30)
        self.L_md5_message.place(x=50,y=80,width=300,height=30)
        self.L_md5_info.place(x=5,y=80,width=32,height=30)
        self.L_sha1_message.place(x=50,y=120,width=300,height=30)
        self.L_sha1_info.place(x=5,y=120,width=32,height=30)
        self.B_change.place(x=50,y=160,width=70,height=30)
        self.L_new_md5_message.place(x=50,y=230,width=300,height=30)
        self.L_new_md5_info.place(x=5,y=230,width=32,height=30)
        self.L_new_sha1_message.place(x=50,y=270,width=300,height=30)
        self.L_new_sha1_info.place(x=5,y=270,width=32,height=30)
        self.L_new_message.place(x=50,y=195,width=300,height=30)
        self.L_new_info.place(x=5,y=195,width=40,height=30)

    def res_config(self):
        self.L_file.config(text='请选择文件或者输入文件路径')
        self.B_choose.config(command=self.select_config)
        self.B_change.config(command=self.change_file_md5)

    def select_config(self):#如果路径非空，直接执行校验，路径报错弹出警告
        if self.E_var.get()!='':
            self.view_md5()
        else:
            self.file_path=askopenfilename()
            self.E_var.set(self.file_path)
            self.view_md5()


    def view_md5(self):#显示md5码
        try:
            md5_str,sha1_str=md5_check(self.E_var.get())
            self.L_md5_message.config(text=md5_str)
            self.L_sha1_message.config(text=sha1_str)
            print('md5:',md5_str)
            print('sha1:',sha1_str)
        except Exception:
            messagebox.showwarning(title='警告',message='请选择正确的文件')

    def change_file_md5(self):
        print('修改')
        if self.E_var.get()=='':
            messagebox.showwarning(title='警告',message='请选择文件')
        else:
            try:
               md5_check(self.E_var.get())
               new_file_name, md5_str, sha1_str=change_md5(self.E_var.get())
               self.L_new_message.config(text=new_file_name)
               self.L_new_md5_message.config(text=md5_str)
               self.L_new_sha1_message.config(text=sha1_str)
            except Exception:
                messagebox.showwarning(title='警告', message='请选择正确的文件')


a=App()