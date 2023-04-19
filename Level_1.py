"""Bài 1: """ 
""" Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, 
nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). 
Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy. """

j = [] #Tạo một danh sách rỗng để lưu kết quả
for i in range(2000, 3201): #Duyệt qua tất cả các số trong đoạn từ 2000 đến 3200
    if (i%7==0) and (i%5!=0): #Kiểm tra xem số i có chia hết cho 7 và không phải là bội số của 5 không
        j.append(str(i)) #Nếu đúng, thì thêm số i vào danh sách result
        lis = ', '.join(j) # thêm dấu "," vào xâu 
print(lis)
--------------------------------------------------------------------------------------------------------

"""Bài 2: """ 
""" Viết một chương trình có thể tính giai thừa của một số cho trước. 
Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy.
Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320. """

x = int(input("Nhập số cần tính giai thừa: "))
def fact(x):
    if x == 0:
        return 1 # vì 0! = 1
    return x * fact(x - 1) #trường hợp này có thể xem thành vòng lặp 
print (fact(x))
--------------------------------------------------------------------------------------------------------

"""Bài 3: """ 
