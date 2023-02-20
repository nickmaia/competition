###############################################################
####### By Elder Vicente de Paulo Sobrinho - UFTM #############
###############################################################
## http://maratona.sbc.org.br/ambiente20/python3.txt
## http://maratona.ime.usp.br/primfase19/provas/competicao/info_maratona.pdf
## Tamanho do arquivo-fonte: 100KB (este arquivo tem 40KB ou seja, seu código pode ter + 60KB)
## Podemos embarcar o numpy ou melhor tinynumpy https://github.com/wadetb/tinynumpy
## Versão para embarcar e usar na maratona de programação........
## Coloquei seu código no final do arquivo
from __future__ import division
from __future__ import absolute_import
import sys
import ctypes
from math import sqrt
from copy import copy, deepcopy
from collections.abc import Iterable
import operator

class LinAlgError(Exception):
    pass

_dtypes = [('B', 'b1', 'bool', ctypes.c_bool),
           ('b', 'i1', 'int8', ctypes.c_int8),
           ('B', 'u1', 'uint8', ctypes.c_uint8),
           ('h', 'i2', 'int16', ctypes.c_int16),
           ('H', 'u2', 'uint16', ctypes.c_uint16),
           ('i', 'i4', 'int32', ctypes.c_int32),
           ('I', 'u4', 'uint32', ctypes.c_uint32),
           ('q', 'i8', 'int64', ctypes.c_int64),
           ('Q', 'u8', 'uint64', ctypes.c_uint64),
           ('f', 'f4', 'float32', ctypes.c_float),
           ('d', 'f8', 'float64', ctypes.c_double), ]

_known_dtypes = [d[2] for d in _dtypes]
for d in _known_dtypes:
    globals()[d] = d

newaxis = None
nan = float('nan')

def _convert_dtype(dtype, to='numpy'):
    if dtype is None:
        return dtype
    dtype = str(dtype)
    index = {'array':0, 'short':1, 'numpy':2, 'ctypes':3}[to]
    for dd in _dtypes:
        if dtype in dd:
            return dd[index]
    return dtype

def _ceildiv(a, b):
    return -(-a // b)


def _get_step(view):
    cont_strides = _strides_for_shape(view.shape, view.itemsize)
    step = view.strides[-1] // cont_strides[-1]
    corrected_strides = tuple([i * step for i in cont_strides])
    almost_cont = view.strides == corrected_strides
    if almost_cont:
        return step
    else:
        return 0


def _strides_for_shape(shape, itemsize):
    strides = []
    stride_product = 1
    for s in reversed(shape):
        strides.append(stride_product)
        stride_product *= s
    return tuple([i * itemsize for i in reversed(strides)])


def _size_for_shape(shape):
    stride_product = 1
    for s in shape:
        stride_product *= s
    return stride_product


def squeeze_strides(s):
    return tuple([s[0]] + [s[i] for i in range(1, len(s)) if s[i] != s[i-1]])


def _shape_from_object(obj):
    shape = []
    def _shape_from_object_r(index, element, axis):
        try:
            for i, e in enumerate(element):
                _shape_from_object_r(i, e, axis+1)
            while len(shape) <= axis:
                shape.append(0)
            l = i + 1
            s = shape[axis]
            if l > s:
                shape[axis] = l
        except TypeError:
            pass
    _shape_from_object_r(0, obj, 0)
    return tuple(shape)


def _assign_from_object(array, obj):
    key = []
    def _assign_from_object_r(element):
        try:
            for i, e in enumerate(element):
                key.append(i)
                _assign_from_object_r(e)
                key.pop()
        except TypeError:
            array[tuple(key)] = element
    _assign_from_object_r(obj)


def _increment_mutable_key(key, shape):
    for axis in reversed(range(len(shape))):
        key[axis] += 1
        if key[axis] < shape[axis]:
            return True
        if axis == 0:
            return False
        key[axis] = 0


def _key_for_index(index, shape):
    key = []
    cumshape = [1]
    for i in reversed(shape):
        cumshape.insert(0, cumshape[0] * i)
    for s in cumshape[1:-1]:
        n = index // s
        key.append(n)
        index -= n * s
    key.append(index)
    return tuple(key)


def _zerositer(n):
    for i in range(n):
        yield 0


## Public functions
def array(obj, dtype=None, copy=True, order=None):
    dtype = _convert_dtype(dtype)
    if isinstance(obj, ndarray):
        a = obj.view()
        if dtype is not None and dtype != a.dtype:
            a = a.astype(dtype)
        elif copy:
            a = a.copy()
        return a
    if hasattr(obj, '__array_interface__'):
        D = obj.__array_interface__
        dtype_orig = _convert_dtype(D['typestr'][1:])
        if D['strides']:
            itemsize = int(D['typestr'][-1])
            bufsize = D['strides'][0] * D['shape'][0] // itemsize
        else:
            bufsize = _size_for_shape(D['shape'])
        BufType = (_convert_dtype(dtype_orig, 'ctypes') * bufsize)
        buffer = BufType.from_address(D['data'][0])
        a = ndarray(D['shape'], dtype_orig,
                    buffer=buffer, strides=D['strides'], order=order)
        if dtype is not None and dtype != dtype_orig:
            a = a.astype(dtype)
        elif copy:
            a = a.copy()
        return a
    else:
        shape = _shape_from_object(obj)
        if dtype is None:
            el = obj
            while isinstance(el, (tuple, list)) and el:
                el = el[0]
            if isinstance(el, int):
                dtype = 'int64'
        a = ndarray(shape, dtype, order=None)
        _assign_from_object(a, obj)
        return a


def zeros_like(a, dtype=None, order=None):
    dtype = a.dtype if dtype is None else dtype
    return zeros(a.shape, dtype, order)

def ones_like(a, dtype=None, order=None):
    dtype = a.dtype if dtype is None else dtype
    return ones(a.shape, dtype, order)

def empty_like(a, dtype=None, order=None):
    dtype = a.dtype if dtype is None else dtype
    return empty(a.shape, dtype, order)

def zeros(shape, dtype=None, order=None):
    return empty(shape, dtype, order)

def ones(shape, dtype=None, order=None):
    a = empty(shape, dtype, order)
    a.fill(1)
    return a

def eye(size):
    a = zeros((size,size))
    for i in range(size):
        a[i,i] = 1
    return a


def empty(shape, dtype=None, order=None):
    return ndarray(shape, dtype, order=order)


def arange(*args, **kwargs):
    dtype = kwargs.pop('dtype', None)
    if kwargs:
        x = list(kwargs.keys())[0]
        raise TypeError('arange() got an unexpected keyword argument %r' % x)
    if len(args) == 0:
        raise TypeError('Required argument "start" not found')
    elif len(args) == 1:
        start, stop, step = 0, int(args[0]), 1
    elif len(args) == 2:
        start, stop, step = int(args[0]), int(args[1]), 1
    elif len(args) == 3:
        start, stop, step = int(args[0]), int(args[1]), int(args[2])
    else:
        raise TypeError('Too many input arguments')
    # Init
    iter = range(start, stop, step)
    a = empty((len(iter),), dtype=dtype)
    a[:] = list(iter)
    return a


def linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None):
    start, stop = float(start), float(stop)
    ra = stop - start
    if endpoint:
        step = ra / (num-1)
    else:
        step = ra / num
    a = empty((num,), dtype)
    a[:] = [start + i * step for i in range(num)]
    if retstep:
        return a, step
    else:
        return a

def add(ndarray_vec1, ndarray_vec2):
    c = []
    for a, b in zip(ndarray_vec1, ndarray_vec2):
        c.append(a+b)
    cRay = array(c)
    return cRay

def subtract(ndarray_vec1, ndarray_vec2):
    c = []
    for a, b in zip(ndarray_vec1, ndarray_vec2):
        c.append(a-b)
    cRay = array(c)
    return cRay

def multiply(ndarray_vec1, ndarray_vec2):
    c = []
    for a, b in zip(ndarray_vec1, ndarray_vec2):
        c.append(a*b)
    cRay = array(c)
    return cRay

def divide(ndarray_vec1, integer):
    c = []
    for a in ndarray_vec1:
        c.append(a / integer)
    cRay = array(c)
    return cRay

def cross(u, v):
    uDim = len(u)
    vDim = len(v)
    uxv = []
    if uDim == vDim == 2:
        try:
            uxv = [u[0]*v[1]-u[1]*v[0]]            
        except LinAlgError as e:
            uxv = e        
    elif uDim == vDim == 3:
        try:
            for i in range(uDim):
                uxv = [u[1]*v[2]-u[2]*v[1], -(u[0]*v[2]-u[2]*v[0]),
                       u[0]*v[1]-u[1]*v[0]]
        except LinAlgError as e:
            uxv = e
    else:
        raise IndexError('Vector has invalid dimensions')
    return uxv

def dot(u, v):
    uDim = len(u)
    vDim = len(v)
    if uDim == vDim:
        try:
            u_dot_v = sum(map(operator.mul, u, v))
        except LinAlgError as e:
            u_dot_v = e
    else:
        raise IndexError('Vector has invalid dimensions')
    return u_dot_v

def reshape(X,shape):
    assert isinstance(X, ndarray)
    assert isinstance(shape, tuple) or isinstance(shape, list)
    return X.reshape(shape)

class ndarray(object):    
    __slots__ = ['_dtype', '_shape', '_strides', '_itemsize', 
                 '_offset', '_base', '_data']
    def __init__(self, shape, dtype='float64', buffer=None, offset=0,
                 strides=None, order=None):
        if order is not None:
            raise RuntimeError('ndarray order parameter is not supported')
        try : 
            assert isinstance(shape, Iterable)
            shape = tuple(shape)
        except Exception as e:
            raise AssertionError('The shape must be tuple or list')
        assert all([isinstance(x, int) for x in shape])
        self._shape = shape
        dtype = _convert_dtype(dtype) if (dtype is not None) else 'float64'
        if dtype not in _known_dtypes:
            raise TypeError('data type %r not understood' % dtype)
        self._dtype = dtype
        self._itemsize = int(_convert_dtype(dtype, 'short')[-1])
        if buffer is None:
            self._base = None
            assert offset == 0
            self._offset = 0
            assert strides is None
            self._strides = _strides_for_shape(self._shape, self.itemsize)
        else:
            if isinstance(buffer, ndarray) and buffer.base is not None:
                buffer = buffer.base
            self._base = buffer
            if isinstance(buffer, ndarray):
                buffer = buffer.data
            assert isinstance(offset, int) and offset >= 0
            self._offset = offset
            if strides is None:
                strides = _strides_for_shape(shape, self.itemsize)
            assert isinstance(strides, tuple)
            assert all([isinstance(x, int) for x in strides])
            assert len(strides) == len(shape)
            self._strides = strides
        buffersize = self._strides[0] * self._shape[0] // self._itemsize
        buffersize += self._offset
        BufferClass = _convert_dtype(dtype, 'ctypes') * buffersize
        if buffer is None:
            self._data = BufferClass()
        elif isinstance(buffer, ctypes.Array):
            self._data = BufferClass.from_address(ctypes.addressof(buffer))
        else:
            self._data = BufferClass.from_buffer(buffer)
    
    @property
    def __array_interface__(self):
        readonly = False
        typestr = '<' + _convert_dtype(self.dtype, 'short')
        if isinstance(self._data, ctypes.Array):
            ptr = ctypes.addressof(self._data)
        elif hasattr(self._data, '__array_interface__'):
            ptr, readonly = self._data.__array_interface__['data']
        elif hasattr(self._data, 'buffer_info'):  # Python's array.array
            ptr = self._data.buffer_info()[0]
        elif isinstance(self._data, bytes):
            ptr = ctypes.cast(self._data, ctypes.c_void_p).value
            readonly = True
        else:
            raise TypeError('Cannot get address to underlying array data')
        ptr += self._offset * self.itemsize
        #
        return dict(version=3,
                    shape=self.shape,
                    typestr=typestr,
                    descr=[('', typestr)],
                    data=(ptr, readonly),
                    strides=self.strides,
                    )
    
    def __len__(self):
        return self.shape[0]
    
    def __getitem__(self, key):
        offset, shape, strides = self._index_helper(key)
        if not shape:
            return self._data[offset]
        else:
            return ndarray(shape, self.dtype,
                           offset=offset, strides=strides, buffer=self)
    
    def __setitem__(self, key, value):
        offset, shape, strides = self._index_helper(key)
        if not shape:
            self._data[offset] = value
            return
        view = ndarray(shape, self.dtype,
                        offset=offset, strides=strides, buffer=self)
        if isinstance(value, (float, int)):
            value_list = [value] * view.size
        elif isinstance(value, (tuple, list)):
            value_list = value
        else:
            if not isinstance(value, ndarray):
                value = array(value, copy=False)
            value_list = value._toflatlist()
        if view.size != len(value_list):
            raise ValueError('Number of elements in source does not match '
                                'number of elements in target.')
        subviews = [view]
        value_index = 0
        count = 0
        while subviews:
            subview = subviews.pop(0)
            step = _get_step(subview)
            if step:
                block = value_list[value_index:value_index+subview.size]
                s = slice(subview._offset, 
                            subview._offset + subview.size * step, 
                            step)
                view._data[s] = block
                value_index += subview.size
                count += 1
            else:
                for i in range(subview.shape[0]):
                    subviews.append(subview[i])
        assert value_index == len(value_list)
    
    def __float__(self):
        if self.size == 1:
            return float(self.data[self._offset])
        else:
            raise TypeError('Only length-1 arrays can be converted to scalar')
    
    def __int__(self):
        if self.size == 1:
            return int(self.data[self._offset])
        else:
            raise TypeError('Only length-1 arrays can be converted to scalar')
    
    def __repr__(self):
        if self.size > 100:
            shapestr = 'x'.join([str(i) for i in self.shape])
            return '<ndarray %s %s at 0x%x>' % (shapestr, self.dtype, id(self))
        def _repr_r(s, axis, offset):
            axisindent = min(2, max(0, (self.ndim - axis - 1)))
            if axis < len(self.shape):
                s += '['
                for k_index, k in enumerate(range(self.shape[axis])):
                    if k_index > 0:
                        s += ('\n       ' + ' ' * axis)  * axisindent
                    offset_ = offset + k * self._strides[axis] // self.itemsize
                    s = _repr_r(s, axis+1, offset_)
                    if k_index < self.shape[axis] - 1:
                        s += ', '
                s += ']'
            else:
                r = repr(self.data[offset])
                if '.' in r:
                    r = ' ' + r
                    if r.endswith('.0'):
                        r = r[:-1]
                s += r
            return s

        s = _repr_r('', 0, self._offset)
        if self.dtype != 'float64' and self.dtype != 'int32':
            return "array(" + s + ", dtype='%s')" % self.dtype
        else:
            return "array(" + s + ")"
    
    def __eq__(self, other):
        if other.__module__.split('.')[0] == 'numpy':
            return other == self
        else:
            out = empty(self.shape, 'bool')
            out[:] = [i1==i2 for (i1, i2) in zip(self.flat, other.flat)]
            return out
    
    def __add__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) :
            out = empty(self.shape, self.dtype)
            out[:] = [dat+other for dat in self._data] 
            return out
        if (isinstance(other, ndarray)):
            if self.shape == other.shape :
                out = empty(self.shape, self.dtype)
                out[:] = [i+j for (i,j) in zip(self.flat, other.flat)]
                return out

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) :
            out = empty(self.shape, self.dtype)
            out[:] = [dat-other for dat in self._data] 
            return out
        if (isinstance(other, ndarray)):
            if self.shape == other.shape :
                out = empty(self.shape, self.dtype)
                out[:] = [i-j for (i,j) in zip(self.flat, other.flat)]
                return out

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) :
            out = empty(self.shape, self.dtype)
            out[:] = [dat*other for dat in self._data] 
            return out
        if (isinstance(other, ndarray)):
            if self.shape == other.shape :
                out = empty(self.shape, self.dtype)
                out[:] = [i*j for (i,j) in zip(self.flat, other.flat)]
                return out       

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) :
            if other == 0 : raise ZeroDivisionError
            out = empty(self.shape, self.dtype)
            out[:] = [dat/other for dat in self._data] 
            return out
        if (isinstance(other, ndarray)):
            if self.shape == other.shape :
                out = empty(self.shape, self.dtype)
                out[:] = [i/j for (i,j) in zip(self.flat, other.flat)]
                return out
            else :
                raise ValueError('Array sizes do not match. '+str(self.shape)\
                                                  +' versus '+str(other.shape))

    def __truediv__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) :
            if other == 0 : raise ZeroDivisionError
            out = empty(self.shape, self.dtype)
            out[:] = [dat/other for dat in self._data] 
            return out
        if (isinstance(other, ndarray)):
            if self.shape == other.shape :
                out = empty(self.shape, self.dtype)
                out[:] = [i/j for (i,j) in zip(self.flat, other.flat)]
                return out
            else :
                raise ValueError('Array sizes do not match. '+str(self.shape)\
                                                  +' versus '+str(other.shape))

    def __floordiv__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) :
            if other == 0 : raise ZeroDivisionError
            out = empty(self.shape, self.dtype)
            out[:] = [dat//other for dat in self._data] 
            return out
        if (isinstance(other, ndarray)):
            if self.shape == other.shape :
                out = empty(self.shape, self.dtype)
                out[:] = [i//j for (i,j) in zip(self.flat, other.flat)]
                return out
            else :
                raise ValueError('Array sizes do not match. '+str(self.shape)\
                                                  +' versus '+str(other.shape))

    def __mod__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) :
            out = empty(self.shape, self.dtype)
            out[:] = [dat%other for dat in self._data] 
            return out
        if (isinstance(other, ndarray)):
            if self.shape == other.shape :
                out = empty(self.shape, self.dtype)
                out[:] = [i%j for (i,j) in zip(self.flat, other.flat)]
                return out
            else :
                raise ValueError('Array sizes do not match. '+str(self.shape)\
                                                  +' versus '+str(other.shape))

    def __pow__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) :
            out = empty(self.shape, self.dtype)
            out[:] = [dat**other for dat in self._data] 
            return out
        if (isinstance(other, ndarray)):
            if self.shape == other.shape :
                out = empty(self.shape, self.dtype)
                out[:] = [i**j for (i,j) in zip(self.flat, other.flat)]
                return out
            else :
                raise ValueError('Array sizes do not match. '+str(self.shape)\
                                                  +' versus '+str(other.shape))

    def __iadd__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) :
            for i in range(len(self._data)):
                self._data[i]+=other
            return self
        if (isinstance(other, ndarray)):
            if self.shape == other.shape :
                for i in range(len(self._data)):
                    self._data[i]+=other._data[i]
                return self            
            else :
                raise ValueError('Array sizes do not match. '+str(self.shape)\
                                                  +' versus '+str(other.shape))

    def __isub__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) :
            for i in range(len(self._data)):
                self._data[i]-=other
            return self
        if (isinstance(other, ndarray)):
            if self.shape == other.shape :
                for i in range(len(self._data)):
                    self._data[i]-=other._data[i]
                return self
            else :
                raise ValueError('Array sizes do not match. '+str(self.shape)\
                                                  +' versus '+str(other.shape))

    def __imul__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) :
            for i in range(len(self._data)):
                self._data[i]*=other
            return self
        if (isinstance(other, ndarray)):
            if self.shape == other.shape :
                for i in range(len(self._data)):
                    self._data[i]*=other._data[i]
                return self
            else :
                raise ValueError('Array sizes do not match. '+str(self.shape)\
                                                  +' versus '+str(other.shape))

    def __idiv__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) :
            if other == 0 : raise ZeroDivisionError
            for i in range(len(self._data)):
                self._data[i]/=other
            return self
        if (isinstance(other, ndarray)):
            if self.shape == other.shape :
                for i in range(len(self._data)):
                    self._data[i]/=other._data[i]
                return self
            else :
                raise ValueError('Array sizes do not match. '+str(self.shape)\
                                                  +' versus '+str(other.shape))

    def __itruediv__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) :
            if other == 0 : raise ZeroDivisionError
            for i in range(len(self._data)):
                self._data[i]/=other
            return self
        if (isinstance(other, ndarray)):
            if self.shape == other.shape :
                for i in range(len(self._data)):
                    self._data[i]/=other._data[i]
                return self
            else :
                raise ValueError('Array sizes do not match. '+str(self.shape)\
                                                  +' versus '+str(other.shape))

    def __ifloordiv__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) :
            if other == 0 : raise ZeroDivisionError
            for i in range(len(self._data)):
                self._data[i]//=other
            return self
        if (isinstance(other, ndarray)):
            if self.shape == other.shape :
                for i in range(len(self._data)):
                    self._data[i]//=other._data[i]
                return self
            else :
                raise ValueError('Array sizes do not match. '+str(self.shape)\
                                                  +' versus '+str(other.shape))

    def __imod__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) :
            if other == 0 : raise ZeroDivisionError
            for i in range(len(self._data)):
                self._data[i]%=other
            return self
        if (isinstance(other, ndarray)):
            if self.shape == other.shape :
                for i in range(len(self._data)):
                    self._data[i]%=other._data[i]
                return self
            else :
                raise ValueError('Array sizes do not match. '+str(self.shape)\
                                                  +' versus '+str(other.shape))

    def __imod__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) :
            if other == 0 : raise ZeroDivisionError
            for i in range(len(self._data)):
                self._data[i]%=other
            return self
        if (isinstance(other, ndarray)):
            if self.shape == other.shape :
                for i in range(len(self._data)):
                    self._data[i]%=other._data[i]
                return self
            else :
                raise ValueError('Array sizes do not match. '+str(self.shape)\
                                                  +' versus '+str(other.shape))

    def __ipow__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) :
            for i in range(len(self._data)):
                self._data[i]**=other
            return self
        if (isinstance(other, ndarray)):
            if self.shape == other.shape :
                for i in range(len(self._data)):
                    self._data[i]**=other._data[i]
                return self
            else :
                raise ValueError('Array sizes do not match. '+str(self.shape)\
                                                  +' versus '+str(other.shape))


    ## Private helper functions
    def _index_helper(self, key):
        if not isinstance(key, tuple):
            key = (key,)
        axis = 0
        shape = []
        strides = []
        offset = self._offset
        for k in key:
            axissize = self._shape[axis]
            if isinstance(k, int):
                if k >= axissize:
                    raise IndexError('index %i is out of bounds for axis %i '
                                     'with size %s' % (k, axis, axissize))
                offset += k * self._strides[axis] // self.itemsize
                axis += 1
            elif isinstance(k, slice):
                start, stop, step = k.indices(self.shape[axis])
                shape.append(_ceildiv(stop - start, step))
                strides.append(step * self._strides[axis])
                offset += start * self._strides[axis] // self.itemsize
                axis += 1
            elif k is Ellipsis:
                raise TypeError("ellipsis are not supported.")
            elif k is None:
                shape.append(1)
                stride = 1
                for s in self._strides[axis:]:
                    stride *= s
                strides.append(stride)
            else:
                raise TypeError("key elements must be instaces of int or slice.")
        shape.extend(self.shape[axis:])
        strides.extend(self._strides[axis:])
        return offset, tuple(shape), tuple(strides)
    
    def _toflatlist(self):
        value_list = []
        subviews = [self]
        count = 0
        while subviews:
            subview = subviews.pop(0)
            step = _get_step(subview)
            if step:
                s = slice(subview._offset, 
                          subview._offset + subview.size * step, 
                          step)
                value_list += self._data[s]
                count += 1
            else:
                for i in range(subview.shape[0]):
                    subviews.append(subview[i])
        return value_list
    
    @property
    def ndim(self):
        return len(self._shape)
    
    @property
    def size(self):
        return _size_for_shape(self._shape)
    
    @property
    def nbytes(self):
        return _size_for_shape(self._shape) * self.itemsize
    
    def _get_shape(self):
        return self._shape
    
    def _set_shape(self, newshape):
        if newshape == self.shape:
            return
        if self.size != _size_for_shape(newshape):
            raise ValueError('Total size of new array must be unchanged')
        if _get_step(self) == 1:
            self._shape = tuple(newshape)
            self._strides = _strides_for_shape(self._shape, self.itemsize)
            return
        N = self.ndim
        shape = [self.shape[i] for i in range(N) if self.shape[i] > 1]
        strides = [self.strides[i] for i in range(N) if self.shape[i] > 1]
        newshape_ = [newshape[i] for i in range(len(newshape)) 
                     if newshape[i] > 1]
        if newshape_ != shape:
            raise AttributeError('incompatible shape for non-contiguous array')
        strides.append(strides[-1])
        shape.append(1)
        i = -1
        newstrides = []
        try:
            for s in reversed(newshape):
                if s == 1:
                    newstrides.append(strides[i] * shape[i])
                else:
                    i -= 1
                    newstrides.append(strides[i])
        except IndexError:
            raise AttributeError('incompatible shape for non-contiguous array')
        else:
            newstrides.reverse()
            self._shape = tuple(newshape)
            self._strides = tuple(newstrides)
    shape = property(_get_shape, _set_shape)  # Python 2.5 compat (e.g. Jython)
    
    @property
    def strides(self):
        return self._strides
    
    @property
    def dtype(self):
        return self._dtype
    
    @property
    def itemsize(self):
        return self._itemsize
    
    @property
    def base(self):
        return self._base
    
    @property
    def data(self):
        return self._data
    
    @property
    def flat(self):
        subviews = [self]
        count = 0
        while subviews:
            subview = subviews.pop(0)
            step = _get_step(subview)
            if step:
                s = slice(subview._offset, 
                          subview._offset + subview.size * step, 
                          step)
                for i in self._data[s]:
                    yield i
            else:
                for i in range(subview.shape[0]):
                    subviews.append(subview[i])
    
    @property
    def T(self):
        if self.ndim < 2:
            return self
        else:
            return self.transpose()
    
    @property
    def flags(self):
        
        c_cont = _get_step(self) == 1
        return dict(C_CONTIGUOUS=c_cont,
                    F_CONTIGUOUS=(c_cont and self.ndim < 2),
                    OWNDATA=(self._base is None),
                    WRITEABLE=True, # todo: fix this
                    ALIGNED=c_cont,  # todo: different from contiguous?
                    UPDATEIFCOPY=False,  # We don't support this feature
               )
    
    ## Methods - managemenet
    
    def fill(self, value):
        assert isinstance(value, (int, float))
        self[:] = value
    
    def clip(self, a_min, a_max, out=None):
        if out is None:
            out = empty(self.shape, self.dtype)
        L = self._toflatlist()
        L = [min(a_max, max(a_min, x)) for x in L]
        out[:] = L
        return out
    
    def copy(self):
        out = empty(self.shape, self.dtype)
        out[:] = self
        return out
    
    def flatten(self):
        out = empty((self.size,), self.dtype)
        out[:] = self
        return out
    
    def ravel(self):
        return self.reshape((self.size, ))
    
    def repeat(self, repeats, axis=None):
        if axis:
            raise (TypeError, "axis argument is not supported")
        out = empty((self.size * repeats,), self.dtype)
        for i in range(repeats):
            out[i*self.size:(i+1)*self.size] = self
        return out
    
    def reshape(self, newshape):
        out = self.view()
        try:
            out.shape = newshape
        except AttributeError:
            out = self.copy()
            out.shape = newshape
        return out
    
    def transpose(self):
        ndim = self.ndim
        if ndim < 2:
            return self.view()
        shape = self.shape[::-1]
        out = empty(shape, self.dtype)
        #
        if ndim == 2:
            for i in range(self.shape[0]):
                out[:, i] = self[i, :]
        elif ndim == 3:
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    out[:, j, i] = self[i, j, :]
        else:
            raise ValueError('Tinynumpy supports transpose up to ndim=3')
        return out
    
    def astype(self, dtype):
        out = empty(self.shape, dtype)
        out[:] = self
    
    def view(self, dtype=None, type=None):
        if dtype is None:
            dtype = self.dtype
        if dtype == self.dtype:
            return ndarray(self.shape, dtype, buffer=self, 
                           offset=self._offset, strides=self.strides)
        elif self.ndim == 1:
            itemsize = int(_convert_dtype(dtype, 'short')[-1])
            size = self.nbytes // itemsize
            offsetinbytes = self._offset * self.itemsize
            offset = offsetinbytes // itemsize
            return ndarray((size, ), dtype, buffer=self, offset=offset)
        else:
            raise ValueError('new type not compatible with array.')
    
    ## Methods - statistics
    def all(self, axis=None):
        if axis:
            raise (TypeError, "axis argument is not supported")
        return all(self.flat)
    
    def any(self, axis=None):
        if axis:
            raise (TypeError, "axis argument is not supported")
        return any(self.flat)
    
    def min(self, axis=None):
        if axis:
            raise (TypeError, "axis argument is not supported")
        return min(self.flat)
    
    def max(self, axis=None):
        if axis:
            raise (TypeError, "axis argument is not supported")
        return max(self.flat)
    
    def sum(self, axis=None):
        if axis:
            raise (TypeError, "axis argument is not supported")
        return sum(self.flat)
    
    def prod(self, axis=None):
        if axis:
            raise (TypeError, "axis argument is not supported")
        p = 1.0
        for i in self.flat:
            p *= float(i)
        return p
        
    def ptp(self, axis=None):
        if axis:
            raise (TypeError, "axis argument is not supported")
        mn = self.data[self._offset]
        mx = mn
        for i in self.flat:
            if i > mx:
                mx = i
            if i < mn:
                mn = i
        return mx - mn

    def mean(self, axis=None):
        if axis:
            raise (TypeError, "axis argument is not supported")
        return self.sum() / self.size
    
    def argmax(self, axis=None):
        if axis:
            raise (TypeError, "axis argument is not supported")
        r = self.data[self._offset]
        r_index = 0
        for i_index, i in enumerate(self.flat):
            if i > r:
                r = i
                r_index = i_index
        return r_index

    def argmin(self, axis=None):
        if axis:
            raise (TypeError, "axis argument is not supported")
        r = self.data[self._offset]
        r_index = 0
        for i_index, i in enumerate(self.flat):
            if i < r:
                r = i
                r_index = i_index
        return r_index
    
    def cumprod(self, axis=None, out=None):
        if axis:
            raise (TypeError, "axis argument is not supported")
        if out is None:
            out = empty((self.size,), self.dtype)
        p = 1
        L = []
        for x in self.flat:
            p *= x
            L.append(p)
        out[:] = L
        return out

    def cumsum(self, axis=None, out=None):
        if axis:
            raise (TypeError, "axis argument is not supported")
        if out is None:
            out = empty((self.size,), self.dtype)
        p = 0
        L = []
        for x in self.flat:
            p += x
            L.append(p)
        out[:] = L
        return out

    def var(self, axis=None):
        if axis:
            raise (TypeError, "axis argument is not supported")
        m = self.mean()
        acc = 0
        for x in self.flat:
            acc += abs(x - m) ** 2
        return acc / self.size

    def std(self, axis=None):
        return sqrt(self.var(axis))

    def argwhere(self, val):
        idx  = [i for i, e in enumerate(self.flat) if e == val]
        keys = [list(_key_for_index(i, self.shape)) for i in idx]
        return keys

    def tolist(self):
        shp    = list(self.shape).copy()
        jump   = self.size//shp[-1]
        n_comp = 0 #comprehension depth
        comp   = list(self._data).copy()
        while n_comp < len(self.shape)-1 :
            comp = [comp[i*shp[-1]:i*shp[-1]+shp[-1]] for i in range(jump)]
            shp.pop()
            jump = len(comp)//shp[-1]
            n_comp +=1
        return comp


class nditer:
    def __init__(self, array):
        self.array = array
        self.key = [0] * len(self.array.shape)

    def __iter__(self):
        return self

    def __len__(self):
        return _size_for_shape(self.array.shape)

    def __getitem__(self, index):
        key = _key_for_index(index, self.array.shape)
        return self.array[key]

    def __next__(self):
        if self.key is None:
            raise StopIteration
        value = self.array[tuple(self.key)]
        if not _increment_mutable_key(self.key, self.array.shape):
            self.key = None
        return value

    def next(self):
        return self.__next__()
        

######### PUT YOUR CODE HERE.......
def mainCode():
    ## ............
    pass

mainCode()

