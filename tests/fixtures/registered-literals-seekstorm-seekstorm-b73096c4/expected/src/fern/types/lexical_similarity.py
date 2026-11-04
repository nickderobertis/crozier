

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LexicalSimilarity(enum.StrEnum):
    """
    Similarity type defines the scoring and ranking of the search results:
    - Bm25f: considers documents composed from several fields, with different field lengths and importance
    - Bm25fProximity: considers term proximity, e.g. for implicit phrase search with improved relevancy
    """

    BM25F = "Bm25f"
    BM25F_PROXIMITY = "Bm25fProximity"

    def visit(self, bm25f: typing.Callable[[], T_Result], bm25f_proximity: typing.Callable[[], T_Result]) -> T_Result:
        if self is LexicalSimilarity.BM25F:
            return bm25f()
        if self is LexicalSimilarity.BM25F_PROXIMITY:
            return bm25f_proximity()
