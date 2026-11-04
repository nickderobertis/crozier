

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TokenPagination(UniversalBaseModel):
    limit: int = pydantic.Field()
    """
    Page size used for this response.
    """

    next_page_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Opaque token for the next page. Omit or absent when there is no next page.
    """

    previous_page_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Opaque token for the previous page. Omit or absent when there is no previous page.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
