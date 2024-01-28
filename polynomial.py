class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub): #including Sub as possible first term
            if isinstance(self.p2, Add) or isinstance(self.p1, Sub): #including Sub as possible second term
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub): #including Sub as possible second term (int * sub)
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)
    
class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub): #if first term is Add or Sub
            if isinstance(self.p2, Add) or isinstance(self.p1, Sub): #if second term is Add or Sub
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2) #first term is add or sub, second term is int
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub): #first term is int, second term is add or sub
            return repr(self.p1) + " / ( " + repr(self.p2) + " )" 
        return repr(self.p1) + " / " + repr(self.p2) #both terms are int

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)

#More tests below
poly2 = Div( Int(5), Sub( X(), Int(1)))
print(poly2)

poly3 = Sub( Sub( Int(4), Int(3)), Add( X(), Div( Int(1), Sub( Mul(X(), X()), Int(1)))))
print(poly3)

poly4 = Sub( Sub( Int(4), Int(3)), Add( X(), Mul( Int(1), Sub( Mul(X(), X()), Int(1)))))
print(poly4)

