

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TerminalRefundQuerySort(UniversalBaseModel):
    """ """

    sort_order: typing.Optional[str] = pydantic.Field(default=None)
    """
    The order in which results are listed.
    - `ASC` - Oldest to newest.
    - `DESC` - Newest to oldest (default).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
