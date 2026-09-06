

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_custom_code_blocks_scripts_response_blocks_item import ListCustomCodeBlocksScriptsResponseBlocksItem
from .list_custom_code_blocks_scripts_response_pagination import ListCustomCodeBlocksScriptsResponsePagination


class ListCustomCodeBlocksScriptsResponse(UniversalBaseModel):
    """
    Custom Code Blocks corresponding to where scripts were applied
    """

    blocks: typing.Optional[typing.List[ListCustomCodeBlocksScriptsResponseBlocksItem]] = None
    pagination: typing.Optional[ListCustomCodeBlocksScriptsResponsePagination] = pydantic.Field(default=None)
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
