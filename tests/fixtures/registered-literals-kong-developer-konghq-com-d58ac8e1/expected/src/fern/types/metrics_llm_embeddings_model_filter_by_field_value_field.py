

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsLlmEmbeddingsModelFilterByFieldValueField(enum.StrEnum):
    """
    The field to filter.
    """

    LLM_EMBEDDINGS_MODEL = "llm_embeddings_model"

    def visit(self, llm_embeddings_model: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsLlmEmbeddingsModelFilterByFieldValueField.LLM_EMBEDDINGS_MODEL:
            return llm_embeddings_model()
