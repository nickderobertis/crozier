

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VectorSimilarity(enum.StrEnum):
    """
    Similarity measure for comparing vector embeddings.
    """

    COSINE = "Cosine"
    DOT = "Dot"
    EUCLIDEAN = "Euclidean"

    def visit(
        self,
        cosine: typing.Callable[[], T_Result],
        dot: typing.Callable[[], T_Result],
        euclidean: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VectorSimilarity.COSINE:
            return cosine()
        if self is VectorSimilarity.DOT:
            return dot()
        if self is VectorSimilarity.EUCLIDEAN:
            return euclidean()
