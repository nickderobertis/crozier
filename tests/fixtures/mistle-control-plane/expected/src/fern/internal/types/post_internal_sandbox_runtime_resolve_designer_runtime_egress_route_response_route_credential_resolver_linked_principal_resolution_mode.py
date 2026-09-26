

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolverLinkedPrincipalResolutionMode(
    enum.StrEnum
):
    REQUIRED = "required"
    PREFERRED = "preferred"

    def visit(self, required: typing.Callable[[], T_Result], preferred: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolverLinkedPrincipalResolutionMode.REQUIRED
        ):
            return required()
        if (
            self
            is PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRouteCredentialResolverLinkedPrincipalResolutionMode.PREFERRED
        ):
            return preferred()
