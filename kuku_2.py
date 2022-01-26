# dan = int(input("なんのだん？"))
# kake = int(input("なにかける？"))
# print(dan,dan*2,dan*3)
# print(dan*kake)

dan = [1,2]
kakeru = [1,2,3,4,5,6,7,8,9]
for d in dan:
    for k in kakeru:
        print(d * k,end=' ')

#いったん飛ばす！！！！！！！！もういややー！
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