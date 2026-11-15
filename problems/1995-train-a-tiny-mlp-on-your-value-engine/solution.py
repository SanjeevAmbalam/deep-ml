import math
import random


# ---- provided: the scalar autograd engine from micrograd (do not change) ----
class Value:
    def __init__(self, data, _children=(), _op=""):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op

    def __repr__(self):
        return f"Value(data={self.data:.4f}, grad={self.grad:.4f})"

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), "+")
        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), "*")
        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward
        return out

    def __pow__(self, k):
        assert isinstance(k, (int, float)), "only int or float powers"
        out = Value(self.data ** k, (self,), f"**{k}")
        def _backward():
            self.grad += k * self.data ** (k - 1) * out.grad
        out._backward = _backward
        return out

    def tanh(self):
        t = math.tanh(self.data)
        out = Value(t, (self,), "tanh")
        def _backward():
            self.grad += (1 - t ** 2) * out.grad
        out._backward = _backward
        return out

    def backward(self):
        topo, visited = [], set()
        def build(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build(child)
                topo.append(v)
        build(self)
        self.grad = 1.0
        for v in reversed(topo):
            v._backward()

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + (-other)

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return other + (-self)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return self * other ** -1
# ---- end provided ----


class Neuron:
    def __init__(self, nin):
        """nin weights, then a bias, each a Value drawn with random.uniform(-1, 1), in that order."""
        self.w = [Value(random.uniform(-1, 1)) for i in range(nin)]
        self.b = Value(random.uniform(-1, 1))

    def __call__(self, x):
        """tanh of the weighted sum of the inputs plus the bias, as a Value."""
        act = sum(wi*xi for wi, xi in zip(self.w, x)) + self.b
        out = act.tanh()
        return out

    def parameters(self):
        """The weights, then the bias."""
        return self.w + [self.b]


class Layer:
    def __init__(self, nin, nout):
        """nout neurons, each taking nin inputs, created in order."""
        self.neurons = [Neuron(nin) for i in range(nout)]

    def __call__(self, x):
        """Every neuron's output on x, in order; a single Value when the layer has one neuron."""
        out = [n(x) for n in self.neurons]
        if len(self.neurons)==1: return out[0]
        return out

    def parameters(self):
        """Every neuron's parameters, neuron by neuron."""
        out = []
        for p in self.neurons:
            out+=p.parameters()
        return out


class MLP:
    def __init__(self, nin, nouts):
        """Layers of sizes nouts, the first taking nin inputs, each the next one's input."""
        lz = [nin] + nouts
        self.layers = [Layer(lz[i], lz[i+1]) for i in range(len(nouts))]

    def __call__(self, x):
        """Run x through the layers in order."""
        for l in self.layers:
            x = l(x)
        return x

    def parameters(self):
        """Every layer's parameters, layer by layer."""
        out = []
        for l in self.layers:
            out+=l.parameters()
        return out


def train(model, xs, ys, steps, lr):
    """Full-batch gradient descent on the summed squared-error loss.

    Returns a list of `steps` floats: each step's loss, measured before that step's update.
    """
    losses = []
    for _ in range(steps):
        # forward pass
        ypds = [model(x) for x in xs]
        # backward pass
        for p in model.parameters():
            p.grad = 0
        loss = sum((y_pred-y_acc)**2 for y_pred, y_acc in zip(ypds, ys))
        # update 
        losses.append(loss.data)
        loss.backward()
        for p in model.parameters():
            p.data -= lr*p.grad 
    return losses