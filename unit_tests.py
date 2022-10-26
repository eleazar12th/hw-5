import pytest
from stack_functional import create_stack, push, pop
from stack_oop import Stack


class TestStackFunctional:
    st = create_stack()

    def test_create_stack(self):
        assert len(self.st) == 0

    def test_push(self):
        push(self.st, 42)
        assert len(self.st) == 1
        assert self.st[0] == 42

    def test_pop(self):
        assert pop(self.st) == 42
        assert len(self.st) == 0


class TestStackOop:
    st = Stack()

    def test_stack_init(self):
        assert len(self.st.a) == 0

    def test_stack_push(self):
        self.st.push(42)
        assert len(self.st.a) == 1
        assert self.st.a[0] == 42

    def test_stack_pop(self):
        assert self.st.pop() == 42
        assert len(self.st.a) == 0
