class Function:
    def __init__(self, f, df):
        self.f = f
        self.df = df
    def __call__(self, x, grad = False):
        if grad:
            return self.df(x)
        else:
            return self.f(x)
    def __add__(self, other):
        return Function(lambda x: self.f(x)+other.f(x), lambda x: self.df(x)+other.df(x))
    def __sub__(self, other):
        return Function(lambda x: self.f(x)-other.f(x), lambda x: self.df(x)-other.df(x))
    def __mul__(self, other):
        return Function(lambda x: self.f(x)*other.f(x), lambda x: self.df(x)*other.f(x)+self.f(x)*other.df(x))
    def __truediv__(self, other):
        return Function(lambda x: self.f(x)/other.f(x), lambda x: (self.df(x)*other.f(x)-self.f(x)*other.df(x))/(other.f(x)*other.f(x)))
    def __matmul__(self, other):
        return Function(lambda x: self.f(other.f(x)), lambda x: self.df(other.f(x))*other.df(x))