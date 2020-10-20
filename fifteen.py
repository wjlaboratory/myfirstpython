class Text:
    def __int__(self):
        pass
    def big(self):
        n,m = 0,0
        def a():
            nonlocal n
            n += 1
            print(n)
            if n==1:
                print("one")
            elif n==2:
                print("two")
        a()
        a()
if __name__=='__main__':
    text = Text()
    text.big()
