import ttkbootstrap as tb
from ttkbootstrap.constants import *
import requests as req

from K import *


class ButtonGroup(tb.Frame):

    def __init__(self, massa):
        super().__init__(massa)

        self.pack(padx=PM, pady=PM, fill=X)

        self.submit_buttom = tb.Button(self,
                                       text="Submit",
                                       bootstyle=SUCCESS
                                       )

        self.cancel_button = tb.Button(self,
                                       text="Cancel",
                                       bootstyle=(OUTLINE, SECONDARY)
                                       )

        self.submit_buttom.pack(side=RIGHT, padx=(PM, 0))

        self.cancel_button.pack(side=RIGHT)


class SearchBarGroup(tb.Frame):
    def __init__(self, massa):
        super().__init__(massa)
        self.pack(expand=True, fill=BOTH, padx=PM, pady=(0, PM))

        self.label_text = tb.StringVar(value="No Search Results")

        self.search_entry = tb.Entry(self)

        self.submit_button = tb.Button(self,
                                       text="Search",
                                       command=self.search_for_record
                                       )

        self.query_label = tb.Label(self,
                                    textvariable=self.label_text,
                                    font=H6,
                                    justify=CENTER
                                    )

        self.query_label.pack(expand=True, padx=PM, pady=PM, side=BOTTOM)
        self.search_entry.pack(expand=True, fill=X, side=LEFT)
        self.submit_button.pack(side=LEFT, padx=(PXS, 0))

    def search_for_record(self):
        name = self.search_entry.get()
        if len(name) < 1:
            self.label_text.set(value="ERROR\nNo Query Given")
            # self.query_label.configure(text="No Query Given")
        else:
            url_string = f"http://10.6.21.76:8000/academics/{name}"
            res = req.get(url_string).json()
            if "msg" in res:
                self.label_text.set(value=f"{res['msg']}")

            else:
                response_string = f"""
                Name: {res['name']}
                Grade: {res['grade']}
                GPA: {res['gpa']}
                """

                self.label_text.set(value=response_string)
            print(f"{res}")
            # self.query_label.configure(text=f"{res}")
        self.query_label.pack(expand=True, anchor=N)


class AcademicSearchWindow(tb.Frame):

    def __init__(self, massa):
        super().__init__(massa)

        self.pack(expand=True, fill=BOTH)

        subtitle = "i think it should give you academic things like gpa"

        self.title_label = tb.Label(text="SMIC RECORDS",
                                    font=DISPLAY4,
                                    bootstyle=PRIMARY
                                    )

        self.subtitle_label = tb.Label(text=subtitle,
                                       font=LEAD
                                       )

        # self.entry = tb.Entry()

        self.title_label.pack(padx=PM,
                              pady=(PM, PS),
                              anchor=W
                              )

        self.subtitle_label.pack(padx=PM,
                                 pady=(0, PM),
                                 anchor=W
                                 )

        self.search = SearchBarGroup(self)


class App(tb.Window):

    def __init__(self, theme):
        super().__init__(themename=theme)
        self.title("Frames")
        self.geometry("1280x720")

        self.academic_window = AcademicSearchWindow(self)

        # self.entry.pack(expand=True,
        #                 padx=20,
        #                 pady=20,
        #                 fill=X,
        #                 anchor=N
        #                 )

        # self.button_group = ButtonGroup(self)


if __name__ == "__main__":
    app = App(theme="minty")
    app.place_window_center()
    app.mainloop()
    