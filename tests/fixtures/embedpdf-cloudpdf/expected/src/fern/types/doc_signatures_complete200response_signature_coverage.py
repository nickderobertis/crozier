

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocSignaturesComplete200ResponseSignatureCoverage(enum.StrEnum):
    WHOLE_REVISION = "whole-revision"
    PARTIAL = "partial"
    MALFORMED = "malformed"

    def visit(
        self,
        whole_revision: typing.Callable[[], T_Result],
        partial: typing.Callable[[], T_Result],
        malformed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocSignaturesComplete200ResponseSignatureCoverage.WHOLE_REVISION:
            return whole_revision()
        if self is DocSignaturesComplete200ResponseSignatureCoverage.PARTIAL:
            return partial()
        if self is DocSignaturesComplete200ResponseSignatureCoverage.MALFORMED:
            return malformed()
