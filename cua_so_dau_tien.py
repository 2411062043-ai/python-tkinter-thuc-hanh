
import tkinter as tk

# Tao cua so chinh
cua_so = tk.Tk()
cua_so.title("Ung dung demo")
cua_so.geometry("400x300")

# Khong cho thay doi kich thuoc cua so
cua_so.resizable(False, False)

# Tao khung tren
khung_tren = tk.Frame(cua_so, bg="lightblue", height=100)
khung_tren.pack(fill="x")
khung_tren.pack_propagate(False)

# Tao khung duoi
khung_duoi = tk.Frame(cua_so, bg="lightyellow")
khung_duoi.pack(fill="both", expand=True)

# Them noi dung vao khung tren
nhan_tren = tk.Label(
    khung_tren,
    text="Khu vuc tieu de",
    bg="lightblue",
    font=("Arial", 14)
)
nhan_tren.pack(pady=10)

# Them noi dung vao khung duoi
nhan_duoi = tk.Label(
    khung_duoi,
    text="Khu vuc noi dung",
    bg="lightyellow",
    font=("Arial", 14)
)
nhan_duoi.pack(pady=10)

# Hien thi cua so
cua_so.mainloop()
