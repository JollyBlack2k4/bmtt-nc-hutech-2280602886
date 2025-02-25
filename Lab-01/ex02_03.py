#Nhập số người dùng 
so = int(input("Nhập một sô nguyên : "))
#Kiểm tra xem số đo có phải số chẳn hay không 
if so % 2 == 0:
    print(so, "là số chẳn.")
else:
    print(so, "Không phải là số chẳn.")