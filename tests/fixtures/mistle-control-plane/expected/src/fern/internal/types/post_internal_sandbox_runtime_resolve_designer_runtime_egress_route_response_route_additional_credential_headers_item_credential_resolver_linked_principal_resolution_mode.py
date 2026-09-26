

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteAdditionalCredentialHeadersItemCredentialResolverLinkedPrincipalResolutionMode(
    enum.StrEnum
):
    REQUIRED = "required"
    PREFERRED = "preferred"

    def visit(self, required: typing.Callable[[], T_Result], preferred: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteAdditionalCredentialHeadersItemCredentialResolverLinkedPrincipalResolutionMode.REQUIRED
        ):
            return required()
        if (
            self
            is PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteAdditionalCredentialHeadersItemCredentialResolverLinkedPrincipalResolutionMode.PREFERRED
        ):
            return preferred()
