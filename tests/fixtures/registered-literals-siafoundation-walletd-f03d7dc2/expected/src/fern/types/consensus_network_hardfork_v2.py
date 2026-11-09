

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ConsensusNetworkHardforkV2(UniversalBaseModel):
    allow_height: typing_extensions.Annotated[
        int, FieldMetadata(alias="allowHeight"), pydantic.Field(alias="allowHeight")
    ]
    require_height: typing_extensions.Annotated[
        int, FieldMetadata(alias="requireHeight"), pydantic.Field(alias="requireHeight")
    ]
    final_cut_height: typing_extensions.Annotated[
        int, FieldMetadata(alias="finalCutHeight"), pydantic.Field(alias="finalCutHeight")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
