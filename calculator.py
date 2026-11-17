#tahap 1
#=======================================================================
#INSTALSI & KONFIGURASI JENDELA UTAMA(GUI)
#========1. memanggil pustaka tkinter
import tkinter as tk

#========2. membuat custom variable jendela utama aplikasi
layar_utama = tk.Tk()

#========3. mengatur atribut jendela utama aplikasi(judul,ukuran,dan warna backruond)
layar_utama.title("kalkulator")
layar_utama.geometry("350x500")
layar_utama.configure(bg="#000000")
#=========================================================================

#tahap 2
#=========================================================================
#deklaeasi variable pemproses data
#membuat varible papan hitung sebagai memori penyimpan input string angka/operator
papan_hitung = ""
#=========================================================================

#tahap 3
#=========================================================================
#PEMBUATAN FUNGSI LOGIKA (DUMMY/SEMENTARA)
#fungsi dikosongkan dengan pass agar tombol yang dibuat bisa merujuk ke fungsi ini
#========1. fungsi dummy untuk tombol angka&operator
def tekan_tombol(num):
    global papan_hitung
    papan_hitung = papan_hitung + str(num)
    string_tampilan.set(papan_hitung)

#========2. fungsi dummy untuk global sama dengan (=)
def hitung():
    global papan_hitung
    try:
        #mengganti karakter visual menjadi operator python sebelum dihitung
        total = str(eval(papan_hitung.replace('x', '*').replace('+', '/').replace(',', '.')))
        string_tampilan.set(total)
        papan_hitung = total
    except:
        string_tampilan.set("error")
        papan_hitung = ""

#========3. fungsi dummy untuk  tombol reset (c)
def hapus_semua():
    global papan_hitung
    papan_hitung = ""
    string_tampilan.set("")
#===========================================================================

#tahap4
#===========================================================================
#PEMBUATAN LAYAR TAMPILAN PAPAN ANGKAB DAN OPERATOR
# #=======1. membuat variable tkinter untuk sinkronisasi teks pada komponen entry
string_tampilan =  tk.StringVar()

#=========2. membuat bkomponen widget entry untuk layar kalkulator
layar = tk.Entry(
    layar_utama,
    textvariable=string_tampilan,
    font=("helvetica", 36),
    bd=0,
    bg="#EBE3E3",
    fg="black",
    justify="right"
)
layar.pack(fill="both", ipadx=10, ipady=30, padx=10, pady=10)
#============================================================================

#tahap 5
#============================================================================
#PEMBUATAN DAN KONFIGURASI WIDGET FRAME TOMBOL
#=======1. membuat frame khusus sebagai tempat meletakan susunan tombol 
frame_tombol = tk.Frame(layar_utama, bg="#000000")
frame_tombol.pack(fill="both", expand="true", padx=10, pady=10)

#=======2. konfigurasi grid layout agar ukuran tombol bisa membesar/mengecil secara proporsional
for i in range(5):
    frame_tombol.rowconfigure(i, weight=1)
for i in range(4):
    frame_tombol.columnconfigure(i, weight=1)
#=============================================================================

#tahap 6
#=============================================================================
#DESAIN DATA & RENDERING TOMBOL (GRID SYSTEM)
#=======1. pemetaan data konfigurasi tombol 
#susunanm data (teks, basis, (row), kolom (colum), warna Bg, warna Fg, fungsi/aksi)
tombol_config = [
    ('c', 0, 0, "#fa0505", 'black', hapus_semua),
    ('+/-', 0, 1, '#a5a5a5', 'black', lambda: tekan_tombol('-')),
    ('%', 0, 2, '#a5a5a5', 'black', lambda: tekan_tombol('/100')),
    ('/', 0, 3, '#a5a5a5', 'black', lambda: tekan_tombol('/')),

    ('1', 1, 0, '#a5a5a5', 'white', lambda: tekan_tombol('1')),
    ('2', 1, 1, '#a5a5a5', 'white', lambda: tekan_tombol('2')),
    ('3', 1, 2, '#a5a5a5', 'white', lambda: tekan_tombol('3')),
    ('x', 1, 3, '#a5a5a5', 'white', lambda: tekan_tombol('x')),

    ('4', 2, 0, '#a5a5a5', 'white', lambda: tekan_tombol('4')),
    ('5', 2, 1, '#a5a5a5', 'white', lambda: tekan_tombol('5')),
    ('6', 2, 2, '#a5a5a5', 'white', lambda: tekan_tombol('6')),
    ('-', 2, 3, '#a5a5a5', 'white', lambda: tekan_tombol('-')),

    ('7', 3, 0, '#a5a5a5', 'white', lambda: tekan_tombol('7')),
    ('8', 3, 1, '#a5a5a5', 'white', lambda: tekan_tombol('8')),
    ('9', 3, 2, '#a5a5a5', 'white', lambda: tekan_tombol('9')),
    ('+', 3, 3, '#a5a5a5', 'white', lambda: tekan_tombol('+')),

    (',', 4, 2, '#a5a5a5', 'white', lambda: tekan_tombol(',')),
    ('=', 4, 3, '#a5a5a5', 'white', hitung)  
]

for teks, r, c, bg_color, fg_color, aksi in tombol_config:
    btn = tk.Button(
        frame_tombol, text=teks, font=("helvetica", 18, "bold"),
        bg=bg_color, fg=fg_color, bd=0, relief="flat", command=aksi
    )
    btn.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

    btn_nol = tk.Button(
        frame_tombol, text="0", font=("helvetica", 18, "bold"),
        bg="#333333", fg="white", bd=0, relief="flat", command=lambda: tekan_tombol('0')
    )
    btn_nol.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
layar_utama.mainloop()