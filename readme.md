Tucil 2 Strategi Algoritma: Topologi Sort dengan Decrease and Conquer

Topologi sort merupakan cara / algoritma untuk mengurutkan Directed Acyclic Graph. Dalam topologi sort ini merupakan pengurutan yang hasilnya tidak unik. Dalam algoritma ini graf diurutkan dengan cara memilih semua node yang tidak memiliki panah yang mengarah ke node tersebut, kemudian node tersebut ditampilkan dan node tersebut dihapus beserta dengan panah yang berasal dari node tersebut, kemudian proses ini dilakukan terus menerus sampai semua node ditampilkan atau tidak tersisa node lagi.

Decrease and conquer merupakan  algoritma yang mereduksi persoalan menjadi 2 sub masalah yang lebih kecil namun selanjutnya yang di proses hanya satu perosialan saja. Dalam varian decrease and conquer ada tiga tipe yaitu, decrease by constant, decrease by constant factor, dan decrease by variable size.

Pada persoalan ini lebih menggunakan decrease by variable size, karena pada pola ini setiap rekursif ukuran variable berkurang. Pada penerapan program ini pada setiap rekursi melakukan penghapusan node-node atau mata kuliah yang sudah tidak memiliki prequiset sampai ketemu basis dari prosedur topological sort. Basis pada persoalan ini adalah ketika sudah tidak ada upagraf lagi atau graf berbentuk sirkular dan tidak ada node yang bisa dihapus (untuk kasus ini akan menghasilkan error).


0. requirements
    - python 3.x

1. cara menjalankan program
    - masukkan test case anda ke folder src dalam format txt
    - jalankan program 13519028.py di folder src dengan cara membuka cmd lalu ketikkan python 13519028.py atau 13519028.py
    - kemudian ketikkan nama file yang telah diinput di folder test tadi (txt bisa diincludekan atau tidak)
    - hasil dari topologi sort akan segera keluar

2. format penulisan file txt
    format yang diterima dalam txt adalah sbg berikut
        nama-kelas1, prequiset-1, prequiset-2, .... , prequiset-n.
        nama-kelas2, prequiset-1, prequiset-2, .... , prequiset-n.
        nama-kelas3, prequiset-1, prequiset-2, .... , prequiset-n.
        ..
        nama-kelasn, prequiset-1, prequiset-2, .... , prequiset-n.

        pastikan graf tidak mengandung sirkular, apabila ada maka bisa error

Hafid Abi Daniswara
13519028