from collections import deque
from typing import List, Set

from data_structures.graphs.base import Graph, Edge


def check_dependencies(dependencies: List[Edge], finished_projects: Set) -> bool:
    """ Checks if all the dependencies for a project are in finished projects

    :param dependencies: Dependencies of a project
    :param finished_projects: set with all the finished projects so far
    :return: returns True if all are satisfied, False if they aren't
    """
    return all((d.destination in finished_projects for d in dependencies))


def handle_dependencies(projects_graph: Graph) -> List[int]:
    """ Returns a possible order to perform the projects based on their dependencies.

    :param projects_graph:
    :return: Returns the order in which to perform the projects
    """
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
