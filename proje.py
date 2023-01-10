print("solucan klası")
class Solucan:
    def __init__(self, sinif, cins):      #iki değişken oluşturuyoruz.
        self.sinifi = sinif
        self.cinsi = cins
    def __str__(self):           #__str__ ile print fonksiyonunu yazıyoruz.
        return "Solucanlar; Yassı, Yuvarlak, Halkalı olarak ayrılırlar."
    def tanit(self):    #kendimiz fonksiyonlar oluşturuyoruz.
        print(f"{self.cinsi}, hayvanlar aleminin {self.sinifi} sınıfında bulunur.")
    def ozellik_ver(self):
        print("Ömrü 2-6 yıl kadardır.")
    def solucana_isim_ver(self):
        solucanismi = str(input("solucana isim ver"))
        print(solucanismi)
        

#Kodun çalıştırılması       
solucan1 = Solucan("Omurgasızlar","Yassı Solucan")
print(solucan1.sinifi)    #özellikleri çağırırken parantez kullanmıyoruz.
print(solucan1.cinsi)
print(solucan1)
solucan1.tanit()        #fonksiyonları çağırırken parantez kullanıyoruz.
solucan1.ozellik_ver()
solucan1.solucana_isim_ver()




# In[52]:

print("--------------------------kurbağa klası-------------------------")
class Kurbaga(Solucan): #İçerisine Solucan yazarak Solucan class'ından miras alıyoruz.
    def __str__(self):  #__str__ fonksiyonunu override ediyoruz. Artık Solucan class'ındaki yerine bu geçerli olacak.
        return """Kurbağalar: Hayvanlar aleminin Omurgalılar sınıfında bulunurlar.
        Toplam 33 familyaya dağılmış yaklaşık 5250 türü bulunur."""
    def ozellik_ver(self):
        print("Amfibi (ikiyaşamlı) canlılardır.")
    def puan_ver(self):
        puan = int(input("Kurbağalara 10 üzerinden kaç puan verirdiniz?"))
        if puan <10:
            print("Yanlış cevap. 10 puan olacaktı.")
        else:
            print("Çok doğru")
        

#Kodun çalıştırılması
kurbaga1 = Kurbaga("Omurgalılar", "Toprak Kurbağası")
print(kurbaga1.sinifi)
print(kurbaga1.cinsi)
print(kurbaga1)
kurbaga1.tanit()
kurbaga1.ozellik_ver()
kurbaga1.puan_ver()




# In[53]:

print("----------------------balık klası--------------------")
class Balik():
    def __init__(self,sinif, cins):
        self.sinifi = sinif
        self.cinsi = cins
    def ornek_ver(self):
        balik_listesi = ["Yılan Balığı","Vatoz Balığı", "Somon", "Orkinos"]
        if self in balik_listesi:
            balik_listesi.remove(self)
        else:
            print("Balıklara örnekler:\n", balik_listesi)
    def pop_quiz(self):
        cevap = input("Balık yemeyenlere ne denir?")
        if cevap.lower() == "pesketaryen":
            print("Doğru!!")
        else:
            print("Yanlış.. Pesketaryen.")
    
    
    

#Kodun çalışması
balik1 = Balik("Omurgalılar", "Levrek")
print(balik1.sinifi)
print(balik1.cinsi)
balik1.ornek_ver()
balik1.pop_quiz()


# In[54]:
print("----------------------sünger klası---------------------")

class Sunger():
    def __init__(self,sinif,cins):
        self.sinifi = sinif
        self.cinsi = cins
    def __len__(self):         #normalde listelerde çalışan len() fonksiyonunu biz tanımlıyoruz.
        print("Tanımlanmış yaklaşık 5000 türü vardır.")
    def soru_sor(self):
        cvp = input("En ünlü sünger kimdir?")
        if cvp.lower() == "süngerbob":
            print("Doğru cevap!!")
        else:
            print("Bilemedin, süngerbob olacaktı.")
    def bilgi_ver(self):
        print("Süngerler, en ilkel çok hücreli canlı gruplarındandır.")

#Kodun çalışması
sunger1 = Sunger("Omurgasızlar", "Deniz süngeri")
print(sunger1.sinifi)
print(sunger1.cinsi)
sunger1.__len__()
sunger1.bilgi_ver()
sunger1.soru_sor()



# In[55]:

print("--------------------eklem bacaklılar klası--------------------")
class Eklembacak():
    def __init__(self,sinif,cins):
        self.sinifi = sinif
        self.cinsi = cins
    def __len__(self):
        print("Tanımlanmış yaklaşık 1 milyon türü vardır.")
    
    def bilgi_ver(self):
        print("Eklembacaklılar, Omurgasızların en büyük grubudur.")
    
    def ornek_ver(self):
        print("Karada örümcekler, akrepler ve böcekler;/n denizlerdeyse yengeçler ve karidesler eklembacaklılara örnektir.")
    def en_korkunc_eklem_bacakli(self):
        bocek = str(input("en korkunç böcek nedir"))
        if bocek.lower() == "örümcek":
            print("Doğru cevap!!")
        else:
            print("o da korkunç ama en korkuncu örümcek")
        
    
#Kodun çalışması
eklembacak1 = Eklembacak("Omurgasızlar", "Örümcek")
print(eklembacak1.sinifi)
print(eklembacak1.cinsi)
eklembacak1.bilgi_ver() 
eklembacak1.ornek_ver()
eklembacak1.en_korkunc_eklem_bacakli()



# In[56]:
print("-----------------------kedi klası-------------------")

class Kedi:
    def __init__(self, cins, goz_renk, tuy_renk):
        self.cins = cins
        self.goz_renk = goz_renk
        self.tuy_renk = tuy_renk
    def miyavla(self):
        print("Miyaaaav")
    def insan_yasi_karsiligi(self, kedi_yasi):
        if kedi_yasi == 1:
            print("1 yaşındaki kedinin insan yaşı: 15")
        elif kedi_yasi == 2:
            print("2 yaşındaki kedinin insan yaşı: 24")
        else:
            print(f"{kedi_yasi} yaşındaki kedinin yaşı:")
            kedi_yasi = 24 + (kedi_yasi-2)*4
            print(kedi_yasi)
    def en_guzel_kedi_rengi(self):
        renk = str(input("en güzel kedi rengi nedir"))
        if renk.lower() == "turuncu":
            print("bence deeeee")
        else:
            print("hayır bence turuncu.")


#Kodun çalışması
kedi1 = Kedi("Sibirya","mavi","beyaz")
print("eylülün kedisinin göz rengi :" , kedi1.goz_renk)
print("kedinin tüy rengi : " , kedi1.tuy_renk)
print("eylülün kedisinin cinsi :" , kedi1.cins)
print("kedi şöyle ses çıkarır : " )
kedi1.miyavla()
kedi1.en_guzel_kedi_rengi()



# In[57]:

print("----------------------------köpek klası -----------------------------:")

class Kopek:
        def __init__(self,cins= "",cinsiyet="",yas="1"):  #kullanıcı verileri girmeyince attribute'ların alacağı değerleri belirliyoruz.
            self.cinsi = cins
            self.cinsiyeti = cinsiyet
            self.yasi = yas
        def ses_cikar(self):
            print("kızgın köpek ne der ? : Havhavhav")
        def insan_yasina_cevir(self):
            x = int(input("evcil hayvanınızın yaşı kaç ?"))
            if x == 1:
                print("evcil hayvanınızın insan yaşı: 15")
            elif x == 2:
                print("evcil hayvanınızın insan yaşı: 24")
            else:
                insan_yasi = 24 + ((x-2)*5)
                print(f'{x} yaşındaki evcil hayvanınızın insan yaşı:{insan_yasi}')
                
            #Operator overloading: Python'da var olan bir operator fonksiyonun bizim class'ımızda çalışması için tekrar yazmak. 
            #Mesela __add__(self,other) => toplama, __sub__(self,other) => çıkarma , __mul__(self,other) =>çarpma
        def __add__(self,other): #Operator overloading yapıyoruz.
            return self.yasi + other.yasi   #burada other dediğimiz toplayacağımız diğer class elemanı
        def en_guzel_kopek_cinsi(self):
            cinss = str(input("en güzel köpek cinsi nedirr"))
            if cinss.lower() == "pitbul":
                print("bence deeeee")
            else:
                print("hayır bence pitbul")
        

#kodun çalışması     
kopek1 = Kopek("Labrador","erkek",4)   
kopek2 = Kopek("Poodle","dişi",2)
print("benim köpeğimin cinsi :" , kopek1.cinsi)
print("benim köpeğimin cinsiyeti :" , kopek1.cinsiyeti)
print("benim köpeğimin yaşı :" , kopek2.yasi)
kopek2.ses_cikar()
kopek1.insan_yasina_cevir()

print("birinci ve ikinci kopeğin yaşları toplmııı : ",kopek1 + kopek2)  #__add__ fonksiyonumuzla 2 köpeğin yaşlarını topluyoruz.
kopek1.en_guzel_kopek_cinsi()


# In[58]:

print("---------------------papağan klası------------------------")
class Papagan(Kopek):   #miras
    def ses_cikar(self):     #override
        x = input("papağan ne diye ses çıkarır")
        print(x)
        

#kodun çalışması         
papagan1 = Papagan("Sultan","erkek",55)
papagan2 = Papagan("Afrika Gri","dişi",45)  
print("1 numaralı papağanın cinsi" , papagan1.cinsi)
print("2 numaralı papağanın cinsi" , papagan2.cinsiyeti)
print("2 numaralı papağanın yaşı" , papagan2.yasi)
papagan1.ses_cikar()
papagan1.insan_yasina_cevir()

print(papagan1 + papagan2) #__add__ fonksiyonunu çağırabiliyoruz çünkü Kopek class'ından miras aldık.
