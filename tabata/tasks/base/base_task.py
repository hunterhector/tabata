"""
A task base to be implemented by the sub-tasks to represent a task with scores.
"""
from abc import ABC, abstractmethod
from typing import Dict, NamedTuple, Generic, TypeVar
from forte.processors.base import PackProcessor
from forte.data import DataPack, MultiPack

__all__ = [
    "MetricBase",
    "TaskBase",
    "TabaTask"
]

class MetricBase(ABC):
    def __init__(self, config:Dict):
        super().__init__()

    @abstractmethod
    def compute_metric(self, data_pair: MultiPack) -> NamedTuple:
        raise NotImplementedError


class TaskBase(ABC):
    def __init__(self, config: Dict):
        super().__init__()
        self._processor = self.initialize_processor(config)
        self._metric = self.define_metric(config)

    @abstractmethod
    def initialize_processor(self, config) -> PackProcessor:
        raise NotImplementedError

    @abstractmethod
    def define_metric(self, config) -> MetricBase:
        raise NotImplementedError


TabaTask = TypeVar('TabaTask', bound=TaskBase)
