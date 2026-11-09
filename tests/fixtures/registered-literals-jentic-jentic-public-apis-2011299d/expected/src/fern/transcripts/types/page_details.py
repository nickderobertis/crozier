

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PageDetails(UniversalBaseModel):
    """
    Details of the transcript page. Transcripts are sorted from newest to oldest. The previous URL always points to a page with older transcripts.
    """

    limit: int = pydantic.Field()
    """
    The number of results this page is limited to
    """

    result_count: int = pydantic.Field()
    """
    The actual number of results in the page
    """

    current_url: str = pydantic.Field()
    """
    The URL used to retrieve the current page of transcripts
    """

    prev_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL to the next page of transcripts. The previous URL always points to a page with older transcripts.
    """

    next_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL to the next page of transcripts. The next URL always points to a page with newer transcripts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
