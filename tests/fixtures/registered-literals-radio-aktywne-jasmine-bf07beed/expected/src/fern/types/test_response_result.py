

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TestResponseResult(UniversalBaseModel):
    """
    Result of the test.
    """

    success: bool = pydantic.Field()
    """
    Indicates if the test was successful.
    """

    message: str = pydantic.Field()
    """
    Message returned from the test.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
