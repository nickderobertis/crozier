

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_artmesh_rebuild_preset import ModelingOperationActionArtmeshRebuildPreset
from .modeling_operation_action_artmesh_rebuild_quality import ModelingOperationActionArtmeshRebuildQuality
from .modeling_operation_action_artmesh_rebuild_topology import ModelingOperationActionArtmeshRebuildTopology


class ModelingOperationActionArtmeshRebuild(UniversalBaseModel):
    preset: ModelingOperationActionArtmeshRebuildPreset
    topology: typing.Optional[ModelingOperationActionArtmeshRebuildTopology] = None
    columns: float
    rows: float
    alpha_threshold: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="alphaThreshold"), pydantic.Field(alias="alphaThreshold")
    ] = None
    quality: typing.Optional[ModelingOperationActionArtmeshRebuildQuality] = None
    preserve_bindings: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="preserveBindings"), pydantic.Field(alias="preserveBindings")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
