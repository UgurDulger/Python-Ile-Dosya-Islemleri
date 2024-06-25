#19010011026 uğur DÜLGER

A_list = []
Son_Id = 100
Id = 100
Dosya = open("19010011026.txt","a")
Dosya.close()

def Kişi_Ekle():
    global Id
    global A_list
    global Dosya

    def SonIdBul():
        global Id
        global Son_Id
        global Dosya
        kontol = []
        with open("19010011026.txt","r+") as Dosya:
            U = Dosya.readlines()
            for C in U:
                D = C.split(" ")
                K = D[0]
                Son_Id = int(K)
                kontol.append(Son_Id)
                Son_Id = Son_Id + 1
        Id = Son_Id
        for i in range(len(kontol)):
            if i != len(kontol) - 1:
                u = kontol[i]
                c = kontol[i+1]
                d = c - u
                if d > 1:
                    Id = kontol[x]+1
        if kontol[0] != 100:
             Id =100

    with open("19010011026.txt", "r") as Dosya:
        x = Dosya.readlines()
        for a in x:
            if a != "":
                SonIdBul()

    Oyuncu_Adi = input("Oyuncu Adını Giriniz :")
    Oyun_Adi = input("Oyun Adını Giriniz :")
    Harcanan_Para = input("Oyunda Harcanan Parayı Giriniz :")
    Harcanan_Sure= input("Oyunda Harcanan Süreyi Giriniz :")

    A_list.append(Id)
    A_list.append(Oyuncu_Adi)
    A_list.append(Oyun_Adi)
    A_list.append(Harcanan_Para)
    A_list.append(Harcanan_Sure)

    with open("19010011026.txt", "a") as Dosya:
        for A in A_list:
            Dosya.writelines("{} ".format(A))
        Dosya.writelines("\n")

    A_list.clear()

    def Id_Sirala():

        global Dosya
        IdSirala_List = []
        Ind = 0
        with open("19010011026.txt", "r") as Dosya:
            A = Dosya.readlines()
            for B in A:
                if B != "":
                    C = B.split(" ")
                    IdSirala_List.append(list())
                for x in range(len(C)):
                    if x != 5:
                        IdSirala_List[Ind].append(C[x])
                Ind = Ind + 1
        IdSirala_List.sort()
        with open("19010011026.txt", "w") as Dosya:
            for A in IdSirala_List:
                for B in range(len(A)):
                    Dosya.writelines("{} ".format(A[B]))
                Dosya.writelines("\n")
    Id_Sirala()


Kişi_Ekle()