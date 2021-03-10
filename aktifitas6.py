class student:
 """ A Class Representating A Student """
 def __init__(self, n, a, r, t, ns, k):
    self.full_name=n
    self.age=a
    self.rank=r
    self.team=t
    self.namasekolah=ns
    self.kota=k
 def get_age(self):
    return self.age
 def get_rank(self):
    return self.rank
 def get_team(self):
    return self.team
 def get_namasekolah(self):
    return self.namasekolah
 def get_kota(self):
    return self.kota
f = student ("Uzumaki Naruto",18,"Gennin","Team 7","Konoha Academy School","Konoha")
print(f.full_name)
print(f.get_age())
print(f.get_rank())
print(f.get_team())
print(f.get_namasekolah())
print(f.get_kota())


