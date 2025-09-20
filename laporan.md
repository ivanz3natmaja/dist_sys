

## LK 01: Lingkungan Praktik Mandiri + Ujicoba Messaging Protocols

I Wayan Ivan Zenatmaja - 2546000075

1. Buat Lingkungan Praktik Mandiri berbasis VSCode+GitHub Copilot, WSL2 + Ubuntu, Docker Container
   
   <img src="file:///C:/Users/Wayan/AppData/Roaming/marktext/images/2025-09-19-14-58-05-image.png" title="" alt="" width="396">
   
   Gambar 1. Tampilan sudah berada di Lingkungan Praktik Mandiri. 
   
   2. Fork Repository Program: [GitHub - abazh/dist_sys: Distributed System Hands-On](https://github.com/abazh/dist_sys) ke dalam akun Github @ivanz3natmaja

![](C:\Users\Wayan\AppData\Roaming\marktext\images\2025-09-19-14-56-13-image.png)

Gambar  2. Tampilan github sudah dilakukan fork 

3. Menginstal extension yang dibutuhkan untuk menganalisis protokol pada repositori
   
   <img src="file:///C:/Users/Wayan/AppData/Roaming/marktext/images/2025-09-19-20-40-24-image.png" title="" alt="" width="479">
   
   Gambar 3. Menginstal extension vsc-webshark

4.  Pastikan mengarahkan lokasinya pada  usr/bin/sharkd
   
   ![](C:\Users\Wayan\AppData\Roaming\marktext\images\2025-09-20-17-58-40-image.png)
   
   Gambar 4. Tampilan pengaturan pada vsc-webshark  (Bagian sharkd full path)

5. Lakukan ujicoba per protocol dan modifikasi yang diperlukan

sudo apt install wireshark -y

## **Protokol MQTT**

- Melakukan docker compose pada mqtt.yml

`docker compose -f compose/mqtt.yml up -d`

![](C:\Users\Wayan\AppData\Roaming\marktext\images\2025-09-20-18-11-11-image.png)

Gambar  5. Tampilan mempraktekkan docker compose

- Pada file pub.py dilakukan modifikasi  seolah-olah ini menggunakan platform YT ceritanya

<img src="file:///C:/Users/Wayan/AppData/Roaming/marktext/images/2025-09-20-18-56-00-image.png" title="" alt="" width="529">

Gambar 6.  Modifikasi baris 21-23

![](C:\Users\Wayan\AppData\Roaming\marktext\images\2025-09-20-18-55-10-image.png)

Gambar 7. Modifikasi baris 47-48

- Pada file sub.py dilakukan modifikasi 
  
  <img src="file:///C:/Users/Wayan/AppData/Roaming/marktext/images/2025-09-20-19-02-44-image.png" title="" alt="" width="440">
  
  Gambar 8. Modifikasi baris 15-16

- Melakukan split terminal dan melaksanakan masing-masing perintah pada masing-masing terminal
  
  `docker compose -f compose/mqtt.yml exec mqtt-sub python sub.py`
  
  `docker compose -f compose/mqtt.yml exec mqtt-pub python pub.py`

- Kemudian coba dilakukan, ternyata pelanggan tidak dapat menerima pesan, karena kanalnya berbeda antara sub dan pub
  
  ![](C:\Users\Wayan\AppData\Roaming\marktext\images\2025-09-20-20-48-28-image.png)
  
  Gambar 9. Tampilan sub.py yang tidak menerima pesan, meski berhasil terhubung ke broker

- Coba disamakan topicnya sister/channel/gaming di sub.py. 
  
  <img src="file:///C:/Users/Wayan/AppData/Roaming/marktext/images/2025-09-20-20-53-33-image.png" title="" alt="" width="447">
  
  Gambar 10. Pengubahan topic pada sub.py (Menyamakan dengan pub.py)

![](C:\Users\Wayan\AppData\Roaming\marktext\images\2025-09-20-20-50-35-image.png)

Gambar 11. sub.py berhasil terhubung

- Untuk melakukan pengecekan ip untuk mengetahui proses mqtt yang terjadi

<img title="" src="file:///C:/Users/Wayan/AppData/Roaming/marktext/images/2025-09-20-21-04-49-image.png" alt="" width="424">

Gambar 12. Tampilan melakukan perintah ip a

<img src="file:///C:/Users/Wayan/AppData/Roaming/marktext/images/2025-09-20-20-57-19-image.png" title="" alt="" width="365">

Gambar 13. Tampilan didapatkan br-.... 

<img title="" src="file:///C:/Users/Wayan/AppData/Roaming/marktext/images/2025-09-20-21-08-24-image.png" alt="" width="462">

Gambar 14. Tampilan melakukan perintah sudo apt install tcpdump

- Melakukan analisis mqtt.pcap

<img src="file:///C:/Users/Wayan/AppData/Roaming/marktext/images/2025-09-20-21-13-22-image.png" title="" alt="" width="479">

Gambar 15. Tampilan melakukan perintah sudo tcp dump

![](C:\Users\Wayan\AppData\Roaming\marktext\images\2025-09-20-21-45-02-image.png)

Gambar 16. Tampilan mqtt.pcap

- **Aliran utama:** komunikasi antar host 172.18.0.2, 172.18.0.3, dan 172.18.0.4.

- **Aktivitas MQTT:** semua paket yang terlihat adalah **Publish Message** ke topik:
  
  `sister/channel/gaming`



## Protokol TCP

- Melakukan docker compose pada reqresp.yml

`docker compose -f compose/reqresp.yml up -d`

![](C:\Users\Wayan\AppData\Roaming\marktext\images\2025-09-20-18-33-38-image.png)

Gambar 17. Tampilan mempraktekkan docker compose

- Melakukan split terminal dan melaksanakan masing-masing perintah pada masing-masing terminal
  
  `docker compose -f compose/reqresp.yml exec reqresp-server python server.py`
  
  `docker compose -f compose/reqresp.yml exec reqresp-client python client.py`
  
  ![](C:\Users\Wayan\AppData\Roaming\marktext\images\2025-09-20-22-31-27-image.png)
  
  Gambar 18. Tampilan dilakukan split terminal

- Melakukan tangkapan melalui tcp dump
  
  <img src="file:///C:/Users/Wayan/AppData/Roaming/marktext/images/2025-09-20-22-39-58-image.png" title="" alt="" width="502">
  
  Gambar 19. Tampilan tcp dump

- Melakukan analisis tcp.pcap
  
  ![](C:\Users\Wayan\AppData\Roaming\marktext\images\2025-09-20-22-44-09-image.png)
  
  Gambar 20. Tampilan membuka tcp.pcap
  
  - **Aktivitas TCP:** pertukaran pesan antara host 172.18.0.6 dan 172.18.0.5 melalui port 2222 yang kemudian ditutup secara normal dengan FIN-ACK
  
  - **Aliran utama:** komunikasi antar host 172.18.0.6 dan 172.18.0.5.
  
  - Kode tidak dilakukan modifikasi apapun
    
    

# Protokol SOAP

- Melakukan modifikasi kode pada protokol SOAP dengan metode perkalian selisih kuadrat

![](C:\Users\Wayan\AppData\Roaming\marktext\images\2025-09-20-23-27-48-image.png)

Gambar 21. modifikasi pada client.py

![](C:\Users\Wayan\AppData\Roaming\marktext\images\2025-09-20-23-28-38-image.png)

Gambar 22. modifikasi pada server.py

- Melakukan docker compose
  
  `docker compose -f compose/soap.yml up -d`

<img src="file:///C:/Users/Wayan/AppData/Roaming/marktext/images/2025-09-20-23-31-22-image.png" title="" alt="" width="481">

Gambar 23.  Melakukan tahapan docker compose

- Melakukan split terminal serta menangkap proses melalui wireshark
  
  Melaksanakan perintah:
  
  `docker compose -f compose/soap.yml exec soap-server python server.py`
  
  `docker compose -f compose/soap.yml exec soap-client python client.py`

<img title="" src="file:///C:/Users/Wayan/AppData/Roaming/marktext/images/2025-09-20-23-32-32-image.png" alt="" width="715">

didapatkan hasil -500.

Gambar 24. Tahapan split terminal

- Melakukan analisis pada soap.pcap (Setelah direname dari rest.pcap)

![](C:\Users\Wayan\AppData\Roaming\marktext\images\2025-09-20-23-34-55-image.png)

Gambar 25. Tampilan wireshark

- **Aktivitas SOAP:** pertukaran pesan antara host 172.18.0.6 dan 172.18.0.5 melalui port 8000 yang kemudian ditutup secara normal.

- **Aliran utama:** komunikasi antar host 172.18.0.6 dan 172.18.0.5.



# Protokol Upcall

![](C:\Users\Wayan\AppData\Roaming\marktext\images\2025-09-21-00-02-29-image.png)

Gambar 26. Tampilan docker compose



![](C:\Users\Wayan\AppData\Roaming\marktext\images\2025-09-21-00-03-51-image.png)

Gambar 27. Tampilan Split Terminal



![](C:\Users\Wayan\AppData\Roaming\marktext\images\2025-09-21-00-04-11-image.png)

Gambar 28. Tampilan Split Terminal



![](C:\Users\Wayan\AppData\Roaming\marktext\images\2025-09-21-00-05-59-image.png)

Gambar 29. Tampilan upcall.pcap (Setelah direname dari upcall.pcap)

Tidak ada modifikasi kode sama sekali

Aktivitas Upcall : TCP (dengan beberapa payload `PSH, ACK`) + 1 ARP announcement

Aliran utama : Komunikasi **172.18.0.12** (client, port 38992) dengan **172.18.0.7** (server, port 4141)
