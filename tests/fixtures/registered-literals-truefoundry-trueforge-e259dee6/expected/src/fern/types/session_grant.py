

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_by_subject import CreatedBySubject
from .session_grant_subject import SessionGrantSubject


class SessionGrant(UniversalBaseModel):
    created_at: str = pydantic.Field()
    """
    When the session was shared with the subject (ISO-8601 UTC).
    """

    granted_by_subject: CreatedBySubject
    subject: SessionGrantSubject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
