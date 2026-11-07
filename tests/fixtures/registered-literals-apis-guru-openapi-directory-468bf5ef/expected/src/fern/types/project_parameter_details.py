

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ProjectParameterDetails(UniversalBaseModel):
    average: float
    count: int
    display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ] = None
    first_updated: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="firstUpdated"), pydantic.Field(alias="firstUpdated")
    ]
    last_updated: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ]
    last_value: typing_extensions.Annotated[float, FieldMetadata(alias="lastValue"), pydantic.Field(alias="lastValue")]
    locations: int
    parameter: str
    parameter_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="parameterId"), pydantic.Field(alias="parameterId")
    ]
    unit: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
