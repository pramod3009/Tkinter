import tkinter as tk
from tkinter import *
from ttk import Frame, Button, Style
from tkinter import messagebox as tkMessageBox
TITLE_FONT = ("Helvetica", 18, "bold")

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo,PageThree,PageFour,PageFive,PageSix,PageSeven,PageEight):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

            frame.configure(bg="#a1dbcd")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        self.columnconfigure(0, pad=20)
        self.columnconfigure(1, pad=20)
        self.columnconfigure(2, pad=20)
        self.columnconfigure(3, pad=20)

        self.rowconfigure(0, pad=20)
        self.rowconfigure(1, pad=20)
        self.rowconfigure(2, pad=20)
        self.rowconfigure(3, pad=20)
        self.rowconfigure(4, pad=20)

        self.instr1=Label(self,bg='gray12',fg="white" ,width =125,justify=RIGHT, height=6,text="TOOLS ANALYZER")
        self.instr1.configure(font=("Times New Roman", 14, "bold"))
        self.instr1.grid(row=0,column=1, columnspan=4, sticky=W+E)


        self.columnconfigure(0, pad=1)
        self.columnconfigure(1, pad=1)
        self.columnconfigure(2, pad=1)
        self.columnconfigure(3, pad=1)
        self.columnconfigure(4, pad=1)
        self.columnconfigure(6, pad=1)
        self.rowconfigure(0, pad=40)
        self.rowconfigure(1, pad=40)
        self.rowconfigure(2, pad=40)
        self.rowconfigure(3, pad=40)
        self.rowconfigure(4, pad=40)
        self.rowconfigure(10, pad=180)

        self.pack(fill=BOTH, expand=True)


        self.lbl = Label(self, text="SEARCH FOR YOUR TOOL",bg="#a1dbcd")
        self.lbl.configure(font=("Times New Roman", 12, "bold"))
        self.lbl.grid(sticky=W,row=3,column=2, pady=10, padx=5)


        self.text1=Text(self,width=50,height=2)
        self.text1.grid(row=4,column=3,sticky=W)
        self.text1.insert(0.0,"insert your statement here")
        self.top1=Label(self,fg="black",text="Search tools for:Android\n\t     Java\n\t            Graphics\n\t        C/C++\n                               Electronics\n\t     CAD\n\t             Networks\n\t            Database",bg="#a1dbcd")
        self.top1.configure(font=("Times New Roman", 12, "bold"))
        self.top1.grid(sticky=W,row=3,column=1)



        self.obtn = Button(self, text="SUBMIT",command=self.contains)
        self.obtn.grid(row=10, column=2,columnspan=2,sticky=W)
        self.pack()
    def contains(self):
        input=self.text1.get("1.0","end-1c")
        #print(input)
        for i in ['computer graphics','graphics','cg','opengl','visual basic']:
             if i in input:
                    self.controller.show_frame("PageOne")
                    return
        if "java" in input:
            self.controller.show_frame("PageTwo")
            return
        for i in ['cad','autocad','computer aided design']:
             if i in input:
                 self.controller.show_frame("PageThree")
                 return
        if "android" in input:
            self.controller.show_frame("PageFour")
            return
        for i in ['dbms','database','db','backend']:
             if i in input:
                 self.controller.show_frame("PageFive")
                 return
        for i in  ["networks","cn","computer networks",'protocols','computer network','network','protocol',"wireshark"] :
             if i in input:
                 self.controller.show_frame("PageSix")
                 return
        for i in  ["basic electronic","ec","circuit","multisim"] :
             if i in input:
                 self.controller.show_frame("PageSeven")
                 return
        for i in ["c", "c++","code blocks"]:
            if i in input:
                self.controller.show_frame("PageEight")
                return

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
        self.columnconfigure(0, pad=5)
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, pad=5)
        self.columnconfigure(3, pad=5)
        self.columnconfigure(4, pad=5)
        self.rowconfigure(0, pad=15)
        self.rowconfigure(1, pad=15)
        self.rowconfigure(2, pad=15)
        self.rowconfigure(3, pad=15)
        self.rowconfigure(4, pad=15)
        self.rowconfigure(18, pad=15)
        self.rowconfigure(46, pad=15)
        self.lbl1 = Label(self, text="TOP TOOLS",bg="#a1dbcd")
        self.lbl1.grid(sticky=W, row=2, column=1, pady=1, padx=4)
        self.lbl1.configure(font=("Times New Roman",14,"bold"))
        self.lbl2 = Label(self, text="1.CorelIDRAW",bg="#a1dbcd")
        self.lbl2.grid(sticky=W, row=2, column=2, pady=1, padx=4)
        self.lbl2.configure(font=("Times New Roman",12))
        self.lbl3 = Label(self, text="2.Opengl",bg="#a1dbcd")
        self.lbl3.grid(sticky=W, row=2, column=3, pady=1, padx=4)
        self.lbl3.configure(font=("Times New Roman",12))
        self.lbl4 = Label(self, text="3.DirectX",bg="#a1dbcd")
        self.lbl4.grid(sticky=W, row=2, column=4, pady=1, padx=4)
        self.lbl4.configure(font=("Times New Roman",12))
        self.lbl5 = Label(self, text="4.Vulkan",bg="#a1dbcd")
        self.lbl5.grid(sticky=W, row=2, column=5, pady=1, padx=4)
        self.lbl5.configure(font=("Times New Roman",12))
        #for two big textboxes
        self.tb7 = Text(self, width=55, height=20,font=("Helvetica",11),wrap=WORD)
        self.tb7.grid(row=4, column=0, columnspan=2, sticky=W)
        self.tb8 = Text(self, width=55, height=20,font=("Helvetica",11),wrap=WORD)
        self.tb8.grid(row=4, column=5, columnspan=2, sticky=W)

        #forsmall two textboxes
        self.tb1 = Text(self, width=55, height=5)
        self.tb1.grid(row=18, column=0, sticky=W)
        self.tb1.insert(0.0, "insert tool number to compare here")
        self.tb2 = Text(self, width=55, height=5)
        self.tb2.insert(0.0, "insert tool number to compare here")
        self.tb2.grid(row=18, column=5, sticky=W)

        #buttons
        self.hbtn = Button(self, text="BACK", command=lambda: controller.show_frame("StartPage"))
        self.hbtn.grid(row=46, column=0, columnspan=2, sticky=W)

        self.obtn = Button(self, text="SUBMIT", command=lambda: self.info())
        self.obtn.grid(row=46, column=2, columnspan=2, sticky=W)
    def info(self):
       # print(val)
        self.tb7.configure(state=NORMAL)
        self.tb8.configure(state=NORMAL)

        self.tb7.delete(1.0,END)
        self.tb8.delete(1.0,END)
        cg={'1':"CORELDRAW\n\n1) Memory space : For a nifty program of its size, Corel Draw occupy uses very limited capacity of any machine ie., a computer’s memory.\n----------------------------------------------------------------------------------------2) Performance : Machine works to its full capacity, required very less down-time and the performance never is an issue.\n---------------------------------------------------------------------------------------- 3)Ease of Use :  Also, it is very easy to install on most machines and is OS independent.\n---------------------------------------------------------------------------------------- 4) Platform support : Windows OS or Linux or any other.\n----------------------------------------------------------------------------------------",'2':"OPENGL\n\n1)Memory space : The amount of RAM storage is also limited for the driver and it might return a GL_OUT_OF_MEMORY when you call glGetError()\n----------------------------------------------------------------------------------------2)Performance : The OpenGL API is an open standard, which means that various hardware makers and operating system developers can freely create an OpenGL implementation as part of their system\n----------------------------------------------------------------------------------------3) Ease of Use : Many essential OpenGL extensions and methods, although documented, arealso patented, thus imposing serious legal troubles to implement them.\n----------------------------------------------------------------------------------------4) Platform support :Windows, macOS, and Linux.\n----------------------------------------------------------------------------------------",'3':"DIRECT3D\n\n1) Memory space : If you need more space than available the that's no problem. The driver will move the data between system-ram, AGP-memory and video ram for you.\n---------------------------------------------------------------------------------------- 2)Performance : Direct3D is a proprietary API by Microsoft that provides functions to render two-dimensional (2D) and three-dimensional (3D) graphics, and uses hardware acceleration if available on the graphics card.\n----------------------------------------------------------------------------------------3) Ease of use : Direct3D frees the game programmer from accommodating the graphics hardware.\n----------------------------------------------------------------------------------------4)Platform support : Windows platform.\n----------------------------------------------------------------------------------------",'4':"VULKAN\n\n1) Memory space : reduced load on CPUs through the use of batching, leaving the CPU free to do more computation or rendering than otherwise.\n----------------------------------------------------------------------------------------2) Performance : It can offer higher performance and more balanced CPU/GPU usage, much like Direct3D 12 and Mantle. \n----------------------------------------------------------------------------------------3)Ease of Use : Someone trying to learn what's really going on through Vulkan only understands the abstraction, not the hardware., command queues are more explicit, as are GPU devices, state changes, memory allocation.\n----------------------------------------------------------------------------------------4)Platform Support : Vulkan is available on multiple modern operating systems.\n----------------------------------------------------------------------------------------"}
        point1=self.tb1.get("1.0","end-1c")
        point2=self.tb2.get("1.0","end-1c")
        if point1 > '4' or point2 > '4':
             tkMessageBox.showinfo("TOOLS ANALYZER", "Please insert correct tool number")
        self.tb7.insert(0.0, cg[point1])
        self.tb8.insert(0.0, cg[point2])
        self.tb7.configure(state=DISABLED)
        self.tb8.configure(state=DISABLED)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
        self.columnconfigure(0, pad=5)
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, pad=5)
        self.columnconfigure(3, pad=5)
        self.columnconfigure(4, pad=5)
        self.rowconfigure(0, pad=15)
        self.rowconfigure(1, pad=15)
        self.rowconfigure(2, pad=15)
        self.rowconfigure(3, pad=15)
        self.rowconfigure(4, pad=15)
        self.rowconfigure(18, pad=15)
        self.rowconfigure(46, pad=15)
        self.controller.title("Tools Analyzer")

        #self.pack(fill=BOTH, expand=True)

        self.lbl1 = Label(self, text="TOP TOOLS:",bg="#a1dbcd")
        self.lbl1.grid(sticky=W, row=2, column=1, pady=1, padx=4)
        self.lbl1.configure(font=("Times New Roman", 14, "bold"))
        self.lblj2 = Label(self, text="1.Eclipse",bg="#a1dbcd")
        self.lblj2.grid(sticky=W, row=2, column=2, pady=1, padx=4)
        self.lblj2.configure(font=("Times New Roman", 12))
        self.lblj3 = Label(self, text="2.Netbeans",bg="#a1dbcd")
        self.lblj3.grid(sticky=W, row=2, column=3, pady=1, padx=4)
        self.lblj3.configure(font=("Times New Roman", 12))
        self.lblj4 = Label(self, text="3.IntelliJ IDEA",bg="#a1dbcd")
        self.lblj4.grid(sticky=W, row=2, column=4, pady=1, padx=4)
        self.lblj4.configure(font=("Times New Roman", 12))
        self.lblj5 = Label(self, text="4.JCreator",bg="#a1dbcd")
        self.lblj5.grid(sticky=W, row=2, column=5, pady=1, padx=4)
        self.lblj5.configure(font=("Times New Roman", 12))
        self.hbtn = Button(self, text="BACK", command=lambda: controller.show_frame("StartPage"))
        self.hbtn.grid(row=46, column=0, columnspan=2, sticky=W)
        self.obtn = Button(self, text="SUBMIT", command=lambda: self.info())
        self.obtn.grid(row=46, column=2, columnspan=2, sticky=W)
        self.tb7 = Text(self, width=55, height=20, font=("Helvetica", 11), wrap=WORD)
        self.tb7.grid(row=4, column=0, columnspan=2, sticky=W)
        self.tb8 = Text(self, width=55, height=20, font=("Helvetica", 11), wrap=WORD)
        self.tb8.grid(row=4, column=5, columnspan=2, sticky=W)

        self.tb1 = Text(self, width=55, height=5)
        self.tb1.insert(0.0, "insert tool number to compare here")
        # self.tb1.insert(self,'enter tool number',0)
        self.tb1.grid(row=18, column=0, sticky=W)
        self.tb2 = Text(self, width=55, height=5)
        self.tb2.insert(0.0, "insert tool number to compare here")

        self.tb2.grid(row=18, column=5, sticky=W)

    def info(self):
        # print(val)
        self.tb7.configure(state=NORMAL)
        self.tb8.configure(state=NORMAL)

        self.tb7.delete(1.0, END)
        self.tb8.delete(1.0, END)
        java = {'1': "ECLIPSE\n\n1) Cost : It is free and open source.\n----------------------------------------------------------------------------------------2) Features : It supports many other languages other than JAVA.\n Framework integration like Junit and TestNG and other plugins can be done easily.\n----------------------------------------------------------------------------------------3) Ease of Use : Code Completion\n----------------------------------------------------------------------------------------4) Cons : Eclipse with its plugin eclipseme, is not as up-to-date than Netbeans \n----------------------------------------------------------------------------------------", '2': "NETBEANS\n\n1)Cost : It is free and open source.\n----------------------------------------------------------------------------------------2) Features : Powerful built-in Profiler.\n Natively supports Ant and Maven- no custom built system that only works in the IDE.\n----------------------------------------------------------------------------------------3) Ease of Use : Code completion with JPA and queries.\n----------------------------------------------------------------------------------------4) Cons : Takes up more memory than lighter IDEs.\n----------------------------------------------------------------------------------------", '3': "INTELLIJ\n\n1) Cost : Rs.19,000 to Rs.32,000\n----------------------------------------------------------------------------------------2) Features : A part of debugging process, we often want to evaluate some expression to see its value. With IDEA you don't need to select anything to evaluate .\nYou just put cursor at any place inside your expression (at method hasAttribute in given case) and press Alt+F8. IDEA understands which expression you probably need and shows a dialog window suggesting several possible variants for your expression.\n----------------------------------------------------------------------------------------3) Ease of Use : code inspections, like checkstyle and findbugs, built in and easy to use.\n----------------------------------------------------------------------------------------4) Cons : Expensive.\n----------------------------------------------------------------------------------------", '4': "JCREATOR\n\n1) Cost : Rs.2000 to Rs.5000\n----------------------------------------------------------------------------------------2) Features : Different JDK profiles can be used.\nQuick code writing via project templates.\n----------------------------------------------------------------------------------------3) Ease of Use :  Debugging with an easy, intuitive interface. No command-line prompts necessary.\n----------------------------------------------------------------------------------------4) Cons :  Only available for the Windows operating system, although Wine can be used to run JCreator on Unix systems.\n----------------------------------------------------------------------------------------"}
        point1 = self.tb1.get("1.0", "end-1c")
        point2 = self.tb2.get("1.0", "end-1c")
        if point1 > '4' or point2 > '4':
             tkMessageBox.showinfo("TOOLS ANALYZER", "Please insert correct tool number")
        self.tb7.insert(0.0, java[point1])
        self.tb8.insert(0.0, java[point2])
        self.tb7.configure(state=DISABLED)
        self.tb8.configure(state=DISABLED)
class PageThree(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
            self.columnconfigure(0, pad=5)
            self.columnconfigure(1, pad=5)
            self.columnconfigure(2, pad=5)
            self.columnconfigure(3, pad=5)
            self.columnconfigure(4, pad=5)
            self.rowconfigure(0, pad=15)
            self.rowconfigure(1, pad=15)
            self.rowconfigure(2, pad=15)
            self.rowconfigure(3, pad=15)
            self.rowconfigure(4, pad=15)
            self.rowconfigure(18, pad=15)
            self.rowconfigure(46, pad=15)

            self.lbl1 = Label(self, text="TOP TOOLS:",bg="#a1dbcd")
            self.lbl1.grid(sticky=W, row=2, column=1, pady=1, padx=4)
            self.lbl1.configure(font=("Times New Roman", 14, "bold"))
            self.lbla2 = Label(self, text="1.Autocad",bg="#a1dbcd")
            self.lbla2.grid(sticky=W, row=2, column=2, pady=1, padx=4)
            self.lbla2.configure(font=("Times New Roman", 12))
            self.lbla3 = Label(self, text="2.Solidworks",bg="#a1dbcd")
            self.lbla3.grid(sticky=W, row=2, column=3, pady=1, padx=4)
            self.lbla3.configure(font=("Times New Roman", 12))
            self.lbla4 = Label(self, text="3.VectorWorks",bg="#a1dbcd")
            self.lbla4.grid(sticky=W, row=2, column=4, pady=1, padx=4)
            self.lbla4.configure(font=("Times New Roman", 12))
            self.lbla5 = Label(self, text="4.Draftsight",bg="#a1dbcd")
            self.lbla5.grid(sticky=W, row=2, column=5, pady=1, padx=4)
            self.lbla5.configure(font=("Times New Roman", 12))
            self.hbtn = Button(self, text="BACK", command=lambda:controller.show_frame("StartPage") )
            self.hbtn.grid(row=46, column=0, columnspan=2, sticky=W)
            self.obtn = Button(self, text="SUBMIT", command=lambda: self.info())
            self.obtn.grid(row=46, column=2, columnspan=2, sticky=W)
            self.tb7 = Text(self, width=55, height=20, font=("Helvetica", 11), wrap=WORD)
            self.tb7.grid(row=4, column=0, columnspan=2, sticky=W)
            self.tb8 = Text(self, width=55, height=20, font=("Helvetica", 11), wrap=WORD)
            self.tb8.grid(row=4, column=5, columnspan=2, sticky=W)

            self.tb1 = Text(self, width=55, height=5)
            self.tb1.insert(0.0, "insert tool number to compare here")
            # self.tb1.insert(self,'enter tool number',0)
            self.tb1.grid(row=18, column=0, sticky=W)
            self.tb2 = Text(self, width=55, height=5)
            self.tb2.insert(0.0, "insert tool number to compare here")
            #self.tb2.insert(0.0, "insert here")
            self.tb2.grid(row=18, column=5, sticky=W)

        def info(self):
            # print(val)
            self.tb7.configure(state=NORMAL)
            self.tb8.configure(state=NORMAL)

            self.tb7.delete(1.0, END)
            self.tb8.delete(1.0, END)
            auto = {'1': "AUTOCAD\n\n1) Cost : Rs.15,900\n----------------------------------------------------------------------------------------2) Features : Drawings can be created in 2D or 3D and rotated .\nReduced the design timescales , Reuse of the designs\nThe drawing errors can be corrected easily\nThe drawings can be sent/received via email in seconds\n----------------------------------------------------------------------------------------3) Ease of Use : It is not easy for first-time users to learn the software\n----------------------------------------------------------------------------------------4) Cons : consumes large amounts of the computer processing power\nIt requires high-quality computer hardware that can be costly\nIt requires the advanced manufacturing devices which are very expensive.\n----------------------------------------------------------------------------------------", '2': "SOLIDWORKS\n\n1) Cost : range from Rs. 3,995 to Rs. 8,499.\n----------------------------------------------------------------------------------------2) Features : Faster 2D Drawing Creation \nImproved Large Assembly Performance \nExpanded capabilities for Model Based Definition\n----------------------------------------------------------------------------------------3) Ease of Use : Toolbar is well oriented and simple\nQuick learning is possible.\n----------------------------------------------------------------------------------------4) Cons : Fails to makes detailed drawing using raw data\nImage rendering comes no where near to CATIA or higher versions\n----------------------------------------------------------------------------------------", '3': "VECTORWORKS\n\n1) Cost : $2,595.\n----------------------------------------------------------------------------------------2) Features : It is fully compatible with DWF/DXF/DWG files.\n----------------------------------------------------------------------------------------3) Ease of Use : The program is straightforward to set up and use\n----------------------------------------------------------------------------------------4)Cons : The software requires much computer processing\nsometimes the software does not properly export the DWGs\n----------------------------------------------------------------------------------------", '4': "DRAFTSIGHT\n\n1) Cost : Free.\n----------------------------------------------------------------------------------------2) Features : DraftSight is good for 2D modeling. \nit can save and open DXF and DWG files\noffers macro recording\n----------------------------------------------------------------------------------------3) Ease of Use : it’s good for quick calculations and drawings.\n----------------------------------------------------------------------------------------4) Cons : The free version of DraftSight doesn’t offer much\nit doesn’t run LISP routines and offers no express tools.\n----------------------------------------------------------------------------------------"}
            point1 = self.tb1.get("1.0", "end-1c")
            point2 = self.tb2.get("1.0", "end-1c")
            if point1 > '4' or point2 > '4':
             tkMessageBox.showinfo("TOOLS ANALYZER", "Please insert correct tool number")
            self.tb7.insert(0.0, auto[point1])
            self.tb8.insert(0.0, auto[point2])
            self.tb7.configure(state=DISABLED)
            self.tb8.configure(state=DISABLED)
class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
        self.columnconfigure(0, pad=5)
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, pad=5)
        self.columnconfigure(3, pad=5)
        self.columnconfigure(4, pad=5)
        self.rowconfigure(0, pad=15)
        self.rowconfigure(1, pad=15)
        self.rowconfigure(2, pad=15)
        self.rowconfigure(3, pad=15)
        self.rowconfigure(4, pad=15)
        self.rowconfigure(18, pad=15)
        self.rowconfigure(46, pad=15)

        self.lbl1 = Label(self, text="TOP TOOLS:",bg="#a1dbcd")
        self.lbl1.grid(sticky=W, row=2, column=1, pady=1, padx=4)
        self.lbl1.configure(font=("Times New Roman", 14, "bold"))
        self.lblc2 = Label(self, text="1.Android Studio",bg="#a1dbcd")
        self.lblc2.grid(sticky=W, row=2, column=2, pady=1, padx=4)
        self.lblc2.configure(font=("Times New Roman", 12))
        self.lblc3 = Label(self, text="2.Eclipse",bg="#a1dbcd")
        self.lblc3.grid(sticky=W, row=2, column=3, pady=1, padx=4)
        self.lblc3.configure(font=("Times New Roman", 12))
        self.lblc4 = Label(self, text="3.IntelliJ IDEA",bg="#a1dbcd")
        self.lblc4.grid(sticky=W, row=2, column=4, pady=1, padx=4)
        self.lblc4.configure(font=("Times New Roman", 12))
        self.lblc5 = Label(self, text="4.Xamarin.Android",bg="#a1dbcd")
        self.lblc5.grid(sticky=W, row=2, column=5, pady=1, padx=4)
        self.lblc5.configure(font=("Times New Roman", 12))
        self.hbtn = Button(self, text="BACK", command=lambda: controller.show_frame("StartPage"))
        self.hbtn.grid(row=46, column=0, columnspan=2, sticky=W)
        self.obtn = Button(self, text="SUBMIT", command=lambda: self.info())
        self.obtn.grid(row=46, column=2, columnspan=2, sticky=W)
        self.tb7 = Text(self, width=55, height=20, font=("Helvetica", 11), wrap=WORD)
        self.tb7.grid(row=4, column=0, columnspan=2, sticky=W)
        self.tb8 = Text(self, width=55, height=20, font=("Helvetica", 11), wrap=WORD)
        self.tb8.grid(row=4, column=5, columnspan=2, sticky=W)

        self.tb1 = Text(self, width=55, height=5)
        self.tb1.insert(0.0, "insert tool number to compare here")
        # self.tb1.insert(self,'enter tool number',0)
        self.tb1.grid(row=18, column=0, sticky=W)
        self.tb2 = Text(self, width=55, height=5)
        self.tb2.insert(0.0, "insert tool number to compare here")
        #self.tb2.insert(0.0, "insert here")
        self.tb2.grid(row=18, column=5, sticky=W)

    def info(self):
        # print(val)
        self.tb7.configure(state=NORMAL)
        self.tb8.configure(state=NORMAL)

        self.tb7.delete(1.0, END)
        self.tb8.delete(1.0, END)
        android = {'1': "ANDROID STUDIO\n\n1) Cost : Free\n----------------------------------------------------------------------------------------2) Features : Layouts are built and can be observed in real time\nUses Gradle as the official build tool for projects\nInstant Run allows developers to build their app once and as they change their code\n----------------------------------------------------------------------------------------3) Ease of Use : Layouts are automatically updated after every change.\nYou can even see these changes on different screens.\n----------------------------------------------------------------------------------------4) Cons : The gradle build takes a lot of time to compile the code\n----------------------------------------------------------------------------------------", '2': "ECLIPSE\n\n1) Cost : Free \n----------------------------------------------------------------------------------------2) Features : Has full support for both Java and XML\n----------------------------------------------------------------------------------------3) Ease of Use : Working with eclipse can be difficult at times\nprobably when debugging and designing layouts\nEclipse sometimes get stuck and we have to restart eclipse from time to time.\n----------------------------------------------------------------------------------------4) Cons : Though there are plenty of plugins , they aren't always reliable\nSome aren't maintained\nbug fixes can be slow\n----------------------------------------------------------------------------------------", '3':"INTELLIJ IDEA\n\n1) Cost : $499/1st year\n----------------------------------------------------------------------------------------2) Features : Uses a fast indexing technique to provide contextual hints.\n----------------------------------------------------------------------------------------3) Ease of Use : On-the-fly code analysis to detect errors and propose refactorization.\n----------------------------------------------------------------------------------------4) Cons : running tests is slow because IntelliJ only does (re)compile the test/source when you hit the run button\n----------------------------------------------------------------------------------------", '4': "XAMARIN.ANDROID\n\n1) Cost : free community version \n----------------------------------------------------------------------------------------2) Features : Xamarin is a platform on which you can build cross-platform mobile applications for Android, iOS and Windows Mobile and use only one codebase.\n----------------------------------------------------------------------------------------3) Ease of Use : Using Xamarin is relatively painless and easy.\n----------------------------------------------------------------------------------------4) Cons : Lacking third party library support \n----------------------------------------------------------------------------------------"}
        point1 = self.tb1.get("1.0", "end-1c")
        point2 = self.tb2.get("1.0", "end-1c")
        if point1 > '4' or point2 > '4':
             tkMessageBox.showinfo("TOOLS ANALYZER", "Please insert correct tool number")
        self.tb7.insert(0.0, android[point1])
        self.tb8.insert(0.0, android[point2])
        self.tb7.configure(state=DISABLED)
        self.tb8.configure(state=DISABLED)

class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
        self.columnconfigure(0, pad=5)
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, pad=5)
        self.columnconfigure(3, pad=5)
        self.columnconfigure(4, pad=5)
        self.rowconfigure(0, pad=15)
        self.rowconfigure(1, pad=15)
        self.rowconfigure(2, pad=15)
        self.rowconfigure(3, pad=15)
        self.rowconfigure(4, pad=15)
        self.rowconfigure(18, pad=15)
        self.rowconfigure(46, pad=15)

        self.lbl1 = Label(self, text="TOP TOOLS:",bg="#a1dbcd")
        self.lbl1.grid(sticky=W, row=2, column=1, pady=1, padx=4)
        self.lbl1.configure(font=("Times New Roman", 14, "bold"))
        self.lblc2 = Label(self, text="1.Oracle",bg="#a1dbcd")
        self.lblc2.grid(sticky=W, row=2, column=2, pady=1, padx=4)
        self.lblc2.configure(font=("Times New Roman", 12))
        self.lblc3 = Label(self, text="2.MySQL",bg="#a1dbcd")
        self.lblc3.grid(sticky=W, row=2, column=3, pady=1, padx=4)
        self.lblc3.configure(font=("Times New Roman", 12))
        self.lblc4 = Label(self, text="3.Microsoft Access",bg="#a1dbcd")
        self.lblc4.grid(sticky=W, row=2, column=4, pady=1, padx=4)
        self.lblc4.configure(font=("Times New Roman", 12))
        self.lblc5 = Label(self, text="4.MongoDB",bg="#a1dbcd")
        self.lblc5.grid(sticky=W, row=2, column=5, pady=1, padx=4)
        self.lblc5.configure(font=("Times New Roman", 12))
        self.hbtn = Button(self, text="BACK", command=lambda: controller.show_frame("StartPage"))
        self.hbtn.grid(row=46, column=0, columnspan=2, sticky=W)
        self.obtn = Button(self, text="SUBMIT", command=lambda: self.info())
        self.obtn.grid(row=46, column=2, columnspan=2, sticky=W)
        self.tb7 = Text(self, width=55, height=20, font=("Helvetica", 11), wrap=WORD)
        self.tb7.grid(row=4, column=0, columnspan=2, sticky=W)
        self.tb8 = Text(self, width=55, height=20, font=("Helvetica", 11), wrap=WORD)
        self.tb8.grid(row=4, column=5, columnspan=2, sticky=W)

        self.tb1 = Text(self, width=55, height=5)
        self.tb1.insert(0.0, "insert tool number to compare here")
        # self.tb1.insert(self,'enter tool number',0)
        self.tb1.grid(row=18, column=0, sticky=W)
        self.tb2 = Text(self, width=55, height=5)
        self.tb2.insert(0.0, "insert tool number to compare here")
        #self.tb2.insert(0.0, "insert here")
        self.tb2.grid(row=18, column=5, sticky=W)

    def info(self):
        # print(val)
        self.tb7.configure(state=NORMAL)
        self.tb8.configure(state=NORMAL)

        self.tb7.delete(1.0, END)
        self.tb8.delete(1.0, END)
        dbms = {'1':"ORACLE\n\n1) Cost : Rs.36,500  to Rs.59,500\n----------------------------------------------------------------------------------------2) Features : Oracle Enterprise Server, designed for grid computing, is the best RDBMS, running on multiple platforms, with the latest version 12c, in which the c is for cloud computing.\nOracle Express also has tools and a separate server application. It also has more operating system options than Microsoft SQL Server Express.\n----------------------------------------------------------------------------------------3)  Ease of Use : Built in Administration tools and customizable settings makes it easy to use\n----------------------------------------------------------------------------------------4) Cons : One of the potential disadvantages of using Oracle Database 11G is the cost.\n----------------------------------------------------------------------------------------",'2': "MYSQL\n\n1) Cost : MySQL. an open source database and is free\n----------------------------------------------------------------------------------------2) Features :  MySQL is the most popular database for internet systems such as e-commerce and dynamic website. \nCan be used even when no network is available.\n----------------------------------------------------------------------------------------3) Ease of Use :  Flexible privilege and password system.\n----------------------------------------------------------------------------------------4) Cons : Falls behind others due to slow updates.\n----------------------------------------------------------------------------------------", '3': "MICROSOFT ACCESS\n\n1) Cost : Rs.7000\n----------------------------------------------------------------------------------------2) Features : Ease to integrate – Access works well with many of the developing software programs based in Windows.\n It also can be used in the front-end as back-end tables with products like Microsoft SQL Server and non-Microsoft products like Oracle and Sybase.\nMicrosoft Access makes it easy to import data.\n----------------------------------------------------------------------------------------3) Ease of Use : Easy to install and use — Access gives data managers a fully functional, relational database management system in minutes.\n Like many other Microsoft applications, Access contains Wizards that walk you through each step of the way.\n----------------------------------------------------------------------------------------4) Cons : Multi-user limited — Technical limit is 255 concurrent users, but real world limit is 10 to 80 (depending on type of application).\n----------------------------------------------------------------------------------------", '4': "MONGO DB\n\n1) Cost : free\n----------------------------------------------------------------------------------------2) Features : schema-less. If you have a flexible schema, this is ideal for a document store like MongoDB.\n----------------------------------------------------------------------------------------3) Ease of Use : This is difficult to implement in a performant manner in RDBMS.\n----------------------------------------------------------------------------------------4) Cons : Data size in MongoDB is typically higher due to e.g. each document has field names stored in it.\nless flexibity with querying (e.g. no JOINs).\nno support for transactions - certain atomic operations are supported, at a single document level\n----------------------------------------------------------------------------------------"}
        point1 = self.tb1.get("1.0", "end-1c")
        point2 = self.tb2.get("1.0", "end-1c")
        if point1 > '4' or point2 > '4':
             tkMessageBox.showinfo("TOOLS ANALYZER", "Please insert correct tool number")
        self.tb7.insert(0.0, dbms[point1])
        self.tb8.insert(0.0, dbms[point2])
        self.tb7.configure(state=DISABLED)
        self.tb8.configure(state=DISABLED)
class PageSix(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
        self.columnconfigure(0, pad=5)
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, pad=5)
        self.columnconfigure(3, pad=5)
        self.columnconfigure(4, pad=5)
        self.rowconfigure(0, pad=15)
        self.rowconfigure(1, pad=15)
        self.rowconfigure(2, pad=15)
        self.rowconfigure(3, pad=15)
        self.rowconfigure(4, pad=15)
        self.rowconfigure(18, pad=15)
        self.rowconfigure(46, pad=15)

        self.lbl1 = Label(self, text="TOP TOOLS:",bg="#a1dbcd")
        self.lbl1.grid(sticky=W, row=2, column=1, pady=1, padx=4)
        self.lbl1.configure(font=("Times New Roman", 14, "bold"))
        self.lblc2 = Label(self, text="1.Wireshark",bg="#a1dbcd")
        self.lblc2.grid(sticky=W, row=2, column=2, pady=1, padx=4)
        self.lblc2.configure(font=("Times New Roman", 12))
        self.lblc3 = Label(self, text="2.NAST",bg="#a1dbcd")
        self.lblc3.grid(sticky=W, row=2, column=3, pady=1, padx=4)
        self.lblc3.configure(font=("Times New Roman", 12))
        self.lblc4 = Label(self, text="3.Zenmap",bg="#a1dbcd")
        self.lblc4.grid(sticky=W, row=2, column=4, pady=1, padx=4)
        self.lblc4.configure(font=("Times New Roman", 12))
        self.lblc5 = Label(self, text="4.Angry IP Scanner",bg="#a1dbcd")
        self.lblc5.grid(sticky=W, row=2, column=5, pady=1, padx=4)
        self.lblc5.configure(font=("Times New Roman", 12))
        self.hbtn = Button(self, text="BACK", command=lambda: controller.show_frame("StartPage"))
        self.hbtn.grid(row=46, column=0, columnspan=2, sticky=W)
        self.obtn = Button(self, text="SUBMIT", command=lambda: self.info())
        self.obtn.grid(row=46, column=2, columnspan=2, sticky=W)
        self.tb7 = Text(self, width=55, height=20, font=("Helvetica", 11), wrap=WORD)
        self.tb7.grid(row=4, column=0, columnspan=2, sticky=W)
        self.tb8 = Text(self, width=55, height=20, font=("Helvetica", 11), wrap=WORD)
        self.tb8.grid(row=4, column=5, columnspan=2, sticky=W)

        self.tb1 = Text(self, width=55, height=5)
        # self.tb1.insert(self,'enter tool number',0)
        self.tb1.grid(row=18, column=0, sticky=W)
        self.tb1.insert(0.0, "insert tool number to compare here")
        self.tb2 = Text(self, width=55, height=5)
        self.tb2.insert(0.0, "insert tool number to compare here")
        #self.tb2.insert(0.0, "insert here")
        self.tb2.grid(row=18, column=5, sticky=W)

    def info(self):
        # print(val)
        self.tb7.configure(state=NORMAL)
        self.tb8.configure(state=NORMAL)

        self.tb7.delete(1.0, END)
        self.tb8.delete(1.0, END)
        cn = {'1': "WIRESHARK\n\n1) Cost : Free \n----------------------------------------------------------------------------------------2) Features : Live capture and offline analysis\nstandard three-pane packet browser\nmulti-platform (Windows, Linux, OS X, Solaris, FreeBSD, NetBSD, and many others)\ncaptured network data can be browsed via GUI, or via the TTY-mode TShark utility.\n----------------------------------------------------------------------------------------3) Ease of Use : coloring rules makes it easier to analyze protocols.\n----------------------------------------------------------------------------------------4) Cons : It cannot send packets to the network or do other active things\n----------------------------------------------------------------------------------------", '2': "NAST\n\n1) Cost : Free \n----------------------------------------------------------------------------------------2) Features : Build LAN hosts list.\nFollow a TCP-DATA stream.\nFind LAN internet gateways.\nDiscover promiscuous nodes.\nReset an established connection.\nfind link type (hub or switch); catch daemon banner of LAN nodes; control arp answers to discover possible arp-spoofings; byte counting with an optional filter; and write reports logging.\n----------------------------------------------------------------------------------------3) Ease of Use :  the tool is quite useful and does a great job of capturing network traffic.\n----------------------------------------------------------------------------------------4) Cons : has not been under development for quite some time.\n----------------------------------------------------------------------------------------", '3': "ZENMAP\n\n1) Cost : Free\n----------------------------------------------------------------------------------------2) Features : Zenmap can be used to read live captures or save captures for later viewing.\nWith Zenmap you can empower the features of Nmap to help you with: network inventory, managing service upgrade schedules, and monitoring host or service uptime.\nHost discovery; port scanning; version detection; OS detection; scriptable interface; web scanning; full IPv6 support; Nping support; fast scanning;\n----------------------------------------------------------------------------------------3) Ease of Use : Available in almost all operating systems\n----------------------------------------------------------------------------------------4) Cons : Sometimes we need to masquerade ourselves before scanning and for that purpose scanning through proxies is done but Zenmap’s proxy support is kind of broken.\n----------------------------------------------------------------------------------------", '4': "ANGRY IP SCANNER\n\n1) Cost : Free\n----------------------------------------------------------------------------------------2) Features : It is Portable (zero installation on certain platforms) and has ping checks.\nIt can resolves hostnames and also determines MAC address.\nIt can determine currently logged-in user.\nScan results can be saved as CSV, TXT, XML, or IP-Port list; and fast, mutli-threaded scanning.\n----------------------------------------------------------------------------------------3) Ease of Use : cross platform scanner that is designed, from the ground up, to be incredibly fast and very simple to use.\n----------------------------------------------------------------------------------------4) Cons : It provides less information and options than Nmap\n----------------------------------------------------------------------------------------"}
        point1 = self.tb1.get("1.0", "end-1c")
        point2 = self.tb2.get("1.0", "end-1c")
        if point1 > '4' or point2 > '4':
             tkMessageBox.showinfo("TOOLS ANALYZER", "Please insert correct tool number")
        self.tb7.insert(0.0, cn[point1])
        self.tb8.insert(0.0, cn[point2])
        self.tb7.configure(state=DISABLED)
        self.tb8.configure(state=DISABLED)
class PageSeven(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
        self.columnconfigure(0, pad=5)
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, pad=5)
        self.columnconfigure(3, pad=5)
        self.columnconfigure(4, pad=5)
        self.rowconfigure(0, pad=15)
        self.rowconfigure(1, pad=15)
        self.rowconfigure(2, pad=15)
        self.rowconfigure(3, pad=15)
        self.rowconfigure(4, pad=15)
        self.rowconfigure(18, pad=15)
        self.rowconfigure(46, pad=15)

        self.lbl1 = Label(self, text="TOP TOOLS:",bg="#a1dbcd")
        self.lbl1.grid(sticky=W, row=2, column=1, pady=1, padx=4)
        self.lbl1.configure(font=("Times New Roman", 14, "bold"))
        self.lblc2 = Label(self, text="1.Multisim",bg="#a1dbcd")
        self.lblc2.grid(sticky=W, row=2, column=2, pady=1, padx=4)
        self.lblc2.configure(font=("Times New Roman", 12))
        self.lblc3 = Label(self, text="2.123D Circuits.io",bg="#a1dbcd")
        self.lblc3.grid(sticky=W, row=2, column=3, pady=1, padx=4)
        self.lblc3.configure(font=("Times New Roman", 12))
        self.lblc4 = Label(self, text="3.Easy EDA",bg="#a1dbcd")
        self.lblc4.grid(sticky=W, row=2, column=4, pady=1, padx=4)
        self.lblc4.configure(font=("Times New Roman", 12))
        self.lblc5 = Label(self, text="4.Altium Circuit Maker",bg="#a1dbcd")
        self.lblc5.grid(sticky=W, row=2, column=5, pady=1, padx=4)
        self.lblc5.configure(font=("Times New Roman", 12))
        self.hbtn = Button(self, text="BACK", command=lambda: controller.show_frame("StartPage"))
        self.hbtn.grid(row=46, column=0, columnspan=2, sticky=W)
        self.obtn = Button(self, text="SUBMIT", command=lambda: self.info())
        self.obtn.grid(row=46, column=2, columnspan=2, sticky=W)
        self.tb7 = Text(self, width=55, height=20, font=("Helvetica", 11), wrap=WORD)
        self.tb7.grid(row=4, column=0, columnspan=2, sticky=W)
        self.tb8 = Text(self, width=55, height=20, font=("Helvetica", 11), wrap=WORD)
        self.tb8.grid(row=4, column=5, columnspan=2, sticky=W)

        self.tb1 = Text(self, width=55, height=5)
        self.tb1.insert(0.0, "insert tool number to compare here")
        # self.tb1.insert(self,'enter tool number',0)
        self.tb1.grid(row=18, column=0, sticky=W)
        self.tb2 = Text(self, width=55, height=5)
        self.tb2.insert(0.0, "insert tool number to compare here")
        self.tb2.insert(0.0, "insert here")
        self.tb2.grid(row=18, column=5, sticky=W)

    def info(self):
        # print(val)
        self.tb7.configure(state=NORMAL)
        self.tb8.configure(state=NORMAL)

        self.tb7.delete(1.0, END)
        self.tb8.delete(1.0, END)
        ec = {'1': "Multisim\n\n1) Cost : Rs .69,800 (professional)\n----------------------------------------------------------------------------------------2) Features : includes options for design validation and gives users flexible layout options even with 4-layer PCBs with up to 1400 pin designs.\n----------------------------------------------------------------------------------------3) Ease of Use : allows users to design their own circuits (circuit capture) and run simulations using a SPICE-based app to test the designs on the fly.\n----------------------------------------------------------------------------------------4) Cons : The package comes in two versions , the free version does not have as many functionalities as the paid one.\n----------------------------------------------------------------------------------------", '2': "123D Circuits.io\n\n1) Cost : Free but for those who prefer to keep their projects to themselves will have to pay a monthly fee ranging from $12 to $25 per-month.\n----------------------------------------------------------------------------------------2) Features : A browser-based software suite that allows users to virtually create their own circuit designs using a simulated Arduino board as well as an accompanying breadboard.\nThere’s also options that allow for integrating LEDs and other electronics into your virtual project and each design can be simulated to see if they function correctly before continuing. \n----------------------------------------------------------------------------------------3) Ease of Use : Good tool for beginners looking to work with the popular dev board\nUsers can program their creations using simple easy to use tutorials from the sites collaborators ,it’s open-source everything there.\n----------------------------------------------------------------------------------------4) Cons : You need to pay a monthly fee to keep your designs private.\n----------------------------------------------------------------------------------------", '3': "EASYEDA\n\n1) Cost : Free\n---------------------------------------------------------------------------------------- 2) Features : EasyEDA is an online-based PCB design tool\nIt allows you to design your schematics and PCB without having to download and install any software on your computer.\nThe software is usually hosted on servers that are directly managed by the EasyEDA Company, so any software updates are done automatically. \n----------------------------------------------------------------------------------------3) Ease of Use : Most of the things, such as libraries, projects, custom-made parts, packages and shared files are accessible via a simple drop down menu at the top left side of the software interface. This makes it easy for you to navigate through the software regardless of whether you are beginner or pro.\n----------------------------------------------------------------------------------------4) Cons : The servers do not allow to cache too many packages\n----------------------------------------------------------------------------------------", '4': "ALTIUM CIRCUIT MAKER\n\n1) Cost : Free\n----------------------------------------------------------------------------------------2) Features : Users are allowed to have 2 private projects, the so-called sandbox mode for practicing.\nBy default, all schematics and PCBs are uploaded to the server and can be viewed by other users.\nUsers are allowed to fork existing projects, or request permission to collaborate in existing projects.\n----------------------------------------------------------------------------------------3) Ease of Use : All documents are under version control by default, allowing users to revert changes made in their projects.\n----------------------------------------------------------------------------------------4) Cons : Users are allowed to own unlimited projects, and there is no hard limit on board complexity.However, Altium warns that users may experience a performance drop for large projects.\n----------------------------------------------------------------------------------------"}
        point1 = self.tb1.get("1.0", "end-1c")
        point2 = self.tb2.get("1.0", "end-1c")
        if point1 > '4' or point2 > '4':
             tkMessageBox.showinfo("TOOLS ANALYZER", "Please insert correct tool number")
        self.tb7.insert(0.0, ec[point1])
        self.tb8.insert(0.0, ec[point2])
        self.tb7.configure(state=DISABLED)
        self.tb8.configure(state=DISABLED)
class PageEight(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
        self.columnconfigure(0, pad=5)
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, pad=5)
        self.columnconfigure(3, pad=5)
        self.columnconfigure(4, pad=5)
        self.rowconfigure(0, pad=15)
        self.rowconfigure(1, pad=15)
        self.rowconfigure(2, pad=15)
        self.rowconfigure(3, pad=15)
        self.rowconfigure(4, pad=15)
        self.rowconfigure(18, pad=15)
        self.rowconfigure(46, pad=15)

        self.lbl1 = Label(self, text="TOP TOOLS:",bg="#a1dbcd")
        self.lbl1.grid(sticky=W, row=2, column=1, pady=1, padx=4)
        self.lbl1.configure(font=("Times New Roman", 14, "bold"))
        self.lblc2 = Label(self, text="1.Code::Blocks",bg="#a1dbcd")
        self.lblc2.grid(sticky=W, row=2, column=2, pady=1, padx=4)
        self.lblc2.configure(font=("Times New Roman", 12))
        self.lblc3 = Label(self, text="2.Dev C++",bg="#a1dbcd")
        self.lblc3.grid(sticky=W, row=2, column=3, pady=1, padx=4)
        self.lblc3.configure(font=("Times New Roman", 12))
        self.lblc4 = Label(self, text="3.CodeLite",bg="#a1dbcd")
        self.lblc4.grid(sticky=W, row=2, column=4, pady=1, padx=4)
        self.lblc4.configure(font=("Times New Roman", 12))
        self.lblc5 = Label(self, text="4.Netbeans",bg="#a1dbcd")
        self.lblc5.grid(sticky=W, row=2, column=5, pady=1, padx=4)
        self.lblc5.configure(font=("Times New Roman", 12))
        self.hbtn = Button(self, text="BACK", command=lambda: controller.show_frame("StartPage"))
        self.hbtn.grid(row=46, column=0, columnspan=2, sticky=W)
        self.obtn = Button(self, text="SUBMIT", command=lambda: self.info())
        self.obtn.grid(row=46, column=2, columnspan=2, sticky=W)
        self.tb7 = Text(self, width=55, height=20, font=("Helvetica", 11), wrap=WORD)
        self.tb7.grid(row=4, column=0, columnspan=2, sticky=W)
        self.tb8 = Text(self, width=55, height=20, font=("Helvetica", 11), wrap=WORD)
        self.tb8.grid(row=4, column=5, columnspan=2, sticky=W)

        self.tb1 = Text(self, width=55, height=5)
        # self.tb1.insert(self,'enter tool number',0)
        self.tb1.grid(row=18, column=0, sticky=W)
        self.tb1.insert(0.0, "insert tool number to compare here")
        self.tb2 = Text(self, width=55, height=5)
        #self.tb2.insert(0.0, "insert here")
        self.tb2.insert(0.0, "insert tool number to compare here")
        self.tb2.grid(row=18, column=5, sticky=W)

    def info(self):
        # print(val)
        self.tb7.configure(state=NORMAL)
        self.tb8.configure(state=NORMAL)

        self.tb7.delete(1.0, END)
        self.tb8.delete(1.0, END)
        c = {'1': "Code::Blocks\n\n1) Cost : Free\n----------------------------------------------------------------------------------------2) Features : Supports Compiling, Debugging, Code Coverage, Profiling, Auto-completion of code.\n----------------------------------------------------------------------------------------3) Ease of Use : Works on Windows, Linux and Mac OS X as well.\nIt is designed to be fully configurable and extensible with its plugins.\n----------------------------------------------------------------------------------------4) Cons : error reporter at compile time is not as good as the other tools.\n----------------------------------------------------------------------------------------", '2': "Dev C++\n\n1) Cost : Free\n----------------------------------------------------------------------------------------2) Features : Code Completion.\nProfiling support.\nSupport GCC-based compilers.\n----------------------------------------------------------------------------------------3) Ease of Use : Customizable syntax highlighting editor.\n----------------------------------------------------------------------------------------4) Cons : the compiler error messages are hard to read\n----------------------------------------------------------------------------------------", '3': "CODELITE\n\n1) Cost : Free\n----------------------------------------------------------------------------------------2) Features : Supports next generation debugger.\nIt also has its own RAD tool for building Widgets-based applications.\nSupports Static code analysis, refactoring, class browser and profiling\n----------------------------------------------------------------------------------------3) Ease of Use : It has amazingly fast and powerful code completion tool based on their in-house parser.\n----------------------------------------------------------------------------------------4) Cons :  it doesnt offer anything unique that's not available in these other IDEs.\n----------------------------------------------------------------------------------------", '4': "NETBEANS\n\n1) Cost : Free\n----------------------------------------------------------------------------------------2) Features : Supports multiplatform.\ncode completion is fast and supports refactoring for C/C++.\nThis IDE is well integrated with the multi-session gdb debugger.\nIt comes with automatic indentation, semantic highlighting, and formatting\n----------------------------------------------------------------------------------------3) Ease of Use : You can use development tools on remote hosts to create, execute, and even debug projects from your client system in a simple manner\n----------------------------------------------------------------------------------------4) Cons : Takes up more memory than lighter IDEs\n----------------------------------------------------------------------------------------"}
        point1 = self.tb1.get("1.0", "end-1c")
        point2 = self.tb2.get("1.0", "end-1c")
        if point1 > '4' or point2 > '4':
             tkMessageBox.showinfo("TOOLS ANALYZER", "Please insert correct tool number")
        self.tb7.insert(0.0, c[point1])
        self.tb8.insert(0.0, c[point2])
        self.tb7.configure(state=DISABLED)
        self.tb8.configure(state=DISABLED)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()