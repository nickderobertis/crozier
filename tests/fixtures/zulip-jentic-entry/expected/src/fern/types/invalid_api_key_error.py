

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InvalidApiKeyError(UniversalBaseModel):
    """
    ### Invalid API key

    A typical failed JSON response for when the API key is invalid.
    """

    result: typing.Any
    msg: typing.Any
    code: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
