class SuperList(list):
    def __len__(self):
        return 1000


superList1 = SuperList()
print(len(superList1))
superList1.append(5)
print(superList1)
superList1.append(10)
print(superList1)
superList1.append(20)
print(superList1)
superList1.append(10)
print(superList1)
superList1.append(11)
print(superList1)
superList1.append(13)
print(superList1)
print(superList1[5])
print(issubclass(SuperList, list))
