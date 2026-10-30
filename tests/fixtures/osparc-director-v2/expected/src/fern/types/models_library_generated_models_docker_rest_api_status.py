

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelsLibraryGeneratedModelsDockerRestApiStatus(enum.StrEnum):
    """
    Status is one of `none`, `starting`, `healthy` or `unhealthy`

    - "none"      Indicates there is no healthcheck
    - "starting"  Starting indicates that the container is not yet ready
    - "healthy"   Healthy indicates that the container is running correctly
    - "unhealthy" Unhealthy indicates that the container has a problem
    """

    NONE = "none"
    STARTING = "starting"
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        starting: typing.Callable[[], T_Result],
        healthy: typing.Callable[[], T_Result],
        unhealthy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ModelsLibraryGeneratedModelsDockerRestApiStatus.NONE:
            return none()
        if self is ModelsLibraryGeneratedModelsDockerRestApiStatus.STARTING:
            return starting()
        if self is ModelsLibraryGeneratedModelsDockerRestApiStatus.HEALTHY:
            return healthy()
        if self is ModelsLibraryGeneratedModelsDockerRestApiStatus.UNHEALTHY:
            return unhealthy()
