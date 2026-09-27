

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_artmesh_generate_preset import ModelingOperationActionArtmeshGeneratePreset
from .modeling_operation_action_artmesh_generate_quality import ModelingOperationActionArtmeshGenerateQuality
from .modeling_operation_action_artmesh_generate_topology import ModelingOperationActionArtmeshGenerateTopology


class ModelingOperationActionArtmeshGenerate(UniversalBaseModel):
    preset: ModelingOperationActionArtmeshGeneratePreset
    topology: typing.Optional[ModelingOperationActionArtmeshGenerateTopology] = None
    columns: float
    rows: float
    alpha_threshold: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="alphaThreshold"), pydantic.Field(alias="alphaThreshold")
    ] = None
    quality: typing.Optional[ModelingOperationActionArtmeshGenerateQuality] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
