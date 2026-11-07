

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .session_status import SessionStatus
from .third_party_service import ThirdPartyService


class ThirdPartyServiceWithSession(UniversalBaseModel):
    service: ThirdPartyService
    session: typing.Optional[SessionStatus] = pydantic.Field(default=None)
    """
    Session status if user has an active session, null otherwise
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
