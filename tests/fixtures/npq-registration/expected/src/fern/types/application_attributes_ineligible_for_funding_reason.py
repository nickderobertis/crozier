

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApplicationAttributesIneligibleForFundingReason(enum.StrEnum):
    """
    Indicates why this NPQ participant is not eligible for DfE funding
    """

    PREVIOUSLY_FUNDED = "previously-funded"
    ESTABLISHMENT_INELIGIBLE = "establishment-ineligible"

    def visit(
        self, previously_funded: typing.Callable[[], T_Result], establishment_ineligible: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ApplicationAttributesIneligibleForFundingReason.PREVIOUSLY_FUNDED:
            return previously_funded()
        if self is ApplicationAttributesIneligibleForFundingReason.ESTABLISHMENT_INELIGIBLE:
            return establishment_ineligible()
