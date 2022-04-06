import tkinter as tk

# 基本設定
WINDOW_SIZE = "600x480"
FONT = "Meiryo"
FONT_SIZE = 20

BUTTON_WIDTH = 12
BUTTON_PDAX = 10
BUTTON_PADY = 10

# 画面ウィジェットの作成
def create_widgets(win):
    win.geometry(WINDOW_SIZE)
    win.title("AudioAnalysis")

    win.recortBtn = tk.Button(win, 
    text="録音" ,
    font=(FONT,FONT_SIZE) ,
    width=BUTTON_WIDTH ,
    command=Create_Record_Dialog
    ).grid(
        row=0, 
        column=0,
        padx=BUTTON_PDAX ,
        pady=BUTTON_PADY)

    win.lordBtn = tk.Button(win, 
    text="読込" ,
    font=(FONT,FONT_SIZE) ,
    width=BUTTON_WIDTH ,
    command=Create_Lord_Dialog
    ).grid(
        row=1, 
        column=0,
        padx=BUTTON_PDAX ,
        pady=BUTTON_PADY)

    win.closeBtn = tk.Button(win, 
    text="閉じる" ,
    font=(FONT,10) ,
    width=BUTTON_WIDTH ,
    command=CloseBtn_Click
    ).grid(
        row=2, 
        column=1,
        padx=BUTTON_PDAX ,
        pady=BUTTON_PADY)

def Create_Record_Dialog():
    # 録音画面を作成して、RecordWindowにわたす
    print("録音画面を開く")

def Create_Lord_Dialog():
    # ファイル選択のエクスプローラーを開く
    print("ファイル選択画面を開く")


def CloseBtn_Click():
    win.destroy()


win = tk.Tk()
create_widgets(win)
win.mainloop()