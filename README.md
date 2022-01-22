# Tugas Besar IF1210 Dasar Pemrograman
> _Program Ini Dibuat Untuk Memenuhi Tugas Perkuliahan Mata Kuliah Dasar Pemrograman (IF1210)_ <br/>
>
> Sekolah Teknik Elektro dan Informatika <br/>
> Institut Teknologi Bandung <br/>
> Semester II Tahun 2020/2021 <br/>

## Table of Contents
* [Penggunaan Program](#penggunaan-program)
* [Spesifikasi Program](#spesifikasi-program)
* [Struktur Data File Eksternal](#struktur-data-file-eksternal)
* [Kantong Ajaib Doremonangis](#kantong-ajaib-doremonangis)

## Penggunaan Program
**Clone repository ini menggunakan command berikut (git bash)**
```
$ git clone https://github.com/sivaren/TBIF1210-01-03.git
```

**Windows (open `cmd` on this folder)**
```
cd src
python all_in_one.py file_csv
```

## Spesifikasi Program
<table>
    <tr>
      <td><b>Fungsi</b></td>
      <td><b>Keterangan</b></td>
    </tr>
    <tr>
      <td>F01</td>
      <td>Register</td>
    </tr>
    <tr>
      <td>F02</td>
      <td>Login</td>
    </tr>
    <tr>
      <td>F03</td>
      <td>Pencarian gadget berdasarkan rarity</td>
    </tr>
    <tr>
      <td>F04</td>
      <td>Pencarian gadget berdasarkan tahun ditemukan</td>
    </tr>
    <tr>
      <td>F05</td>
      <td>Menambah item</td>
    </tr>
    <tr>
      <td>F06</td>
      <td>Menghapus Gadget atau Consumable</td>
    </tr>
    <tr>
      <td>F07</td>
      <td>Mengubah Jumlah Gadget atau Consumable pada Inventory</td>
    </tr>
    <tr>
      <td>F08</td>
      <td>Meminjam Gadget</td>
    </tr>
    <tr>
      <td>F09</td>
      <td>Mengembalikan Gadget</td>
    </tr>
    <tr>
      <td>F10</td>
      <td>Meminta Consumable</td>
    </tr>
    <tr>
      <td>F11</td>
      <td>Melihat Riwayat Peminjaman Gadget</td>
    </tr>
    <tr>
      <td>F12</td>
      <td>Melihat Riwayat Pengembalian Gadget</td>
    </tr>
    <tr>
      <td>F13</td>
      <td>Melihat Riwayat Pengambilan Consumable</td>
    </tr>
    <tr>
      <td>F14</td>
      <td>Load Data</td>
    </tr>
    <tr>
      <td>F15</td>
      <td>Save Data</td>
    </tr>
    <tr>
      <td>F16</td>
      <td>Help</td>
    </tr>
    <tr>
      <td>F17</td>
      <td>Exit</td>
    </tr>
</table>

## Struktur Data File Eksternal
<table>
    <tr>
      <td><b>File</b></td>
      <td><b>Keterangan</b></td>
    </tr>
    <tr>
      <td>user.csv</td>
      <td>File User</td>
    </tr>
    <tr>
      <td>gadget.csv</td>
      <td>File Gadget</td>
    </tr>
    <tr>
      <td>consumable.csv</td>
      <td>File Consumable</td>
    </tr>
    <tr>
      <td>consumable_history.csv</td>
      <td>File Pengambilan Consumable</td>
    </tr>
    <tr>
      <td>gadget_borrow_history.csv</td>
      <td>File Riwayat Peminjaman Gadget</td>
    </tr>
    <tr>
      <td>gadget_return_history.csv</td>
      <td>File Riwayat Pengembalian Gadget</td>
    </tr>
</table>

## Kantong Ajaib Doremonangis
<table>
    <tr>
      <td><b>Bagian</b></td>
      <td><b>Keterangan</b></td>
    </tr>
    <tr>
      <td>folder file_csv</td>
      <td>berisi file-file eksternal yang dibutuhkan dalam bentuk xxx.csv</td>
    </tr>
    <tr>
      <td>primitif.py</td>
      <td>berisi beberapa fungsi primitif/antara yang dipakai untuk F01-F17</td>
    </tr>
    <tr>
      <td>F01-F17.py</td>
      <td>hanya untuk maintenance (tidak dipergunakan untuk di-run)</td>
    </tr>
    <tr>
      <td>main_program.py</td>
      <td>berisi pembentukan alur program, termasuk opsi-opsi dari menu program</td>
    </tr>
    <tr>
      <td>all_in_one.py</td>
      <td>berisi keseluruhan final code dan dipergunakan untuk di-run</td>
    </tr>
</table>
