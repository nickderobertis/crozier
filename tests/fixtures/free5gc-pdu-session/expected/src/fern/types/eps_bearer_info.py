

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EpsBearerInfo(UniversalBaseModel):
    ebi: int
    pgw_s8u_fteid: typing_extensions.Annotated[
        str, FieldMetadata(alias="pgwS8uFteid"), pydantic.Field(alias="pgwS8uFteid")
    ]
    bearer_level_qo_s: typing_extensions.Annotated[
        str, FieldMetadata(alias="bearerLevelQoS"), pydantic.Field(alias="bearerLevelQoS")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
