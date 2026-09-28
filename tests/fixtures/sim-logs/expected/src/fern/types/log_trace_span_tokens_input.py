

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LogTraceSpanTokensInput(UniversalBaseModel):
    total: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total tokens.
    """

    input: typing.Optional[float] = pydantic.Field(default=None)
    """
    Input tokens.
    """

    output: typing.Optional[float] = pydantic.Field(default=None)
    """
    Output tokens.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
