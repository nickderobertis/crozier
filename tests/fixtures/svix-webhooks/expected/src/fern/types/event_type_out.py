

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EventTypeOut(UniversalBaseModel):
    archived: typing.Optional[bool] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    deprecated: bool
    description: str
    feature_flag: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="featureFlag"), pydantic.Field(alias="featureFlag")
    ] = None
    name: str
    schemas: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = pydantic.Field(
        default=None
    )
    """
    The schema for the event type for a specific version as a JSON schema.
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
