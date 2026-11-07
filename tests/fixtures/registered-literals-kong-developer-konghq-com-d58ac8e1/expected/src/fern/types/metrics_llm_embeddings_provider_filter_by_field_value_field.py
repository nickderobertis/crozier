

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsLlmEmbeddingsProviderFilterByFieldValueField(enum.StrEnum):
    """
    The field to filter.
    """

    LLM_EMBEDDINGS_PROVIDER = "llm_embeddings_provider"

    def visit(self, llm_embeddings_provider: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsLlmEmbeddingsProviderFilterByFieldValueField.LLM_EMBEDDINGS_PROVIDER:
            return llm_embeddings_provider()
