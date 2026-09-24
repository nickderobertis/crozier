

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .logout_response_response import LogoutResponseResponse
from .logout_response_status import LogoutResponseStatus


class LogoutResponse(UniversalBaseModel):
    api: str = pydantic.Field()
    """
    The path of the REST API method
    """

    method: str = pydantic.Field()
    """
    The name of the REST API method
    """

    response: LogoutResponseResponse
    status: LogoutResponseStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
