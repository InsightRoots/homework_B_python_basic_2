# a = [1 ,2 ,3]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for A in a:
#     for B in b:
#         print(f"Aの中身{A}, Bの中身{B}",end=' ')

# dan = int(input("なんのだん？"))
# kake = int(input("なにかける？"))
#
# kake = [1,2,3,4]
# dan = [1]
# for k in kake:
#     for d in dan:
#         print(d*k,d*k*2,)

n = int(input("行数を入力してください: "))
m = int(input("列数を入力してください: "))
for g in range(1, n+1):
    for j in range(1, m+1) :
        print(g * j, end=" ")
    print()

# 出来たー！！！！！！！！！！！！！！！！

# dan = [1,2]
# kakeru = [1,2,3,4]
# for d in dan:
#     for k in kakeru:
#         print(d             *k,end=' ')
#
# for i in range(5):
#     for y in range(3):
#         print(i * y,end=" ")

#もういややー！
#
# multi_dan = [1]
# multi_kake = [1,2,3,4,5,6,7,8,9]
# for dan in multi_dan :
#     for kake in multi_kake :
#         print(kake,kake*list(range(10)))

# ぜんっぜんわからん！！！！！！！！！！！！！！！！！！！
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for A in a:
#     for B in b:
#         print(f"Aの中身{A}, Bの中身{B}")
# a = [1, 2]
# b = [4, 5]
# for A in a:
#     for B in b:
#         print(f"Aの中身{A}, Bの中身{B}",end=' ')

#
# a = [n for n in range(5)]
# print(a)


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for A in a:
#     for B in b:
#         print(f"Aの中身{A},\n"
#               f""f"Bの中身{B}",end=' ')