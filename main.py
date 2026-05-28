price=float(input("Nhập đơn giá của sản phẩm: "))
total=int(input("Nhập số lượng cần mua: "))
sum_price=price*total
if (sum_price >= 1000000):
    payment = sum_price* 0.9
else:
    payment=sum_price
print("So tien ban phai thanh toan la: ",payment)
password='123456'
total_password=0
while total_password<3:
    input_pw =input("Nhap mat khau cua ban: ")
    if (input_pw == password):
        print("Đăng nhập thành công!")
        break
    else:
        total_password += 1
    if (total_password<3):
        print("Mật khẩu sai, vui lòng nhập lại!")
    else:
        print("Tai khoan da bi khoa")
    
total_product = 0
box = 0
print("he thong kiem dem lo hang ")
print("Nhap so '0' de dung chuong trinh")
while True:
    total_product_box= int (input("Nhập số lượng sản phẩm của thùng: "))
    if(total_product_box <0):
        print("Số lượng không hợp lệ, bỏ qua thùng này!")
    elif total_product_box == 0:
        print("Chuong trinh da kiem dem xong")
        break
    else:
        total_product += total_product_box
        box+=1
print("Tong thung hang da dem la: ",box)
print("Tong so luong san pham thu duoc: ",total_product)