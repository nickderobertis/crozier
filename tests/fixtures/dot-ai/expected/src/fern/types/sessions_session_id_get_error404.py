

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sessions_session_id_get_error404error import SessionsSessionIdGetError404Error
from .sessions_session_id_get_error404meta import SessionsSessionIdGetError404Meta


class SessionsSessionIdGetError404(UniversalBaseModel):
    success: bool
    error: SessionsSessionIdGetError404Error
    meta: typing.Optional[SessionsSessionIdGetError404Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
