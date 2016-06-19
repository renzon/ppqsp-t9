class Chamavel:

    def __call__(self, *args, **kwargs):
        print('executei', id(self))

c1=Chamavel()
print(c1())
