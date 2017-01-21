from unittest import TestCase

from data_structures.graphs.base import Graph

from chapter_4.project_dependencies import handle_dependencies


class TestHandleDependencies(TestCase):
    def test_handle_dependencies(self):
        mapping = {
            "a": 0,
        }
        g = Graph(6)
        g.add_edge(3, 0)
        g.add_edge(1, 5)
        g.add_edge(3, 1)
        g.add_edge(0, 5)
        g.add_edge(2, 3)
        assert handle_dependencies(g) == [4, 5, 0, 1, 3, 2]
