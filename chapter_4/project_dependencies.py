from collections import deque
from typing import List

from data_structures.graphs.base import Graph


def check_dependencies(dependencies, finished_projects):
    return all((d.destination in finished_projects for d in dependencies))


def handle_dependencies(projects_graph: Graph) -> List[int]:
    project_queue = deque(range(projects_graph.v))
    no_advance = 0

    finished_projects = set()
    order = list()

    while project_queue and no_advance < len(project_queue):
        p = project_queue.popleft()
        if check_dependencies(projects_graph.graph[p], finished_projects):
            finished_projects.add(p)
            order.append(p)
            no_advance = 0
        else:
            project_queue.append(p)
            no_advance += 1
    return order
