import tkinter as tk
from tkinter import ttk, messagebox

def popup_sukses(nama, ttgl, email, gender, jurusan):
    #buat jendela pop up custom
    pop = tk.Toplevel(jendela)
    pop.title("Konfirmasi Pendaftaran")
    pop.geometry('400x320')
    pop.resizable(False,False)
    pop.configure(bg='#ffffff')

    #membuat pop up teteap berada paling depan
    pop.transient(jendela)
    pop.grab_set()

    #header judul
    lbl_header = tk.Label(
        pop,
        text='Pendaftaran Berhasil',
        font=('Helvetica', 14, 'bold'),
        fg='#2e7d32',
        bg='#e8f5e9',
        pady=12
    )
    lbl_header.pack(fill='x')

    #Frame konten data
    Frame_data = tk.Frame(pop, bg='#ffffff', padx=25, pady=20)
    Frame_data.pack(fill='both', expand=True)

    list_data = [
        ('Nama', nama),
        ('TTL', ttgl),
        ('Email', email),
        ('Jenis Kelamin', gender),
        ('Jurusan',jurusan)
    ]

    #Menampilkan data secara sejajar dengan grid
    for i, (label, val) in enumerate(list_data):
        tk.Label(
            Frame_data, text=label, font=('Helvetica', 10, 'bold'),
            bg='#ffffff', fg='#333333', anchor='w'
        ).grid(row=i, column=0, padx='w', pady=4)

        tk.Label(
            Frame_data, text=':', font=('Helvetica', 10, 'bold'),
            bg="#ffffff", fg="#333333"
        ).grid(row=i, column=1, padx=8, pady=4)

        tk.Label(
            Frame_data, text=val, font=('Helvetica', 10),
            bg='#ffffff', fg='#555555', anchor='w'   
        ).grid(row=i, column=2, sticky='w', pady=4)

    #tombol tutup/ok
    btn_ok = tk.Button(
        pop,
        text='OK',
        font=('Helvetica', 10, 'bold'),
        bg='#2e7d32',
        fg='white',
        width=12,
        bd=0,
        cursor='hand2',
        command=pop.destroy
    )
    btn_ok.pack(pady=(0, 20))


def simpan_data():
    nama = entry_nama.get()
    ttgl = entry_ttgl.get()
    email = entry_email.get()
    gender = var_gender.get()
    jurusan = combo_jurusan.get()

    #validasi sederhana
    if not nama or not email or jurusan == '-- Pilih Jurusan --':
        messagebox.showwarning('Peringatan', 'Mohon isi semua data yang diperlukan')
        return
    
    #tampilkan pop up sukses kustom 
    popup_sukses(nama, ttgl, email, gender, jurusan)

    #reset form
    reset_form()

def reset_form():
    entry_nama.delete(0, tk.END)
    entry_ttgl.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    var_gender.set('Laki-Laki')
    combo_jurusan.current(0)

#1. inisialisasi window utama 
jendela = tk.Tk()
jendela.title("Formulir pendaftaran TMI")
jendela.geometry("800x650")
jendela.configure(bg="#131212")
jendela.resizable(True,True)

# pembuatan judul jendela
label_judul = tk.Label(jendela, text="Formulir pendaftaran TMI", bg="#131313", fg="#ffffff", font=("Helvetica", 14, "bold"))
label_judul.pack(fill="x", pady=15)

#pembuatan frame berisi form
frame_form = tk.Frame(jendela, bg="#ffffff", padx=20, pady=10)
frame_form.pack(fill="both", expand=True)

#labelm nama
lbl_nama = tk.Label(frame_form, bg="#ffffff", text="Nama Lengkap:", font="bold", anchor="w")
lbl_nama.pack(fill="x", pady=(15, 0))

#entry nama
entry_nama = tk.Entry(frame_form, font=("Helvetica", 20))
entry_nama.pack(fill="x", pady=(0, 10))

#label ttgl
lbl_ttgl = tk.Label(frame_form, bg="#ffffff", text="Tempat/Tanggal Lahir:", font="bold", anchor="w")
lbl_ttgl.pack(fill="x", pady=(15, 0))

#entry ttgl
entry_ttgl = tk.Entry(frame_form, font=("Helvetica", 20))
entry_ttgl.pack(fill="x", pady=(5, 0))

#label Email
lbl_email = tk.Label(frame_form, bg="#ffffff", text="Email:", font="bold", anchor="w")
lbl_email.pack(fill="x", pady=(10, 0))

#entry email
entry_email = tk.Entry(frame_form, font=("Helvetica", 20))
entry_email.pack(fill="x", pady=(0, 5))

#label jenis kelamin
lbl_gender = tk.Label(frame_form, bg="#0914df", text="jenis kelamin:", font="bold", anchor="w")
lbl_gender.pack(fill="x", pady=(5, 0))

var_gender = tk.StringVar(value="laki-laki")
frame_gender = tk.Frame(frame_form, bg="#f8f2f9", highlightbackground="#cccccc", padx=20, pady=10)
frame_gender.pack(fill="x", padx=(0, 10))

rb_pria = tk.Radiobutton(frame_gender, text="laki-laki", font="bold", variable=var_gender, value="laki-laki")
rb_pria.pack(side="left", padx=(0, 20))

rb_wanita = tk.Radiobutton(frame_gender, text="perempuan", font="bold", variable=var_gender, value="perempuan")
rb_wanita.pack(side="left")

# combobox jurusan 
lbl_jurusan = tk.Label(frame_form, text="jurusan / pilihan:", font="bold", anchor="w")
lbl_jurusan.pack(fill="x", pady=(5, 0))

jendela.option_add("*TCombobox*Listbox.font", ("Helvetica", 15))

daftar_jurusan = ["-- Pilih Jurusan --", "Teknik Informatika", "Sistem Informasi", "Desain Grafis", "manajemen", ]
combo_jurusan = ttk.Combobox(frame_form, values=daftar_jurusan, state="readonly", font=("Helvetica", 15))
combo_jurusan.current(0)
combo_jurusan.pack(fill="x", pady=(0, 20))

#tombol submit
frame_tombol = tk.Frame(frame_form, bg="#ffffff")
frame_tombol.pack(fill="x")

btn_simpan = tk.Button(frame_tombol, text="submit", bg="#08f910", fg="white", font=("helvetica", 15, "bold"), command=simpan_data)
btn_simpan.pack(side="left", fill="x", expand=True, padx=(0, 40))

#tombol reset
btn_reset = tk.Button(frame_tombol, text="reset", bg="#f44336", fg="white", font=("helvetica", 15, "bold"), command=reset_form)
btn_reset.pack(side="right", fill="x", expand=True, padx=(40, 0))
 

jendela.mainloop()