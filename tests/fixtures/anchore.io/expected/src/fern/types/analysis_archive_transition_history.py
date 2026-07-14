

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .analysis_archive_transition_history_transition import AnalysisArchiveTransitionHistoryTransition


class AnalysisArchiveTransitionHistory(UniversalBaseModel):
    """
    A rule for auto-archiving image analysis by time and/or tag-history
    """

    created_at: typing.Optional[dt.datetime] = None
    image_digest: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="imageDigest")] = None
    last_updated: typing.Optional[dt.datetime] = None
    rule_id: typing.Optional[str] = None
    transition: typing.Optional[AnalysisArchiveTransitionHistoryTransition] = None
    transition_task_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The task that created & updated this entry
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
