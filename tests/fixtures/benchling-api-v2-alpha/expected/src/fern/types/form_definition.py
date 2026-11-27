

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .form_definition_version import FormDefinitionVersion


class FormDefinition(UniversalBaseModel):
    id: typing.Optional[str] = None
    latest_version: typing_extensions.Annotated[
        typing.Optional[FormDefinitionVersion],
        FieldMetadata(alias="latestVersion"),
        pydantic.Field(alias="latestVersion"),
    ] = None
    modified_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="modifiedAt"),
        pydantic.Field(
            alias="modifiedAt",
            description="Time when the definition was last modified. Will be updated when a new version becomes the default",
        ),
    ] = None
    """
    Time when the definition was last modified. Will be updated when a new version becomes the default
    """

    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
