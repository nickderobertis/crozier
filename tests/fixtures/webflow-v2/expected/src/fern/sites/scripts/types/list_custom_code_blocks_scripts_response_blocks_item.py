

import datetime as dt
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .list_custom_code_blocks_scripts_response_blocks_item_scripts_item import (
    ListCustomCodeBlocksScriptsResponseBlocksItemScriptsItem,
)
from .list_custom_code_blocks_scripts_response_blocks_item_type import ListCustomCodeBlocksScriptsResponseBlocksItemType


class ListCustomCodeBlocksScriptsResponseBlocksItem(UniversalBaseModel):
    """
    A specific instance of Custom Code applied to a Site or Page
    """

    site_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="siteId"),
        pydantic.Field(alias="siteId", description="The Site ID where the custom code was applied"),
    ] = None
    """
    The Site ID where the custom code was applied
    """

    page_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pageId"),
        pydantic.Field(alias="pageId", description="The Page ID (if applied at Page-level)"),
    ] = None
    """
    The Page ID (if applied at Page-level)
    """

    type: typing.Optional[ListCustomCodeBlocksScriptsResponseBlocksItemType] = pydantic.Field(default=None)
    """
    Whether the Custom Code script is applied at the Site-level or Page-level
    """

    scripts: typing.Optional[typing.List[ListCustomCodeBlocksScriptsResponseBlocksItemScriptsItem]] = pydantic.Field(
        default=None
    )
    """
    A list of scripts applied to a Site or a Page
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="The date the Block was created"),
    ] = None
    """
    The date the Block was created
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="The date the Block was most recently updated"),
    ] = None
    """
    The date the Block was most recently updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
