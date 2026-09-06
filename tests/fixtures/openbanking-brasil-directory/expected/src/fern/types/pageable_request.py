

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PageableRequest(UniversalBaseModel):
    page: typing.Optional[int] = pydantic.Field(default=None)
    """
    Page index starts from 0
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    This sets the page size
    """

    sort: typing.Optional[str] = pydantic.Field(default=None)
    """
    Used to sort based on Model Parameters
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
