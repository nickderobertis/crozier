

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SkuAvailabilityValidationRequestTransferType(enum.StrEnum):
    """
    Type of the transfer.
    """

    IMPORT_TO_AZURE = "ImportToAzure"

    def visit(self, import_to_azure: typing.Callable[[], T_Result]) -> T_Result:
        if self is SkuAvailabilityValidationRequestTransferType.IMPORT_TO_AZURE:
            return import_to_azure()
