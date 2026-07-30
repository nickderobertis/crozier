

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .meta_cursors import MetaCursors


class Meta(UniversalBaseModel):
    """
    Response metadata
    """

    cursors: typing.Optional[MetaCursors] = pydantic.Field(default=None)
    """
    Cursors to navigate to previous or next pages through the API
    """

    items_on_page: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of items returned in the data property of the response
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
