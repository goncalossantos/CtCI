from chapter_3.stack import Stack


class TowersOfHanoi(object):
    def __init__(self, n):
        self._n = n
        self.stack = [
            Stack(),
            Stack(),
            Stack(),
        ]
        i = self._n
        while i > 0:
            self.stack[0].push(i)
            i -= 1

    def towers_of_hanoi(self, n, input_s, output_s, temp_s):

        if n > 1:
            self.towers_of_hanoi(n=n - 1, input_s=input_s, output_s=temp_s, temp_s=output_s)

        self.move(input_s, output_s)
        if n > 1:
            self.towers_of_hanoi(n=n - 1, input_s=temp_s, output_s=output_s, temp_s=input_s)

    @staticmethod
    def move(input_s, output_s):
        aux = input_s.pop()
        output_s.push(aux)

    def perform(self):

        self.towers_of_hanoi(n=self._n, input_s=self.stack[0], output_s=self.stack[1], temp_s=self.stack[2])

    def __str__(self):
        s0 = str(self.stack[0]) + "\n"
        s1 = str(self.stack[1]) + "\n"
        s2 = str(self.stack[2]) + "\n"
        return s0 + s1 + s2
