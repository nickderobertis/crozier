

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .texture import Texture


class User(UniversalBaseModel):
    username: str
    uuid_: typing_extensions.Annotated[str, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]
    assets: typing.Optional[typing.Dict[str, Texture]] = pydantic.Field(default=None)
    """
    Map of texture type (e.g. "SKIN", "CAPE") to Texture.
    """

    properties: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
