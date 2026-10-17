

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .session_form_grant import SessionFormGrant


class SessionForm(UniversalBaseModel):
    grant: typing.Optional[SessionFormGrant] = None
    skipper_id: typing.Optional[str] = None
    pin: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
