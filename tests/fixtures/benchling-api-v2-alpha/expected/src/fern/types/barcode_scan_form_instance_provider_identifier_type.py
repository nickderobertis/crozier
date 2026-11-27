

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BarcodeScanFormInstanceProviderIdentifierType(enum.StrEnum):
    """
    How we identify the entity that we should query for. Because Benchling entities have several different ways of declaring identity, we also must allow for different ways they can be distinguished by their barcodes.
    """

    NAME_ONLY = "NAME_ONLY"
    REGISTRY_ID_ONLY = "REGISTRY_ID_ONLY"
    ANY_IDENTIFIER = "ANY_IDENTIFIER"

    def visit(
        self,
        name_only: typing.Callable[[], T_Result],
        registry_id_only: typing.Callable[[], T_Result],
        any_identifier: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BarcodeScanFormInstanceProviderIdentifierType.NAME_ONLY:
            return name_only()
        if self is BarcodeScanFormInstanceProviderIdentifierType.REGISTRY_ID_ONLY:
            return registry_id_only()
        if self is BarcodeScanFormInstanceProviderIdentifierType.ANY_IDENTIFIER:
            return any_identifier()
