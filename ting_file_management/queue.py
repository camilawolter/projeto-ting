from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._list = list()

    def __len__(self):
        return len(self._list)

    def enqueue(self, value):
        self._list.append(value)

    def dequeue(self):
        if len(self._list) == 0:
            return None
        return self._list.pop(0)

    def search(self, index):
        if not 0 <= index < len(self._list):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._list[index]
