

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_api_bridge_read_request_get_deformer_structure_data import PostApiBridgeReadRequestGetDeformerStructureData


class PostApiBridgeReadRequestGetDeformerStructure(UniversalBaseModel):
    data: PostApiBridgeReadRequestGetDeformerStructureData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
