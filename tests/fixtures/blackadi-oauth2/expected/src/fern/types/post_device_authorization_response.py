

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostDeviceAuthorizationResponse(UniversalBaseModel):
    device_code: str
    user_code: str
    verification_uri: str
    verification_uri_complete: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional, per §3.3.1
    """

    expires_in: int
    interval: typing.Optional[int] = pydantic.Field(default=None)
    """
    Omitted when deviceFlowPollingInterval is 0
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
