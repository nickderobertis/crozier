

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocManifest200ResponseScopesActions(enum.StrEnum):
    BASE = "base"
    LAYER = "layer"

    def visit(self, base: typing.Callable[[], T_Result], layer: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocManifest200ResponseScopesActions.BASE:
            return base()
        if self is DocManifest200ResponseScopesActions.LAYER:
            return layer()
