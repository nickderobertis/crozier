

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .session_grant_subject_type import SessionGrantSubjectType


class SessionGrantSubject(UniversalBaseModel):
    """
    Who the session is shared with.
    """

    subject_id: str = pydantic.Field()
    """
    ID of the subject.
    """

    subject_type: SessionGrantSubjectType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
