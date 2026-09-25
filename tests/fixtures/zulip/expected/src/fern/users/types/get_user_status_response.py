

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_user_status_response_status import GetUserStatusResponseStatus


class GetUserStatusResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    status: typing.Optional[GetUserStatusResponseStatus] = pydantic.Field(default=None)
    """
    The status set by the user. Note that, if the user doesn't have a status
    currently set, then the returned dictionary will be empty as none of the
    keys listed below will be present.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
