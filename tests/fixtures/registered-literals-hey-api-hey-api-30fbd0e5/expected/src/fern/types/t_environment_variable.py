

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TEnvironmentVariable(UniversalBaseModel):
    """
    An environment variable
    """

    key: str = pydantic.Field()
    """
    Name or key of the environment variable, accessible via Deno.env or process.env
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional description of the environment variable
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
