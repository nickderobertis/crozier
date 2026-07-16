

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InQueryParam(UniversalBaseModel):
    """
    JWT location in a query param
    """

    name: str = pydantic.Field()
    """
    Name of the query param
    """

    type: str = pydantic.Field()
    """
    String with value InQueryParam
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
