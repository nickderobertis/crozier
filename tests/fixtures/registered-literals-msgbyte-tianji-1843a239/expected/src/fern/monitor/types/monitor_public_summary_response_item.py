

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class MonitorPublicSummaryResponseItem(UniversalBaseModel):
    day: str
    total_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="totalCount"), pydantic.Field(alias="totalCount")
    ]
    up_count: typing_extensions.Annotated[float, FieldMetadata(alias="upCount"), pydantic.Field(alias="upCount")]
    up_rate: typing_extensions.Annotated[float, FieldMetadata(alias="upRate"), pydantic.Field(alias="upRate")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
