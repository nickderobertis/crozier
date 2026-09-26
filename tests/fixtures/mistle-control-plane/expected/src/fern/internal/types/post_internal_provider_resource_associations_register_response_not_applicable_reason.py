

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalProviderResourceAssociationsRegisterResponseNotApplicableReason(enum.StrEnum):
    RESOURCE_KIND_NOT_ENABLED = "resource_kind_not_enabled"
    RESOURCE_REGISTRATION_NOT_SUPPORTED = "resource_registration_not_supported"

    def visit(
        self,
        resource_kind_not_enabled: typing.Callable[[], T_Result],
        resource_registration_not_supported: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is PostInternalProviderResourceAssociationsRegisterResponseNotApplicableReason.RESOURCE_KIND_NOT_ENABLED
        ):
            return resource_kind_not_enabled()
        if (
            self
            is PostInternalProviderResourceAssociationsRegisterResponseNotApplicableReason.RESOURCE_REGISTRATION_NOT_SUPPORTED
        ):
            return resource_registration_not_supported()
