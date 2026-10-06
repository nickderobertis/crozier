

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TimeZone(UniversalBaseModel):
    id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ID"), pydantic.Field(alias="ID")] = None
    raw_offset: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="rawOffset"), pydantic.Field(alias="rawOffset")
    ] = None
    i_d: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="iD"), pydantic.Field(alias="iD")] = None
    display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ] = None
    d_st_savings: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="dSTSavings"), pydantic.Field(alias="dSTSavings")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
