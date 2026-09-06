

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_scripts_response_pagination import ListScriptsResponsePagination
from .list_scripts_response_registered_scripts_item import ListScriptsResponseRegisteredScriptsItem


class ListScriptsResponse(UniversalBaseModel):
    """
    A list of scripts registered to the site
    """

    registered_scripts: typing_extensions.Annotated[
        typing.Optional[typing.List[ListScriptsResponseRegisteredScriptsItem]],
        FieldMetadata(alias="registeredScripts"),
        pydantic.Field(alias="registeredScripts"),
    ] = None
    pagination: typing.Optional[ListScriptsResponsePagination] = pydantic.Field(default=None)
    """
    Pagination object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
