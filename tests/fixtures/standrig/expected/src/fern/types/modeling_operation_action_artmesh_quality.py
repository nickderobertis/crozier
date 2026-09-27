

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modeling_operation_action_artmesh_quality_quality import ModelingOperationActionArtmeshQualityQuality


class ModelingOperationActionArtmeshQuality(UniversalBaseModel):
    quality: ModelingOperationActionArtmeshQualityQuality
    merge: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
