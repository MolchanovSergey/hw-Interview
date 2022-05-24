BAL_DICT = {
    '(': ')',
    '[': ']',
    '{': '}'
}

class Stack(list):

    def isEmpty(self):
        return len(self) == 0

    def push(self, item):
        self.append(item)

    def pop(self):
        if not self.isEmpty():
            _item = self[-1]
            self.__delitem__(-1)
        return _item


    def peek(self):
        if not self.isEmpty():
            return self[-1]

    def size(self):
        return len(self)


def check_ballance(my_str):
    stack = Stack()
    for item_ in my_str:
        if item_ in BAL_DICT:
            stack.push(item_)
        elif item_ == BAL_DICT.get(stack.peek()):
            stack.pop()
        else:
            return 'Несбалансированно'
    if stack.isEmpty():
        return 'Сбалансированно'


if __name__ == '__main__':
    for seq in input('Введите последовательность скобок:').split():
        print(f'{seq:<10}{check_ballance(seq)}')