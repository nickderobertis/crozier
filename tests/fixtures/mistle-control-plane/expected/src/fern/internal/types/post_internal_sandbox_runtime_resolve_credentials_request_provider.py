

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeResolveCredentialsRequestProvider(enum.StrEnum):
    DOCKER = "docker"
    E2B = "e2b"
    FREESTYLE = "freestyle"
    MODAL = "modal"
    OPENCOMPUTER = "opencomputer"
    TENSORLAKE = "tensorlake"

    def visit(
        self,
        docker: typing.Callable[[], T_Result],
        e2b: typing.Callable[[], T_Result],
        freestyle: typing.Callable[[], T_Result],
        modal: typing.Callable[[], T_Result],
        opencomputer: typing.Callable[[], T_Result],
        tensorlake: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostInternalSandboxRuntimeResolveCredentialsRequestProvider.DOCKER:
            return docker()
        if self is PostInternalSandboxRuntimeResolveCredentialsRequestProvider.E2B:
            return e2b()
        if self is PostInternalSandboxRuntimeResolveCredentialsRequestProvider.FREESTYLE:
            return freestyle()
        if self is PostInternalSandboxRuntimeResolveCredentialsRequestProvider.MODAL:
            return modal()
        if self is PostInternalSandboxRuntimeResolveCredentialsRequestProvider.OPENCOMPUTER:
            return opencomputer()
        if self is PostInternalSandboxRuntimeResolveCredentialsRequestProvider.TENSORLAKE:
            return tensorlake()
