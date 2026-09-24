

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V60ResponseInfo(UniversalBaseModel):
    code: int = pydantic.Field()
    """
    Numeric status code (100 = success)
    """

    definition: str = pydantic.Field()
    """
    URL to the response schema
    """

    message: str = pydantic.Field()
    """
    Human-readable summary
    """

    name: str = pydantic.Field()
    """
    Symbolic status name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
