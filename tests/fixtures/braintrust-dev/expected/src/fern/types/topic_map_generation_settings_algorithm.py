

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TopicMapGenerationSettingsAlgorithm(enum.StrEnum):
    HDBSCAN = "hdbscan"
    KMEANS = "kmeans"

    def visit(self, hdbscan: typing.Callable[[], T_Result], kmeans: typing.Callable[[], T_Result]) -> T_Result:
        if self is TopicMapGenerationSettingsAlgorithm.HDBSCAN:
            return hdbscan()
        if self is TopicMapGenerationSettingsAlgorithm.KMEANS:
            return kmeans()
