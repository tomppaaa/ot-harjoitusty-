from tkinter import Tk, ttk, constants

class UI:
    def __init__(self, root):
        self._root = root
        self._currentView=None

    def start(self):
        self.show_mainView()

    def hide_view(self):
        if self._currentView:
            self._currentView.clearView()
        self._currentView = None

    def show_mainView(self):
        self._currentView = mainView(self._root)
        self._currentView.pack()

    def show_registerView(self):
        self._currentView = registerView(self._root)

    def click_login_register(self,page):
        if page == 1:
            self.hide_view()
            self.show_mainView()
            self._currentView.pack()
        if page == 2:
            self.hide_view()
            self._currentView = registerView(self._root)
            self._currentView.pack()


class mainView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self.loadView()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def clearView(self):
        self._frame.destroy()

    def loadView(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Hello!")

        heading_label = ttk.Label(master=self._frame, text="Login or register a new username")
        username_label = ttk.Label(master=self._frame, text="Username")
        username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        password_entry = ttk.Entry(master=self._frame)

        button = ttk.Button(
            master=self._frame, 
            text="Login",
            command=lambda: ui.click_login_register(1)            
        )

        button1 = ttk.Button(
            master=self._frame, 
            text="Register username",
            command=lambda: ui.click_login_register(2)
            )

        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)


        username_label.grid(padx=5, pady=5)
    
        username_entry.grid(row=1, column=1, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        password_label.grid(padx=5, pady=5)
        password_entry.grid(row=2, column=1, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        button.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        button1.grid(row=3, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1)
        self._root.grid_columnconfigure(1, weight=1, minsize=300)


class registerView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._user = None

        self.loadView()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def clearView(self):
        self._frame.destroy()
    
    def loadView(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Choose your username and password to complete the registration.")

        heading_label = ttk.Label(master=self._frame, text="Choose your username and password to complete the registration.")

        username_label = ttk.Label(master=self._frame, text="Username")
        username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        password_entry = ttk.Entry(master=self._frame)

        button = ttk.Button(
            master=self._frame, 
            text="Create username",
            command=lambda: (ui.click_login_register(1))            
        )

        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

        username_label.grid(padx=5, pady=5)
        username_entry.grid(row=1, column=1, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        password_label.grid(padx=5, pady=5)
        password_entry.grid(row=2, column=1, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        button.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1)
        self._root.grid_columnconfigure(1, weight=1, minsize=300)



window = Tk()
window.title("Macro app")

ui = UI(window)
ui.start()

window.mainloop()