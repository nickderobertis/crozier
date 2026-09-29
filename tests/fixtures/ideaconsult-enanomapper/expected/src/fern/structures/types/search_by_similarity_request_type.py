

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchBySimilarityRequestType(enum.StrEnum):
    SMILES = "smiles"
    MOL = "mol"
    URL = "url"

    def visit(
        self,
        smiles: typing.Callable[[], T_Result],
        mol: typing.Callable[[], T_Result],
        url: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchBySimilarityRequestType.SMILES:
            return smiles()
        if self is SearchBySimilarityRequestType.MOL:
            return mol()
        if self is SearchBySimilarityRequestType.URL:
            return url()
