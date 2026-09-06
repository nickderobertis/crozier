

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .get_custom_code_scripts_response_scripts_item import GetCustomCodeScriptsResponseScriptsItem


class GetCustomCodeScriptsResponse(UniversalBaseModel):
    scripts: typing.Optional[typing.List[GetCustomCodeScriptsResponseScriptsItem]] = pydantic.Field(default=None)
    """
    A list of scripts applied to a Site or a Page
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="Date when the Site's scripts were last updated"),
    ] = None
    """
    Date when the Site's scripts were last updated
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="Date when the Site's scripts were created"),
    ] = None
    """
    Date when the Site's scripts were created
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
