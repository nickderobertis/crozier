

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .upsert_custom_code_scripts_response_scripts_item_location import (
    UpsertCustomCodeScriptsResponseScriptsItemLocation,
)


class UpsertCustomCodeScriptsResponseScriptsItem(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    ID of the registered custom code script
    """

    location: UpsertCustomCodeScriptsResponseScriptsItemLocation = pydantic.Field()
    """
    Location of the script, either in the header or footer of the published site
    """

    version: str = pydantic.Field()
    """
    Semantic Version String for the registered script *e.g. 0.0.1*
    """

    attributes: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Developer-specified key/value pairs to be applied as attributes to the script
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
