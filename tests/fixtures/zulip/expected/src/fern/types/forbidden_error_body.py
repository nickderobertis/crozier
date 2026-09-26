

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ForbiddenErrorBody(UniversalBaseModel):
    """
    An example JSON response for when no realm is registered for
    the authenticated server on the bouncer for the given `realm_uuid`:
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
