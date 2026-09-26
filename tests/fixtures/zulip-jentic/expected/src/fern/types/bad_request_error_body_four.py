

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BadRequestErrorBodyFour(UniversalBaseModel):
    """
    An example JSON error response for when the user doesn't have permission
    to subscribe other users to channels and `stream_ids` is not empty.
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
