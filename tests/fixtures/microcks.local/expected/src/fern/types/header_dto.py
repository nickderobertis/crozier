

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class HeaderDto(UniversalBaseModel):
    """
    Data Transfert Object for headers of both Requests and Responses
    """

    name: str = pydantic.Field()
    """
    Unique distinct name of this Header
    """

    values: str = pydantic.Field()
    """
    Values for this header (comma separated strings)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
