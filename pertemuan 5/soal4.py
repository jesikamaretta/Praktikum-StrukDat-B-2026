transaksi = [ 
{"produk": "Buku", "harga": 10000, "jumlah": 3}, 
{"produk": "Pena", "harga": 5000, "jumlah": 10}, 
{"produk": "Penghapus", "harga": 2000, "jumlah": 2} 
] 


for item in transaksi:
    if item['produk'] == 'buku':
        item['produk'] = 8

produk_baru1= {'produk' :'kuas', 'harga' :8000, 'jumlah: 8'}