

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FileListQuery(UniversalBaseModel):
    """
    Query schema for listing files.
    """

    limit: typing.Optional[int] = None
    page_token: typing.Optional[str] = None
    order: typing.Optional[str] = None
    order_by: typing.Optional[str] = None
    content_type: typing.Optional[str] = None
    filename_search: typing.Optional[str] = pydantic.Field(default=None)
    """
    Case-insensitive partial match search on filename (e.g., 'doc' matches 'my_document.pdf')
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
