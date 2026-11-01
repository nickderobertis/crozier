

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateInProgressType(enum.StrEnum):
    """
    Operation in progress. `certificate_renewal` is reported while a
    scheduled or forced certificate-renewal cycle holds the lock, and
    also after a failed cycle whose lock is retained until an operator
    clears it. Clients that switch exhaustively over this value must
    handle it.
    """

    ETCD_ENCRYPTION = "etcd_encryption"
    ETCD_KEY_ROTATION = "etcd_key_rotation"
    K8S_UPGRADE = "k8s_upgrade"
    CP_NODES_RECYCLING = "cp_nodes_recycling"
    OIDC_ENABLE = "oidc_enable"
    SPIRE_SERVER_UPDATE = "spire_server_update"
    CERTIFICATE_RENEWAL = "certificate_renewal"

    def visit(
        self,
        etcd_encryption: typing.Callable[[], T_Result],
        etcd_key_rotation: typing.Callable[[], T_Result],
        k8s_upgrade: typing.Callable[[], T_Result],
        cp_nodes_recycling: typing.Callable[[], T_Result],
        oidc_enable: typing.Callable[[], T_Result],
        spire_server_update: typing.Callable[[], T_Result],
        certificate_renewal: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateInProgressType.ETCD_ENCRYPTION:
            return etcd_encryption()
        if self is UpdateInProgressType.ETCD_KEY_ROTATION:
            return etcd_key_rotation()
        if self is UpdateInProgressType.K8S_UPGRADE:
            return k8s_upgrade()
        if self is UpdateInProgressType.CP_NODES_RECYCLING:
            return cp_nodes_recycling()
        if self is UpdateInProgressType.OIDC_ENABLE:
            return oidc_enable()
        if self is UpdateInProgressType.SPIRE_SERVER_UPDATE:
            return spire_server_update()
        if self is UpdateInProgressType.CERTIFICATE_RENEWAL:
            return certificate_renewal()
