import tkinter as tk
from tkinter import ttk


class MainWin(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        self.master = master
        self.master.config(bg="#2B2D2F")
        master.title("Dictionary") 
        master.geometry("900x600+800+50")
        self.pack(padx=2, pady=2, expand=True, fill='both')
        self.columnconfigure(0,weight=1)
        self.rowconfigure(2, weight=1)
    
        # TOP FRAME
        frameTop = tk.LabelFrame(self, text="", bg="#2B2D2F", pady=5)
        frameTop.grid(row=0, column=0, columnspan=4, sticky="nsew")
        frameTop.columnconfigure(0, weight=1)
        frameTop.rowconfigure(0, weight=1)

        # Back Button
        btnBack = tk.Button(frameTop, text="\N{LEFTWARDS BLACK ARROW}", height=2, width=4)
        btnBack.grid(row=0, column=0, sticky="nw",padx=3, pady=4)

        # Search Field
        entrySearch = tk.Entry(frameTop, width=35)
        entrySearch.grid(row=0, column=3, sticky="nsew", padx=3, pady=2)
        entrySearch.insert(-1, "Search")

        # MIDDLE FRAME
        frameMid = tk.LabelFrame(self, text="", bg="#2B2D2F", padx=5, pady=5)
        frameMid.grid(row=1, column=0, columnspan=2, rowspan=1, sticky="nsew")
        frameMid.columnconfigure(3, weight=1) 
        frameMid.rowconfigure(0, weight=1)

        # All Button
        btnAll = tk.Button(frameMid, text="All")
        btnAll.grid(row=1, column=0)

        #Dictionary Button
        btnDict = tk.Button(frameMid, text="Dictionary")
        btnDict.grid(row=1, column=1, padx=10)

        # Wikipedia Button
        btnWiki = tk.Button(frameMid, text="Wikipedia")
        btnWiki.grid(row=1, column=2, sticky="nw")
    
        # BOTTOM FRAME
        frameBtm = tk.LabelFrame(self, text="", padx=5, pady=5, bg="#2B2D2F")
        frameBtm.grid(row=2, column=0, columnspan=4, sticky="nsew")
        frameBtm.columnconfigure(0, weight=1)   # Expand frame with resize
        frameBtm.rowconfigure(0, weight=1)
        # Info Text Field
        labelInfo = tk.Label(
            frameBtm,
            text="\n\nType a word in to the search box above",
            anchor="n",
            justify="left",
            font=("bold", 19),
            height=25, 
            bg="#2B2D2F", 
            fg="#AEAEAE"
        )
        labelInfo.grid(row=2, column=0, sticky="nsew", padx=1, pady=1, columnspan=4)

if __name__ == '__main__':
    window = tk.Tk()
    app = MainWin(window)
    window.mainloop()
