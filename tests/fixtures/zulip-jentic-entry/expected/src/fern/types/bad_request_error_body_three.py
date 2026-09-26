

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BadRequestErrorBodyThree(UniversalBaseModel):
    """
    An example JSON error response for when any of the specified channels
    does not exist or the user does not have permission to access one of
    the targeted channels.
    """

    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    code: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
