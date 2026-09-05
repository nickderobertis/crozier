

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContainerPortVisibility(enum.StrEnum):
    """
    How this port is exposed to consumers.
    - none: Port is not exposed outside the container process
    - internal: Exposed to the host or cluster network
      (e.g., Docker -p, Kubernetes ClusterIP Service)
    - external: Reachable from outside the host/cluster
      (e.g., OpenShift Route, Kubernetes Ingress/LoadBalancer)
    """

    NONE = "none"
    INTERNAL = "internal"
    EXTERNAL = "external"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        internal: typing.Callable[[], T_Result],
        external: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContainerPortVisibility.NONE:
            return none()
        if self is ContainerPortVisibility.INTERNAL:
            return internal()
        if self is ContainerPortVisibility.EXTERNAL:
            return external()
