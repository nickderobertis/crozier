

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CountriesRow(UniversalBaseModel):
    cities: int
    code: str
    count: int
    first_updated: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="firstUpdated"), pydantic.Field(alias="firstUpdated")
    ]
    last_updated: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ]
    locations: int
    name: str
    parameters: typing.List[str]
    sources: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
