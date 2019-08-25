"""
The main Tabata runner.
"""
from tabata.tasks.base.base_task import *
from typing import List, Iterable
from tabata.tasks import *
from forte.multipack_pipeline import MultiPackPipeline


class Tabata:
    def __init__(self):
        self.task_pool: List[TabaTask] = []
        self.pipeline = MultiPackPipeline

    def add_task(self, task: TabaTask):
        self.task_pool.append(task)

    def compute(self, references: Iterable[str], predictions: Iterable[str]):
        pass


def main():
    tabata = Tabata()
    tabata.add_task(PosTask())

    references = ['this', 'that']
    predictions = ['this', 'that']

    tabata.compute(references, predictions)
