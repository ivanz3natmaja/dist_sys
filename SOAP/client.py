#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:52:27 2024

@author: widhi
"""
from zeep import Client

# URL WSDL menggunakan nama service Docker Compose
wsdl = 'http://soap-server:8000/?wsdl'

# Membuat klien SOAP berdasarkan WSDL
client = Client(wsdl=wsdl)

# Memanggil metode perkalian selisih kuadrat  dari layanan SOAP server (modified)
result = client.service.add(20, 30)

# Menampilkan hasil penjumlahan
print(f'Hasil penjumlahan dari server SOAP: {result}')

