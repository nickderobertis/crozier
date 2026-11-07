

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .content_update_param import ContentUpdateParam
from .single_page import SinglePage


class SinglePageRequest(UniversalBaseModel):
    """
    Single page editor payload containing the page extension and its editable content.
    """

    content: ContentUpdateParam
    page: SinglePage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
