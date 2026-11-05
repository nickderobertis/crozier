

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState(enum.StrEnum):
    """
    `succeeded` is accepted only for a Tilecast Edge release: it is the screen's explicit confirmation that the provisional release passed its health checks, and the only way an Edge target settles. Other families settle from the heartbeat.
    """

    DOWNLOADING = "downloading"
    DOWNLOADED = "downloaded"
    VERIFYING = "verifying"
    READY = "ready"
    WAITING_FOR_PERMISSION = "waiting_for_permission"
    WAITING_FOR_USER = "waiting_for_user"
    INSTALLING = "installing"
    RECONNECTING = "reconnecting"
    FAILED = "failed"
    SUCCEEDED = "succeeded"

    def visit(
        self,
        downloading: typing.Callable[[], T_Result],
        downloaded: typing.Callable[[], T_Result],
        verifying: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        waiting_for_permission: typing.Callable[[], T_Result],
        waiting_for_user: typing.Callable[[], T_Result],
        installing: typing.Callable[[], T_Result],
        reconnecting: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState.DOWNLOADING:
            return downloading()
        if self is PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState.DOWNLOADED:
            return downloaded()
        if self is PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState.VERIFYING:
            return verifying()
        if self is PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState.READY:
            return ready()
        if self is PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState.WAITING_FOR_PERMISSION:
            return waiting_for_permission()
        if self is PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState.WAITING_FOR_USER:
            return waiting_for_user()
        if self is PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState.INSTALLING:
            return installing()
        if self is PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState.RECONNECTING:
            return reconnecting()
        if self is PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState.FAILED:
            return failed()
        if self is PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState.SUCCEEDED:
            return succeeded()
