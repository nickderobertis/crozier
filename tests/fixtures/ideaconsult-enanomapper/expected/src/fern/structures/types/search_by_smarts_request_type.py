

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchBySmartsRequestType(enum.StrEnum):
    SMILES = "smiles"
    MOL = "mol"
    URL = "url"

    def visit(
        self,
        smiles: typing.Callable[[], T_Result],
        mol: typing.Callable[[], T_Result],
        url: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchBySmartsRequestType.SMILES:
            return smiles()
        if self is SearchBySmartsRequestType.MOL:
            return mol()
        if self is SearchBySmartsRequestType.URL:
            return url()
