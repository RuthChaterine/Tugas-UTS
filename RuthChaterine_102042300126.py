print("""
==== Swalayan ====
1. Bahan Makanan
2. Daging Segar
3. Buah Segar
4. Sayur Fresh
5. Exit
""")
pilih = int(input("Silahkan Pilih : "))
potonganBNI = 10000
potonganBCA = 12000

match pilih:
    case 1:
        print("""
        === Bahan Makanan ===
        1. Minyak Goreng
        2. Bumbu Dapur
        3. Beras
        4. Telur
        
        """)
        bahanMakanan = int(input("Pilih Bahan Makanan Yang Kamu Inginkan : "))
        
        match bahanMakanan:
            case 1: #Minyak Goreng
                print("""
                1. Bimoli
                2. Barco
                3. Tropical
                4. Fortune
                """)
                minyakGoreng = int(input("Pilih Merk Yang Ingin Kamu Beli : "))

                match minyakGoreng:
                    case 1: #Bimoli
                        print("=== Ukuran ===")
                        minyakBimoli = ""
                        hargaMinyakBimoli = 0

                        print("""
                        1. Ukuran 1L Rp. 19.000
                        2. Ukuran 2L Rp. 35.000
                        3. Ukuran 5L Rp. 95.000
                        """)
                        ukuranMinyakBimoli = int(input("Pilih Ukuran Yang Kamu Inginkan : "))
                        if ukuranMinyakBimoli == 1:
                            minyakBimoli += "Bimoli 1L"
                            hargaMinyakBimoli += 19000
                        elif ukuranMinyakBimoli == 2:
                            minyakBimoli += "Bimoli 2L"
                            hargaMinyakBimoli += 35000
                        elif ukuranMinyakBimoli == 3:
                            minyakBimoli += "Bimoli 5L"
                            hargaMinyakBimoli += 95000
                        else:
                            print("Pilihan Tidak Tersedia")

                        banyakMinyakBimoli = int(input("Banyak Minyak Yang Ingin Dibeli : "))
                        totalHargaMinyakBimoli = hargaMinyakBimoli*banyakMinyakBimoli
                        print("Harga Yang Dibayarkan Adalah : ", totalHargaMinyakBimoli)
                        dealMinyakBimoli = input("Apakah Anda Ingin Melanjutkan Transaksi? ")
                        if dealMinyakBimoli == "Ya" or dealMinyakBimoli == "ya" or dealMinyakBimoli == "y":
                            print("""
                            1. Cash
                            2. Debit BNI (Potongan 5%)
                            3. Debit BCA (Potongan 2%)
                            4. Debit BRI (Free Pulsa 5rb)
                            """)
                            diskonBimoliBNI = totalHargaMinyakBimoli - potonganBNI
                            diskonBimoliBCA = totalHargaMinyakBimoli - potonganBCA
                            metodePembayaranBimoli = int(input("Silahkan Pilih Metode Pembayaran Anda : "))

                            if metodePembayaranBimoli == 1:
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", totalHargaMinyakBimoli)
                                konfirmasiPembayaranBNIbimoli = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBNIbimoli == "Y" or konfirmasiPembayaranBNIbimoli == "y":
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan : {minyakBimoli}
                                    Harga   : {totalHargaMinyakBimoli}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            elif metodePembayaranBimoli == 2:
                                print("=== Data Pembayaran ===")
                                nomorKartu = input("Nomor Kartu : ")
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonBimoliBNI)
                                konfirmasiPembayaranBNIbimoli = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBNIbimoli == "Y" or konfirmasiPembayaranBNIbimoli == "y":
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan : {minyakBimoli}
                                    Harga   : {diskonBimoliBNI}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            elif metodePembayaranBimoli == 3:
                                print("=== Data Pembayaran ===")
                                nomorKartu = input("Nomor Kartu : ")
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonBimoliBCA)
                                konfirmasiPembayaranBCAbimoli = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBCAbimoli == "Y" or konfirmasiPembayaranBCAbimoli == "y":
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan : {minyakBimoli}
                                    Harga   : {diskonBimoliBCA}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            elif metodePembayaranBimoli == 4:
                                print("=== Data Pembayaran ===")
                                nomorKartu = input("Nomor Kartu : ")
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonBimoliBCA)
                                konfirmasiPembayaranBCAbimoli = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBCAbimoli == "Y" or konfirmasiPembayaranBCAbimoli == "y":
                                    print("Anda Mendapatkan Free Pulsa Senilai Rp. 5.000")
                                    freePulsaBimoliBRI = input("Nomor HP : ")
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan    : {minyakBimoli}
                                    Free       : Pulsa Rp. 5.000
                                    No. Tujuan : {freePulsaBimoliBRI}
                                    Harga      : {diskonBimoliBCA}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            else:
                                print("Pilihan Tidak Tersedia")

                        else:
                            print("Transaksi Gagal!")



                    case 2: #Barco
                        print("=== Ukuran ===")
                        minyakBarco = ""
                        hargaMinyakBarco = 0

                        print("""
                        1. Ukuran 1L Rp. 30.000
                        2. Ukuran 2L Rp. 60.000
                        """)
                        ukuranMinyakBarco = int(input("Pilih Ukuran Yang Kamu Inginkan : "))
                        if ukuranMinyakBarco == 1:
                            minyakBarco += "Barco 1L"
                            hargaMinyakBarco += 30000
                        elif ukuranMinyakBarco == 2:
                            minyakBarco += "Baarc0 2L"
                            hargaMinyakBarco += 60000
                        else:
                            print("Pilihan Tidak Tersedia")

                        banyakMinyakBarco = int(input("Banyak Minyak Yang Ingin Dibeli : "))
                        totalHargaMinyakBarco = hargaMinyakBarco*banyakMinyakBarco
                        print("Harga Yang Dibayarkan Adalah : ", totalHargaMinyakBarco)
                        dealMinyakBarco = input("Apakah Anda Ingin Melanjutkan Transaksi? ")
                        if dealMinyakBarco == "Ya" or dealMinyakBarco == "ya" or dealMinyakBarco == "y":
                            print("""
                            1. Cash
                            2. Debit BNI (Potongan 5%)
                            3. Debit BCA (Potongan 2%)
                            4. Debit BRI (Free Pulsa 5rb)
                            """)
                            diskonBarcoBNI = totalHargaMinyakBarco - potonganBNI
                            diskonBarcoBCA = totalHargaMinyakBarco - potonganBCA
                            metodePembayaranBarco = int(input("Silahkan Pilih Metode Pembayaran Anda : "))

                            if metodePembayaranBarco == 1:
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", totalHargaMinyakBarco)
                                konfirmasiPembayaranBNIBarco = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBNIBarco == "Y" or konfirmasiPembayaranBNIBarco == "y":
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan : {minyakBarco}
                                    Harga   : {totalHargaMinyakBarco}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            elif metodePembayaranBarco == 2:
                                print("=== Data Pembayaran ===")
                                nomorKartu = input("Nomor Kartu : ")
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonBarcoBNI)
                                konfirmasiPembayaranBNIBarco = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBNIBarco == "Y" or konfirmasiPembayaranBNIBarco == "y":
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan : {minyakBarco}
                                    Harga   : {diskonBarcoBNI}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            elif metodePembayaranBarco == 3:
                                print("=== Data Pembayaran ===")
                                nomorKartu = input("Nomor Kartu : ")
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonBarcoBCA)
                                konfirmasiPembayaranBCAbimoli = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBCAbimoli == "Y" or konfirmasiPembayaranBCAbimoli == "y":
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan : {minyakBarco}
                                    Harga   : {diskonBarcoBCA}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            elif metodePembayaranBarco == 4:
                                print("=== Data Pembayaran ===")
                                nomorKartu = input("Nomor Kartu : ")
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonBarcoBCA)
                                konfirmasiPembayaranBCABarco = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBCABarco == "Y" or konfirmasiPembayaranBCABarco == "y":
                                    print("Anda Mendapatkan Free Pulsa Senilai Rp. 5.000")
                                    freePulsaBimoliBRI = input("Nomor HP : ")
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan    : {minyakBarco}
                                    Free       : Pulsa Rp. 5.000
                                    No. Tujuan : {freePulsaBimoliBRI}
                                    Harga      : {diskonBarcoBCA}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            else:
                                print("Pilihan Tidak Tersedia")

                        

                    case 3: #Tropical
                        print("=== Ukuran ===")
                        minyakTropical = ""
                        hargaMinyakTropical = 0

                        print("""
                        1. Ukuran 1L Rp. 20.000
                        2. Ukuran 2L Rp. 35.000
                        """)
                        ukuranMinyakTropical = int(input("Pilih Ukuran Yang Kamu Inginkan : "))
                        if ukuranMinyakTropical == 1:
                            minyakTropical += "Tropical 1L"
                            hargaMinyakTropical += 20000
                        elif ukuranMinyakTropical == 2:
                            minyakTropical += "Tropical 2L"
                            hargaMinyakTropical += 35000
                        else:
                            print("Pilihan Tidak Tersedia")

                        banyakMinyakTropical = int(input("Banyak Minyak Yang Ingin Dibeli : "))
                        totalHargaMinyakTropical = hargaMinyakTropical*banyakMinyakTropical
                        print("Harga Yang Dibayarkan Adalah : ", totalHargaMinyakTropical)
                        dealMinyakTropical = input("Apakah Anda Ingin Melanjutkan Transaksi? ")
                        if dealMinyakTropical == "Ya" or dealMinyakTropical == "ya" or dealMinyakTropical == "y":
                            print("""
                            1. Cash
                            2. Debit BNI (Potongan 5%)
                            3. Debit BCA (Potongan 2%)
                            4. Debit BRI (Free Pulsa 5rb)
                            """)
                            diskonTropicalBNI = totalHargaMinyakTropical - potonganBNI
                            diskonTropicalBCA = totalHargaMinyakTropical - potonganBCA
                            metodePembayaranTropical = int(input("Silahkan Pilih Metode Pembayaran Anda : "))

                            if metodePembayaranTropical == 1:
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", totalHargaMinyakTropical)
                                konfirmasiPembayaranBNITropical = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBNITropical == "Y" or konfirmasiPembayaranBNITropical == "y":
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan : {minyakTropical}
                                    Harga   : {totalHargaMinyakTropical}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            elif metodePembayaranTropical == 2:
                                print("=== Data Pembayaran ===")
                                nomorKartu = input("Nomor Kartu : ")
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonTropicalBNI)
                                konfirmasiPembayaranBNITropical = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBNITropical == "Y" or konfirmasiPembayaranBNITropical == "y":
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan : {minyakTropical}
                                    Harga   : {diskonTropicalBNI}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            elif metodePembayaranTropical == 3:
                                print("=== Data Pembayaran ===")
                                nomorKartu = input("Nomor Kartu : ")
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonTropicalBCA)
                                konfirmasiPembayaranBCATropical = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBCATropical == "Y" or konfirmasiPembayaranBCATropical == "y":
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan : {minyakTropical}
                                    Harga   : {diskonTropicalBCA}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            elif metodePembayaranTropical == 4:
                                print("=== Data Pembayaran ===")
                                nomorKartu = input("Nomor Kartu : ")
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonTropicalBCA)
                                konfirmasiPembayaranBCATropical = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBCATropical == "Y" or konfirmasiPembayaranBCATropical == "y":
                                    print("Anda Mendapatkan Free Pulsa Senilai Rp. 5.000")
                                    freePulsaTropicalBRI = input("Nomor HP : ")
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan    : {minyakTropical}
                                    Free       : Pulsa Rp. 5.000
                                    No. Tujuan : {freePulsaTropicalBRI}
                                    Harga      : {diskonTropicalBCA}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            else:
                                print("Pilihan Tidak Tersedia")

                        else:
                            print("Transaksi Gagal!")

                    case 4: #Fortune
                        print("=== Ukuran ===")
                        minyakFortune = ""
                        hargaMinyakFortune = 0

                        print("""
                        1. Ukuran 1L Rp. 20.000
                        2. Ukuran 2L Rp. 35.000
                        """)
                        ukuranMinyakFortune = int(input("Pilih Ukuran Yang Kamu Inginkan : "))
                        if ukuranMinyakFortune == 1:
                            minyakFortune += "Fortune 1L"
                            hargaMinyakFortune += 20000
                        elif ukuranMinyakFortune == 2:
                            minyakFortune += "Fortune 2L"
                            hargaMinyakFortune += 35000
                        else:
                            print("Pilihan Tidak Tersedia")

                        banyakMinyakFortune = int(input("Banyak Minyak Yang Ingin Dibeli : "))
                        totalHargaMinyakFortune = hargaMinyakFortune*banyakMinyakFortune
                        print("Harga Yang Dibayarkan Adalah : ", totalHargaMinyakFortune)
                        dealMinyakFortune = input("Apakah Anda Ingin Melanjutkan Transaksi? ")
                        if dealMinyakFortune == "Ya" or dealMinyakFortune == "ya" or dealMinyakFortune == "y":
                            print("""
                            1. Cash
                            2. Debit BNI (Potongan 5%)
                            3. Debit BCA (Potongan 2%)
                            4. Debit BRI (Free Pulsa 5rb)
                            """)
                            diskonFortuneBNI = totalHargaMinyakFortune - potonganBNI
                            diskonFortuneBCA = totalHargaMinyakFortune - potonganBCA
                            metodePembayaranFortune = int(input("Silahkan Pilih Metode Pembayaran Anda : "))

                            if metodePembayaranFortune == 1:
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", totalHargaMinyakFortune)
                                konfirmasiPembayaranBNIFortune = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBNIFortune == "Y" or konfirmasiPembayaranBNIFortune == "y":
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan : {minyakFortune}
                                    Harga   : {totalHargaMinyakFortune}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            elif metodePembayaranFortune == 2:
                                print("=== Data Pembayaran ===")
                                nomorKartu = input("Nomor Kartu : ")
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonFortuneBNI)
                                konfirmasiPembayaranBNIFortune = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBNIFortune == "Y" or konfirmasiPembayaranBNIFortune == "y":
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan : {minyakFortune}
                                    Harga   : {diskonFortuneBNI}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            elif metodePembayaranFortune == 3:
                                print("=== Data Pembayaran ===")
                                nomorKartu = input("Nomor Kartu : ")
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonFortuneBCA)
                                konfirmasiPembayaranBCATropical = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBCATropical == "Y" or konfirmasiPembayaranBCATropical == "y":
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan : {minyakFortune}
                                    Harga   : {diskonFortuneBCA}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            elif metodePembayaranFortune == 4:
                                print("=== Data Pembayaran ===")
                                nomorKartu = input("Nomor Kartu : ")
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonFortuneBCA)
                                konfirmasiPembayaranBCAFortune = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBCAFortune == "Y" or konfirmasiPembayaranBCAFortune == "y":
                                    print("Anda Mendapatkan Free Pulsa Senilai Rp. 5.000")
                                    freePulsaFortuneBRI = input("Nomor HP : ")
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan    : {minyakFortune}
                                    Free       : Pulsa Rp. 5.000
                                    No. Tujuan : {freePulsaFortuneBRI}
                                    Harga      : {diskonFortuneBCA}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            else:
                                print("Pilihan Tidak Tersedia")

                    case _:
                        print("Pilihan Tidak Tersedia")


            case 2: #Bumbu Dapur
                print("""
                1. Garam
                2. Gula
                """)
                bumbuDapur = int(input("Pilih Yang Ingin Kamu Beli : "))

                match bumbuDapur:
                    case 1:
                        print("=== Ukuran ===")
                        Garam = ""
                        hargaGaram = 0

                        print("""
                        1. Ukuran 250g Rp. 15.000
                        2. Ukuran 500g Rp. 25.000
                        """)
                        ukuranGaram = int(input("Pilih Ukuran Yang Kamu Inginkan : "))
                        if ukuranGaram == 1:
                            Garam += "Garam 250g"
                            hargaGaram += 19000
                        elif ukuranGaram == 2:
                            Garam += "Garam 500g"
                            hargaGaram += 35000
                        else:
                            print("Pilihan Tidak Tersedia")

                        banyakGaram = int(input("Banyak Barang Yang Ingin Dibeli : "))
                        totalHargaGaram = hargaGaram * banyakGaram
                        print("Harga Yang Dibayarkan Adalah : ", totalHargaGaram)
                        dealGaram = input("Apakah Anda Ingin Melanjutkan Transaksi? ")
                        if dealGaram == "Ya" or dealGaram == "ya" or dealGaram == "y":
                            print("""
                            1. Cash
                            2. Debit BNI (Potongan 5%)
                            3. Debit BCA (Potongan 2%)
                            4. Debit BRI (Free Pulsa 5rb)
                            """)
                            diskonGaramBNI = totalHargaGaram - potonganBNI
                            diskonGaramBCA = totalHargaGaram - potonganBCA
                            metodePembayaranGaram = int(input("Silahkan Pilih Metode Pembayaran Anda : "))

                            if metodePembayaranGaram == 1:
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", totalHargaGaram)
                                konfirmasiPembayaranBNIGaram = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBNIGaram == "Y" or konfirmasiPembayaranBNIGaram == "y":
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan : {Garam}
                                    Harga   : {totalHargaGaram}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            elif metodePembayaranGaram == 2:
                                print("=== Data Pembayaran ===")
                                nomorKartu = input("Nomor Kartu : ")
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonGaramBNI)
                                konfirmasiPembayaranBNIGaram = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBNIGaram == "Y" or konfirmasiPembayaranBNIGaram == "y":
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan : {Garam}
                                    Harga   : {diskonGaramBNI}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            elif metodePembayaranGaram == 3:
                                print("=== Data Pembayaran ===")
                                nomorKartu = input("Nomor Kartu : ")
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonGaramBCA)
                                konfirmasiPembayaranBCAGaram = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBCAGaram == "Y" or konfirmasiPembayaranBCAGaram == "y":
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan : {Garam}
                                    Harga   : {diskonGaramBCA}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            elif metodePembayaranGaram == 4:
                                print("=== Data Pembayaran ===")
                                nomorKartu = input("Nomor Kartu : ")
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonGaramBCA)
                                konfirmasiPembayaranBCAGaram = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBCAGaram == "Y" or konfirmasiPembayaranBCAGaram == "y":
                                    print("Anda Mendapatkan Free Pulsa Senilai Rp. 5.000")
                                    freePulsaGaramBRI = input("Nomor HP : ")
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan    : {Garam}
                                    Free       : Pulsa Rp. 5.000
                                    No. Tujuan : {freePulsaGaramBRI}
                                    Harga      : {diskonGaramBCA}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            else:
                                print("Pilihan Tidak Tersedia")

                        else:
                            print("Transaksi Gagal!")

                    case 2: #Gula
                        print("=== Ukuran ===")
                        Gula = ""
                        hargaGula = 0

                        print("""
                        1. Ukuran 500gr Rp. 8.000
                        2. Ukuran 1kg Rp. 14.500
                        """)
                        ukuranGula = int(input("Pilih Ukuran Yang Kamu Inginkan : "))
                        if ukuranGula == 1:
                            Gula += "Bimoli 1L"
                            hargaGula += 19000
                        elif ukuranGula == 2:
                            Gula += "Bimoli 2L"
                            hargaGula += 35000
                        elif ukuranGula == 3:
                            Gula += "Bimoli 5L"
                            hargaGula += 95000
                        else:
                            print("Pilihan Tidak Tersedia")

                        banyakGula = int(input("Banyak Barang Yang Ingin Dibeli : "))
                        totalHargaGula = hargaGula * banyakGula
                        print("Harga Yang Dibayarkan Adalah : ", totalHargaGula)
                        dealGula = input("Apakah Anda Ingin Melanjutkan Transaksi? ")
                        if dealGula == "Ya" or dealGula == "ya" or dealGula == "y":
                            print("""
                            1. Cash
                            2. Debit BNI (Potongan 5%)
                            3. Debit BCA (Potongan 2%)
                            4. Debit BRI (Free Pulsa 5rb)
                            """)
                            diskonGulaBNI = totalHargaGula - potonganBNI
                            diskonGulaBCA = totalHargaGula - potonganBCA
                            metodePembayaranGula = int(input("Silahkan Pilih Metode Pembayaran Anda : "))

                            if metodePembayaranGula == 1:
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", totalHargaGula)
                                konfirmasiPembayaranBNIGula = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBNIGula == "Y" or konfirmasiPembayaranBNIGula == "y":
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan : {Gula}
                                    Harga   : {totalHargaGula}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            elif metodePembayaranGula == 2:
                                print("=== Data Pembayaran ===")
                                nomorKartu = input("Nomor Kartu : ")
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonGulaBNI)
                                konfirmasiPembayaranBNIGula = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBNIGula == "Y" or konfirmasiPembayaranBNIGula == "y":
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan : {Gula}
                                    Harga   : {diskonGulaBNI}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            elif metodePembayaranGula == 3:
                                print("=== Data Pembayaran ===")
                                nomorKartu = input("Nomor Kartu : ")
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonGulaBCA)
                                konfirmasiPembayaranBCAGula = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBCAGula == "Y" or konfirmasiPembayaranBCAGula == "y":
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan : {Gula}
                                    Harga   : {diskonGulaBCA}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            elif metodePembayaranGula == 4:
                                print("=== Data Pembayaran ===")
                                nomorKartu = input("Nomor Kartu : ")
                                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonGulaBCA)
                                konfirmasiPembayaranBCAGula = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                                if konfirmasiPembayaranBCAGula == "Y" or konfirmasiPembayaranBCAGula == "y":
                                    print("Anda Mendapatkan Free Pulsa Senilai Rp. 5.000")
                                    freePulsaGulaBRI = input("Nomor HP : ")
                                    print("=== Invoice ===")
                                    print(f"""
                                    Pesanan    : {Gula}
                                    Free       : Pulsa Rp. 5.000
                                    No. Tujuan : {freePulsaGulaBRI}
                                    Harga      : {diskonGulaBCA}
                                    Terimakasih Telah Melakukan Transaksi
                                    """)
                                else:
                                    print("Transaksi Gagal!")

                            else:
                                print("Pilihan Tidak Tersedia")

                        else:
                            print("Transaksi Gagal!")

                    case _:
                        print("Pilihan Tidak Tersedia")

    case 2:
        print("""
        === Daging Segar ===
        1. Ikan
        2. Daging
        """)
        dagingSegar = int(input("Pilih Daging Yang Kamu Inginkan : "))
        
        match dagingSegar:
            case 1: #Ikan
                print("""
                1. Tuna 1kg Rp. 120.000
                2. Gurame 1kg Rp. 85.000
                3. Tenggiri 1kg Rp. 140.000
                4. Salmom 1kg Rp. 70.000
                5. Tongkol 1kg Rp. 80.000
                6. Udang 1kg Rp. 130.000
                7. Cumi-Cumi 1kg Rp. 120.000
                """)
                Ikan = int(input("Pilih Merk Yang Ingin Kamu Beli : "))
                namaIkan = ""
                hargaIkan = 0

                if Ikan == 1:
                    namaIkan += "Tuna 1kg"
                    hargaIkan += 120000
                elif Ikan == 2:
                    namaIkan += "Gurame 1kg"
                    hargaIkan += 85000
                elif Ikan == 3:
                    namaIkan += "Tenggiri 1kg"
                    hargaIkan += 140000
                elif Ikan == 4:
                    namaIkan += "Salmon 1kg"
                    hargaIkan += 70000
                elif Ikan == 5:
                    namaIkan += "Tongkol 1kg"
                    hargaIkan += 80000
                elif Ikan == 6:
                    namaIkan += "Udang 1kg"
                    hargaIkan += 130000
                elif Ikan == 7:
                    namaIkan += "Cumi-cumi 1kg"
                    hargaIkan += 140000
                else:
                    print("Pilihan Tidak Ada")

                banyakIkan = int(input("Banyak Barang Yang Ingin Dibeli : "))
                totalHargaIkan = hargaIkan * banyakIkan
                print("Harga Yang Dibayarkan Adalah : ", totalHargaIkan)
                dealIkan = input("Apakah Anda Ingin Melanjutkan Transaksi? ")
                if dealIkan == "Ya" or dealIkan == "ya" or dealIkan == "y":
                    print("""
                    1. Cash
                    2. Debit BNI (Potongan 5%)
                    3. Debit BCA (Potongan 2%)
                    4. Debit BRI (Free Pulsa 5rb)
                    """)
                    diskonIkanBNI = totalHargaIkan - potonganBNI
                    diskonIkanBCA = totalHargaIkan - potonganBCA
                    metodePembayaranIkan = int(input("Silahkan Pilih Metode Pembayaran Anda : "))

                    if metodePembayaranIkan == 1:
                        print("Harga Yang Anda Bayarkan Adalah Rp. ", totalHargaIkan)
                        konfirmasiPembayaranBNIIkan = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                        if konfirmasiPembayaranBNIIkan == "Y" or konfirmasiPembayaranBNIIkan == "y":
                            print("=== Invoice ===")
                            print(f"""
                            Pesanan : {Ikan}
                            Harga   : {totalHargaIkan}
                            Terimakasih Telah Melakukan Transaksi
                            """)
                        else:
                            print("Transaksi Gagal!")

                    elif metodePembayaranIkan == 2:
                        print("=== Data Pembayaran ===")
                        nomorKartu = input("Nomor Kartu : ")
                        print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonIkanBNI)
                        konfirmasiPembayaranBNIIkan = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                        if konfirmasiPembayaranBNIIkan == "Y" or konfirmasiPembayaranBNIIkan == "y":
                            print("=== Invoice ===")
                            print(f"""
                            Pesanan : {Ikan}
                            Harga   : {diskonIkanBNI}
                            Terimakasih Telah Melakukan Transaksi
                            """)
                        else:
                            print("Transaksi Gagal!")

                    elif metodePembayaranIkan == 3:
                        print("=== Data Pembayaran ===")
                        nomorKartu = input("Nomor Kartu : ")
                        print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonIkanBCA)
                        konfirmasiPembayaranBCAIkan = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                        if konfirmasiPembayaranBCAIkan == "Y" or konfirmasiPembayaranBCAIkan == "y":
                            print("=== Invoice ===")
                            print(f"""
                            Pesanan : {Ikan}
                            Harga   : {diskonIkanBCA}
                            Terimakasih Telah Melakukan Transaksi
                            """)
                        else:
                            print("Transaksi Gagal!")

                    elif metodePembayaranIkan == 4:
                        print("=== Data Pembayaran ===")
                        nomorKartu = input("Nomor Kartu : ")
                        print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonIkanBCA)
                        konfirmasiPembayaranBCAIkan = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                        if konfirmasiPembayaranBCAIkan == "Y" or konfirmasiPembayaranBCAIkan == "y":
                            print("Anda Mendapatkan Free Pulsa Senilai Rp. 5.000")
                            freePulsaIkanBRI = input("Nomor HP : ")
                            print("=== Invoice ===")
                            print(f"""
                            Pesanan    : {Ikan}
                            Free       : Pulsa Rp. 5.000
                            No. Tujuan : {freePulsaIkanBRI}
                            Harga      : {diskonIkanBCA}
                            Terimakasih Telah Melakukan Transaksi
                            """)
                        else:
                            print("Transaksi Gagal!")

                    else:
                        print("Pilihan Tidak Tersedia")

                else:
                    print("Pilihan Tidak Tersedia")
            
            case 2: #Daging
                print("""
                1. Ayam 1kg Rp. 40.000
                2. Sapi 1kg Rp. 150.000
                3. Kambing 1kg Rp. 130.000
                4. Domba 1kg Rp. 150.000
                5. Babi 1kg Rp. 100.000 (Non Halal)
                """)
                Daging = int(input("Pilih Merk Yang Ingin Kamu Beli : "))
                jenisDaging = ""
                hargaDaging = 0

                if Daging == 1:
                    jenisDaging += "Ayam 1kg"
                    hargaDaging += 40000
                elif Daging == 2:
                    jenisDaging += "Sapi 1kg"
                    hargaDaging += 150000
                elif Daging == 3:
                    jenisDaging += "Kambing 1kg"
                    hargaDaging += 130000
                elif Daging == 4:
                    jenisDaging += "Domba 1kg"
                    hargaDaging += 150000
                elif Daging == 5:
                    jenisDaging += "Babi 1kg"
                    hargaDaging += 100000
                else:
                    print("Pilihan Tidak Ada")

                banyakDaging = int(input("Banyak Barang Yang Ingin Dibeli : "))
                totalHargaDaging = hargaDaging * banyakDaging
                print("Harga Yang Dibayarkan Adalah : ", totalHargaDaging)
                dealDaging = input("Apakah Anda Ingin Melanjutkan Transaksi? ")
                if dealDaging == "Ya" or dealDaging == "ya" or dealDaging == "y":
                    print("""
                    1. Cash
                    2. Debit BNI (Potongan 5%)
                    3. Debit BCA (Potongan 2%)
                    4. Debit BRI (Free Pulsa 5rb)
                    """)
                    diskonDagingBNI = totalHargaDaging - potonganBNI
                    diskonDagingBCA = totalHargaDaging - potonganBCA
                    metodePembayaranDaging = int(input("Silahkan Pilih Metode Pembayaran Anda : "))

                    if metodePembayaranDaging == 1:
                        print("Harga Yang Anda Bayarkan Adalah Rp. ", totalHargaDaging)
                        konfirmasiPembayaranBNIDaging = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                        if konfirmasiPembayaranBNIDaging == "Y" or konfirmasiPembayaranBNIDaging == "y":
                            print("=== Invoice ===")
                            print(f"""
                            Pesanan : {Daging}
                            Harga   : {totalHargaDaging}
                            Terimakasih Telah Melakukan Transaksi
                            """)
                        else:
                            print("Transaksi Gagal!")

                    elif metodePembayaranDaging == 2:
                        print("=== Data Pembayaran ===")
                        nomorKartu = input("Nomor Kartu : ")
                        print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonDagingBNI)
                        konfirmasiPembayaranBNIDaging = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                        if konfirmasiPembayaranBNIDaging == "Y" or konfirmasiPembayaranBNIDaging == "y":
                            print("=== Invoice ===")
                            print(f"""
                            Pesanan : {Daging}
                            Harga   : {diskonDagingBNI}
                            Terimakasih Telah Melakukan Transaksi
                            """)
                        else:
                            print("Transaksi Gagal!")

                    elif metodePembayaranDaging == 3:
                        print("=== Data Pembayaran ===")
                        nomorKartu = input("Nomor Kartu : ")
                        print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonDagingBCA)
                        konfirmasiPembayaranBCADaging = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                        if konfirmasiPembayaranBCADaging == "Y" or konfirmasiPembayaranBCADaging == "y":
                            print("=== Invoice ===")
                            print(f"""
                            Pesanan : {Daging}
                            Harga   : {diskonDagingBCA}
                            Terimakasih Telah Melakukan Transaksi
                            """)
                        else:
                            print("Transaksi Gagal!")

                    elif metodePembayaranDaging == 4:
                        print("=== Data Pembayaran ===")
                        nomorKartu = input("Nomor Kartu : ")
                        print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonDagingBCA)
                        konfirmasiPembayaranBCADaging = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                        if konfirmasiPembayaranBCADaging == "Y" or konfirmasiPembayaranBCADaging == "y":
                            print("Anda Mendapatkan Free Pulsa Senilai Rp. 5.000")
                            freePulsaDagingBRI = input("Nomor HP : ")
                            print("=== Invoice ===")
                            print(f"""
                            Pesanan    : {Daging}
                            Free       : Pulsa Rp. 5.000
                            No. Tujuan : {freePulsaDagingBRI}
                            Harga      : {diskonDagingBCA}
                            Terimakasih Telah Melakukan Transaksi
                            """)
                        else:
                            print("Transaksi Gagal!")

                    else:
                        print("Pilihan Tidak Tersedia")

                else:
                    print("Pilihan Tidak Tersedia")

            case _:
                print("Pilihan Tidak Ada")

    case 3: #Buah Segar
        print("""
        1. Mangga 1kg Rp. 45.000
        2. Anggur 1kg Rp. 80.000
        3. Apel 1kg Rp. 30.000
        4. Jeruk 1kg Rp. 16.000
        5. Salak 1kg Rp. 15.000
        6. Pisang 1kg Rp. 22.00
        7. Semangka 1kg Rp. 60.000
        8. Buah Naga 1kg Rp. 32.000
        9. Strawberry 1kg Rp. 90.000
        10. Nanas 1kg Rp. 15.000
        """)
        BuahSegar = int(input("Pilih Merk Yang Ingin Kamu Beli : "))
        jenisBuahSegar = ""
        hargaBuahSegar = 0

        if BuahSegar == 1:
            jenisBuahSegar += "Mangga 1kg"
            hargaBuahSegar += 45000
        elif BuahSegar == 2:
            jenisBuahSegar += "Anggur 1kg"
            hargaBuahSegar += 80000
        elif BuahSegar == 3:
            jenisBuahSegar += "Apel 1kg"
            hargaBuahSegar += 30000
        elif BuahSegar == 4:
            jenisBuahSegar += "Jeruk 1kg"
            hargaBuahSegar += 16000
        elif BuahSegar == 5:
            jenisBuahSegar += "Salak 1kg"
            hargaBuahSegar += 15000
        elif BuahSegar == 6:
            jenisBuahSegar += "Pisang 1kg"
            hargaBuahSegar += 22000
        elif BuahSegar == 7:
            jenisBuahSegar += "Semangka 1kg"
            hargaBuahSegar += 60000
        elif BuahSegar == 8:
            jenisBuahSegar += "Buah Naga 1kg"
            hargaBuahSegar += 32000
        elif BuahSegar == 9:
            jenisBuahSegar += "Strawberry 1kg"
            hargaBuahSegar += 90000
        elif BuahSegar == 10:
            jenisBuahSegar += "Nanas 1kg"
            hargaBuahSegar += 15000
        else:
            print("Pilihan Tidak Ada")

        banyakBuahSegar = int(input("Banyak Barang Yang Ingin Dibeli : "))
        totalHargaBuahSegar = hargaBuahSegar * banyakBuahSegar
        print("Harga Yang Dibayarkan Adalah : ", totalHargaBuahSegar)
        dealBuahSegar = input("Apakah Anda Ingin Melanjutkan Transaksi? ")
        if dealBuahSegar == "Ya" or dealBuahSegar == "ya" or dealBuahSegar == "y":
            print("""
            1. Cash
            2. Debit BNI (Potongan 5%)
            3. Debit BCA (Potongan 2%)
            4. Debit BRI (Free Pulsa 5rb)
            """)
            diskonBuahSegarBNI = totalHargaBuahSegar - potonganBNI
            diskonBuahSegarBCA = totalHargaBuahSegar - potonganBCA
            metodePembayaranBuahSegar = int(input("Silahkan Pilih Metode Pembayaran Anda : "))

            if metodePembayaranBuahSegar == 1:
                print("Harga Yang Anda Bayarkan Adalah Rp. ", totalHargaBuahSegar)
                konfirmasiPembayaranBNIBuahSegar = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                if konfirmasiPembayaranBNIBuahSegar == "Y" or konfirmasiPembayaranBNIBuahSegar == "y":
                    print("=== Invoice ===")
                    print(f"""
                    Pesanan : {BuahSegar}
                    Harga   : {totalHargaBuahSegar}
                    Terimakasih Telah Melakukan Transaksi
                    """)
                else:
                    print("Transaksi Gagal!")

            elif metodePembayaranBuahSegar == 2:
                print("=== Data Pembayaran ===")
                nomorKartu = input("Nomor Kartu : ")
                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonBuahSegarBNI)
                konfirmasiPembayaranBNIBuahSegar = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                if konfirmasiPembayaranBNIBuahSegar == "Y" or konfirmasiPembayaranBNIBuahSegar == "y":
                    print("=== Invoice ===")
                    print(f"""
                    Pesanan : {BuahSegar}
                    Harga   : {diskonBuahSegarBNI}
                    Terimakasih Telah Melakukan Transaksi
                    """)
                else:
                    print("Transaksi Gagal!")

            elif metodePembayaranBuahSegar == 3:
                print("=== Data Pembayaran ===")
                nomorKartu = input("Nomor Kartu : ")
                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonBuahSegarBCA)
                konfirmasiPembayaranBCABuahSegar = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                if konfirmasiPembayaranBCABuahSegar == "Y" or konfirmasiPembayaranBCABuahSegar == "y":
                    print("=== Invoice ===")
                    print(f"""
                    Pesanan : {BuahSegar}
                    Harga   : {diskonBuahSegarBCA}
                    Terimakasih Telah Melakukan Transaksi
                    """)
                else:
                    print("Transaksi Gagal!")

            elif metodePembayaranBuahSegar == 4:
                print("=== Data Pembayaran ===")
                nomorKartu = input("Nomor Kartu : ")
                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonBuahSegarBCA)
                konfirmasiPembayaranBCABuahSegar = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                if konfirmasiPembayaranBCABuahSegar == "Y" or konfirmasiPembayaranBCABuahSegar == "y":
                    print("Anda Mendapatkan Free Pulsa Senilai Rp. 5.000")
                    freePulsaBuahSegarBRI = input("Nomor HP : ")
                    print("=== Invoice ===")
                    print(f"""
                    Pesanan    : {BuahSegar}
                    Free       : Pulsa Rp. 5.000
                    No. Tujuan : {freePulsaBuahSegarBRI}
                    Harga      : {diskonBuahSegarBCA}
                    Terimakasih Telah Melakukan Transaksi
                    """)
                else:
                    print("Transaksi Gagal!")

            else:
                print("Pilihan Tidak Tersedia")

        else:
            print("Pilihan Tidak Tersedia")

    
    case 4: #Sayur Segar
        print("""
        1. Bayam 1kg Rp. 21.000
        2. Kangkung 1kg Rp. 15.000
        3. Sawi 1kg Rp. 18.000
        4. Pak Choy 1kg Rp. 24.000
        5. Daun Singkong 1kg Rp. 13.000
        6. Wortel 1kg Rp. 23.00
        7. Kentang 1kg Rp. 44.000
        8. Tomat 1kg Rp. 23.000
        9. Labu 1kg Rp. 21.000
        10. Terong 1kg Rp. 23.000
        11. Labu Siam Rp. 30.000
        12. Kol Rp. 14.000
        13. Jamur Rp. 14.000
        14. Selada Rp. 21.000
        15. Buncis Rp. 30.000
        """)
        SayurSegar = int(input("Pilih Merk Yang Ingin Kamu Beli : "))
        jenisSayurSegar = ""
        hargaSayurSegar = 0

        if SayurSegar == 1:
            jenisSayurSegar += "Bayam 1kg"
            hargaSayurSegar += 21000
        elif SayurSegar == 2:
            jenisSayurSegar += "Kangkung 1kg"
            hargaSayurSegar += 15000
        elif SayurSegar == 3:
            jenisSayurSegar += "Sawi 1kg"
            hargaSayurSegar += 18000
        elif SayurSegar == 4:
            jenisSayurSegar += "Pak Choy 1kg"
            hargaSayurSegar += 24000
        elif SayurSegar == 5:
            jenisSayurSegar += "Daun Singkong 1kg"
            hargaSayurSegar += 13000
        elif SayurSegar == 6:
            jenisSayurSegar += "Wortel 1kg"
            hargaSayurSegar += 23000
        elif SayurSegar == 7:
            jenisSayurSegar += "Kentang 1kg"
            hargaSayurSegar += 44000
        elif SayurSegar == 8:
            jenisSayurSegar += "Tomat 1kg"
            hargaSayurSegar += 23000
        elif SayurSegar == 9:
            jenisSayurSegar += "Labu 1kg"
            hargaSayurSegar += 21000
        elif SayurSegar == 10:
            jenisSayurSegar += "Terong 1kg"
            hargaSayurSegar += 23000
        elif SayurSegar == 11:
            jenisSayurSegar += "Labu Siam 1kg"
            hargaSayurSegar += 30000
        elif SayurSegar == 12:
            jenisSayurSegar += "Kol 1kg"
            hargaSayurSegar += 14000
        elif SayurSegar == 13:
            jenisSayurSegar += "Jamur 1kg"
            hargaSayurSegar += 14000
        elif SayurSegar == 14:
            jenisSayurSegar += "Selada 1kg"
            hargaSayurSegar += 21000
        elif SayurSegar == 15:
            jenisSayurSegar += "Buncis 1kg"
            hargaSayurSegar += 30000
        else:
            print("Pilihan Tidak Ada")

        banyakSayurSegar = int(input("Banyak Barang Yang Ingin Dibeli : "))
        totalHargaSayurSegar = hargaSayurSegar * banyakSayurSegar
        print("Harga Yang Dibayarkan Adalah : ", totalHargaSayurSegar)
        dealSayurSegar = input("Apakah Anda Ingin Melanjutkan Transaksi? ")
        if dealSayurSegar == "Ya" or dealSayurSegar == "ya" or dealSayurSegar == "y":
            print("""
            1. Cash
            2. Debit BNI (Potongan 5%)
            3. Debit BCA (Potongan 2%)
            4. Debit BRI (Free Pulsa 5rb)
            """)
            diskonSayurSegarBNI = totalHargaSayurSegar - potonganBNI
            diskonSayurSegarBCA = totalHargaSayurSegar - potonganBCA
            metodePembayaranSayurSegar = int(input("Silahkan Pilih Metode Pembayaran Anda : "))

            if metodePembayaranSayurSegar == 1:
                print("Harga Yang Anda Bayarkan Adalah Rp. ", totalHargaSayurSegar)
                konfirmasiPembayaranBNISayurSegar = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                if konfirmasiPembayaranBNISayurSegar == "Y" or konfirmasiPembayaranBNISayurSegar == "y":
                    print("=== Invoice ===")
                    print(f"""
                    Pesanan : {SayurSegar}
                    Harga   : {totalHargaSayurSegar}
                    Terimakasih Telah Melakukan Transaksi
                    """)
                else:
                    print("Transaksi Gagal!")

            elif metodePembayaranSayurSegar == 2:
                print("=== Data Pembayaran ===")
                nomorKartu = input("Nomor Kartu : ")
                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonSayurSegarBNI)
                konfirmasiPembayaranBNISayurSegar = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                if konfirmasiPembayaranBNISayurSegar == "Y" or konfirmasiPembayaranBNISayurSegar == "y":
                    print("=== Invoice ===")
                    print(f"""
                    Pesanan : {SayurSegar}
                    Harga   : {diskonSayurSegarBNI}
                    Terimakasih Telah Melakukan Transaksi
                    """)
                else:
                    print("Transaksi Gagal!")

            elif metodePembayaranSayurSegar == 3:
                print("=== Data Pembayaran ===")
                nomorKartu = input("Nomor Kartu : ")
                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonSayurSegarBCA)
                konfirmasiPembayaranBCASayurSegar = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                if konfirmasiPembayaranBCASayurSegar == "Y" or konfirmasiPembayaranBCASayurSegar == "y":
                    print("=== Invoice ===")
                    print(f"""
                    Pesanan : {SayurSegar}
                    Harga   : {diskonSayurSegarBCA}
                    Terimakasih Telah Melakukan Transaksi
                    """)
                else:
                    print("Transaksi Gagal!")

            elif metodePembayaranSayurSegar == 4:
                print("=== Data Pembayaran ===")
                nomorKartu = input("Nomor Kartu : ")
                print("Harga Yang Anda Bayarkan Adalah Rp. ", diskonSayurSegarBCA)
                konfirmasiPembayaranBCASayurSegar = input("Apakah anda Ingin Melanjutkan Pembayaran (Y/N): ")
                if konfirmasiPembayaranBCASayurSegar == "Y" or konfirmasiPembayaranBCASayurSegar == "y":
                    print("Anda Mendapatkan Free Pulsa Senilai Rp. 5.000")
                    freePulsaSayurSegarBRI = input("Nomor HP : ")
                    print("=== Invoice ===")
                    print(f"""
                    Pesanan    : {SayurSegar}
                    Free       : Pulsa Rp. 5.000
                    No. Tujuan : {freePulsaSayurSegarBRI}
                    Harga      : {diskonSayurSegarBCA}
                    Terimakasih Telah Melakukan Transaksi
                    """)
                else:
                    print("Transaksi Gagal!")

            else:
                print("Pilihan Tidak Tersedia")

        else:
            print("Pilihan Tidak Tersedia")


    case 5: #EXIT
        print("==== Terimakasih Telah Berkunjung, Silahkan Datang Kembali ====")

    case _:
        print("Pilihan Tidak Tersedia")


