

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sessions_session_id_get_error500error import SessionsSessionIdGetError500Error
from .sessions_session_id_get_error500meta import SessionsSessionIdGetError500Meta


class SessionsSessionIdGetError500(UniversalBaseModel):
    success: bool
    error: SessionsSessionIdGetError500Error
    meta: typing.Optional[SessionsSessionIdGetError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
