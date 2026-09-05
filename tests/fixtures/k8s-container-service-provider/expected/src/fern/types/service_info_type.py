

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServiceInfoType(enum.StrEnum):
    """
    Service type
    """

    CLUSTER_IP = "ClusterIP"
    NODE_PORT = "NodePort"
    LOAD_BALANCER = "LoadBalancer"

    def visit(
        self,
        cluster_ip: typing.Callable[[], T_Result],
        node_port: typing.Callable[[], T_Result],
        load_balancer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServiceInfoType.CLUSTER_IP:
            return cluster_ip()
        if self is ServiceInfoType.NODE_PORT:
            return node_port()
        if self is ServiceInfoType.LOAD_BALANCER:
            return load_balancer()
