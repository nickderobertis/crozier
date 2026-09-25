

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .session_source_type import SessionSourceType


class SessionSource(UniversalBaseModel):
    """
    How this session was created (e.g. a schedule run). Null for interactive sessions.
    """

    id: str = pydantic.Field()
    """
    Schedule id.
    """

    run_id: str = pydantic.Field()
    """
    Schedule run id.
    """

    type: SessionSourceType = pydantic.Field()
    """
    Session was created by a schedule run.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
