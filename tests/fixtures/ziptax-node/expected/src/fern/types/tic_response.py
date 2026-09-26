

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tic_entry import TicEntry


class TicResponse(UniversalBaseModel):
    tic_list: typing.Optional[typing.List[TicEntry]] = pydantic.Field(default=None)
    """
    Full list of Taxability Information Codes (TICs) available to the account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
