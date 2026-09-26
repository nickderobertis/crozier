

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sessions_get_error500error import SessionsGetError500Error
from .sessions_get_error500meta import SessionsGetError500Meta


class SessionsGetError500(UniversalBaseModel):
    success: bool
    error: SessionsGetError500Error
    meta: typing.Optional[SessionsGetError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
