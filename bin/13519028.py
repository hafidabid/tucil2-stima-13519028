class Graf :
    def __init__(self,ArrayData):
        '''
        CLASS CONSTRUCTOR
        :param ArrayData: berisikan list of list hasil konversi dari txt menuju ke list of list
        '''
        self.data = self.__extractData(ArrayData)
        self.jmlhElmen = self.getJumlahData()

    def __extractData(self,data):
        '''
        FUNGSI UNTUK MERUBAH DATA MENJADI SEBUAH
        FORMAT GRAF (DICTIONARY BERISIKAN ID NODE DAN GRAF YANG MENGARAH KE NODE BERSANGKUTAN)
        :param data: BERUPA LIST OF LIST,FUNCTION INI PRIVATE
        :return: SEBUAH GRAF DALAM BENTUK  DICTIONARY BERISIKAN ID NODE DAN GRAF YG MENGARAH KE NODE BERSANGKUTAN
        '''
        r = []
        for x in data:
            temp = {}
            if(len(x)>0):
                temp["id"] = x[0]
                temp["preq"] = []
                for y in range(1,len(x)):
                    temp["preq"].append(x[y])
                r.append(temp)
        return r

    def removeGraf(self,key):
        '''
        UNTUK MENGHAPUS GRAF YANG TIDAK MEMILIKI PREC YG MENGARAH DAN MENGHAPUS PREC DARI SEMUA
        NODE YANG BERASAL DARI GRAF YANG DIHAPUS
        :param key: ID Node yang ingin dihapus
        :return: mengembalikan boolean apakah ID nodal yang di input diparameter apakah berhasil dihapus dari graf
        '''
        newdata = []
        status = True
        for x in self.data:
            if(x["id"]==key and len(x["preq"])>0):
                status = 1==2
            elif(x["id"]!=key):
                if(key in x["preq"]):
                    x["preq"].remove(key)
                newdata.append(x)
        if(status):
            self.data = newdata
        return status

    def getNoPreq(self):
        '''
        UNTUK MENDAPATKAN GRAF YANG TIDAK MEMILIKI PREC / PANAH YANG MENGARAH KE SUATU NODE
        :return: LIST OF NO PREC NODE
        '''
        return [x["id"] for x in self.data if (len(x["preq"])==0)]

    def getJumlahData(self):
        '''
        :return: mengembalikan jumlah nodal
        '''
        return len(self.data)

def readfiles(flname):
    '''
    memproses file txt menjadi sebuah list of list
    :param flname: nama file txt yang terdapat pada folder test
    :return: list of list hasil pemrosesan file txt
    '''
    flname  = flname + "" if ".txt" in flname else flname + ".txt"
    txt = open("../test/" + flname , 'r').readlines()
    for x in txt:
        if "." not in x: return []
    return [x.strip().replace('.','').replace(" ","").split(sep=",") for x in txt]

def runTopologiSort(objekGraf,semester=1):
    '''
    melakukan topologi sort dengan menghapus node/matkul yang udah tidak memiliki prequiset lagi scr rekursif
    :param objekGraf: objek dari class graf
    :param semester: semester pengambilan, default = 1
    :return: merupakan prosedur rekursif, sehingga tidak ada return
    '''
    if objekGraf.getJumlahData()==0:
        if semester==1:
            print("Tidak ada data")
        else:
            print("topologi sort selesai!")
    else:
            noPreq = objekGraf.getNoPreq()
            if(len(noPreq)==0):
                print("Graf mengandung sirkular sehingga tidak bisa lanjutkan topologi sort")
            else:
                print("Semester "+str(semester)+": ",end='')
                for id in noPreq:
                    print(str(id)+" ",end='')
                    objekGraf.removeGraf(id)
                print()
                runTopologiSort(objekGraf,semester+1)

def validate(listMatkul):
    '''
    memvalidasi apakah txt sudah sesuai dengan format yang ditentukan asisten
    :param listMatkul: list of list hasil dari pembacaan file txt
    :return: boolean apakah valid atau tidak
    '''
    if(len(listMatkul)==0): return False
    z = ""
    for x in listMatkul:
        z = z + str(x)
    z = z.replace("[", "").replace("]", "").replace("'", "").replace(",", "").lower()
    x =0
    while(x<len(z)):
        if not ( (z[x]>='a' and z[x]<='z') or (z[x]>='0' and z[x]<='9') or z[x]==" " or z[x]=="-" or z[x]=="_"):
            return False
        else: x=x+1
    return True

if __name__ == "__main__":
    namafile = input("masukkan nama file test = ")
    data = readfiles(namafile)
    if validate(data):
        runTopologiSort(Graf(data))
    else:
        print("data tidak valid, pastikan format di file txt telah benar dan diakhir baris dikasih titik (format kelas hanya mengandung alfabet, numerik,-,dan _) contoh: Stima_01")
