

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TicSearchResult(UniversalBaseModel):
    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Descriptive label for the TIC, when available
    """

    name: str = pydantic.Field()
    """
    Human-readable label for the matched TIC
    """

    tic: str = pydantic.Field()
    """
    Matched Taxability Information Code (TIC)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
