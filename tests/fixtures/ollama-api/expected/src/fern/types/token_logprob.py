

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TokenLogprob(UniversalBaseModel):
    """
    Log probability information for a single token alternative
    """

    token: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text representation of the token
    """

    logprob: typing.Optional[float] = pydantic.Field(default=None)
    """
    The log probability of this token
    """

    bytes: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    The raw byte representation of the token
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
