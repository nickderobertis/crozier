

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EvidanceData(UniversalBaseModel):
    first_seen: typing_extensions.Annotated[float, FieldMetadata(alias="firstSeen"), pydantic.Field(alias="firstSeen")]
    id: str
    last_seen: typing_extensions.Annotated[float, FieldMetadata(alias="lastSeen"), pydantic.Field(alias="lastSeen")]
    last_updated: typing_extensions.Annotated[
        float, FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
