
disk_size_mb = 1.44
page_count = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4


disk_size_bytes = disk_size_mb * 1_048_576

total_chars = page_count * lines_per_page * chars_per_line
book_size_bytes = total_chars * bytes_per_char


books_on_disk = disk_size_bytes // book_size_bytes


print("Количество книг, помещающихся на дискету:", int(books_on_disk))
