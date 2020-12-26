import tkinter

main_window = tkinter.Tk()

tombol1 = tkinter.Button(main_window, text = "klik 1")
tombol2 = tkinter.Button(main_window, text = "klik 2")

#method positioning
tombol2.pack()
tombol1.pack()

#method menampilkan GUI
main_window.mainloop()


