from tabata.tasks.base.base_task import *
from typing import Dict

__all__ = [
    "PosTask",
]

class PosTask(TaskBase):
    def __init__(self, config: Dict):
        super().__init__(config)
