

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_by_subject import CreatedBySubject
from .session_agent import SessionAgent
from .session_metadata import SessionMetadata
from .session_metrics import SessionMetrics


class Session(UniversalBaseModel):
    agent: SessionAgent
    created_at: str = pydantic.Field()
    """
    ISO 8601 creation timestamp.
    """

    created_by_subject: CreatedBySubject
    id: str = pydantic.Field()
    """
    Unique session id.
    """

    metadata: SessionMetadata
    metrics: SessionMetrics
    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional human-readable title; null until set.
    """

    updated_at: str = pydantic.Field()
    """
    ISO 8601 last-update timestamp.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
