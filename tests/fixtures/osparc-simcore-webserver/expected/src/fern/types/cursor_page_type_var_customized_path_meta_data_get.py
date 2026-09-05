

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .path_meta_data_get import PathMetaDataGet


class CursorPageTypeVarCustomizedPathMetaDataGet(UniversalBaseModel):
    items: typing.List[PathMetaDataGet]
    total: typing.Optional[int] = None
    current_page: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cursor to refetch the current page
    """

    current_page_backwards: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cursor to refetch the current page starting from the last item
    """

    previous_page: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cursor for the previous page
    """

    next_page: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cursor for the next page
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
