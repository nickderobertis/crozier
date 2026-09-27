

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformBrushBrushSurfaceArtmeshSpace(enum.StrEnum):
    MESH_LOCAL = "mesh-local"

    def visit(self, mesh_local: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformBrushBrushSurfaceArtmeshSpace.MESH_LOCAL:
            return mesh_local()
