def selamlama(fn):
    def inner(ad):
        print("hoş geldiniz")
        fn(ad)
        print("görüşmek üzere")
        return inner

@selamlama
def gunaydin(ad):
    print("Hoşgeldiniz")
    print("görüşürüz")

    print(f"Günaydın adım {ad}")

@selamlama
def iyigunler(ad):
    print(f"İyi günler adım {ad}")
    
g = selamlama(gunaydin)
i = selamlama(iyigunler)

gunaydin()
iyigunler()