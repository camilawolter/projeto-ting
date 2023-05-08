import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    priority_queue.enqueue({"qtd_linhas": 4})
    priority_queue.enqueue({"qtd_linhas": 8})
    priority_queue.enqueue({"qtd_linhas": 12})
    priority_queue.enqueue({"qtd_linhas": 1})

    assert len(priority_queue) == 4

    assert priority_queue.search(0)["qtd_linhas"] == 4

    priority_queue.dequeue()

    assert priority_queue.search(0)["qtd_linhas"] == 1

    assert priority_queue.search(1)["qtd_linhas"] == 8

    with pytest.raises(IndexError, match="Índice Inválido"):
        priority_queue.search(10)
