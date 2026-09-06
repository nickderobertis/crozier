

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_item import AppItem
from .config_item import ConfigItem


class SearchResponseBody(UniversalBaseModel):
    schema_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="$schema"),
        pydantic.Field(alias="$schema", description="A URL to the JSON Schema for this object."),
    ] = None
    """
    A URL to the JSON Schema for this object.
    """

    configs: typing.Optional[typing.List[ConfigItem]] = None
    games: typing.Optional[typing.List[AppItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
