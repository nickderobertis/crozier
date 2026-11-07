

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InferenceResult(enum.StrEnum):
    """
    Enum for the inference result type
    """

    SYMBOL_DETECTION = "symbol-detection"
    TEXT_DETECTION = "text-detection"
    GRAPH_CONSTRUCTION = "graph-construction"
    LINE_DETECTION = "line-detection"
    GRAPH_PERSISTENCE = "graph-persistence"

    def visit(
        self,
        symbol_detection: typing.Callable[[], T_Result],
        text_detection: typing.Callable[[], T_Result],
        graph_construction: typing.Callable[[], T_Result],
        line_detection: typing.Callable[[], T_Result],
        graph_persistence: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InferenceResult.SYMBOL_DETECTION:
            return symbol_detection()
        if self is InferenceResult.TEXT_DETECTION:
            return text_detection()
        if self is InferenceResult.GRAPH_CONSTRUCTION:
            return graph_construction()
        if self is InferenceResult.LINE_DETECTION:
            return line_detection()
        if self is InferenceResult.GRAPH_PERSISTENCE:
            return graph_persistence()
