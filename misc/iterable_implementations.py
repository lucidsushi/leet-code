// JAVASCRIPT 1
function makeIterator(n){
  nextIndex = 0;
  return {'next': function(){
    return nextIndex < n.length ?
      {'value': n[nextIndex++], 'done': false} :
      {'done': true};
    }
  };
}

iter = makeIterator([1,2]);

console.log(iter.next())
console.log(iter.next())
console.log(iter.next())


// JAVASCRIPT 2
let array = [1, 2];
let makeIterable = {};
makeIterable[Symbol.iterator] = function* (){
  yield* array
};

for (let item of makeIterable){
  console.log(item);
}


// JAVASCRIPT 3
function* gen(array){
  // yield expects an iterable
  yield* array;
}

iterator = gen([1,2]);

// console.log(iterator.next());
// console.log(iterator.next());
// console.log(iterator.next());

for(let item of iterator){
  console.log(item);
}


# PYTHON 1
def make_iterator(array):
  next_index = [0]

  def next():
    index_value, = next_index
    if index_value < len(array):
      next_index[0] += 1
      return array[index_value]
    else:
      raise StopIteration

  return next

iterator = make_iterator([1,2])

print iterator()
print iterator()
print iterator()


# PYTHON 2
class MakeIterator(object):
  def __init__(self, array):
      self.array = array
      self.next_index = 0

  def __iter__(self):
      return self

  def next(self):
    if self.next_index < len(self.array):
      next_value = self.array[self.next_index]
      self.next_index += 1
      return next_value
    else:
      raise StopIteration

iterator = MakeIterator([1,2])

print iterator.next()
print iterator.next()
print iterator.next()

# __iter__ allows actual iteration
# for item in iterator:
#   print item

