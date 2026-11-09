

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PageSegment(UniversalBaseModel):
    """
    A search match located on a page of a paginated document, such as a PDF.
    """

    page: int = pydantic.Field()
    """
    The 1-based page number the match occurred on.
    """

    highlight: typing.List[str] = pydantic.Field()
    """
    Matched text fragments from this page, using the same marking convention as `searchExtra.highlight`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
