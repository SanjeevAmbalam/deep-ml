class Value:
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.grad = 0
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op
    def __repr__(self):
        def fmt(x):
            return int(x) if float(x).is_integer() else round(x, 4)
        return f"Value(data={fmt(self.data)}, grad={fmt(self.grad)})"

    def __add__(self, other):
         # Implement addition here
        out = Value(self.data+other.data, (self, other), '+')
        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward 
        return out

    def __mul__(self, other):
        # Implement multiplication here
        out = Value(self.data*other.data, (self, other), '*')
        def _backward():
            self.grad += out.grad * other.data
            other.grad += out.grad * self.data
        out._backward = _backward
        return out

    def relu(self):
        # Implement ReLU here
        if self.data>0:
            out = Value(self.data, (self,), 'relu')
        elif self.data<0:
            out = Value(0, (self,), 'relu')
        def _backward():
            if self.data>0:
                self.grad += out.grad
        out._backward = _backward
        return out

    def backward(self):
        # Implement backward pass here
        topo = []
        visited = set(topo)
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)

        # self.grad is 1 because derivative w/ respect to itself is always 1
        self.grad = 1
        for item in reversed(topo):
            item._backward()
