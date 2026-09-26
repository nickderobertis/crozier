

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_participants_filter_training_status import ListParticipantsFilterTrainingStatus


class ListParticipantsFilter(UniversalBaseModel):
    """
    Filter applications to return more specific results
    """

    updated_since: typing.Optional[str] = pydantic.Field(default=None)
    """
    Return only records that have been updated since this date and time (ISO 8601 date format).
    """

    training_status: typing.Optional[ListParticipantsFilterTrainingStatus] = pydantic.Field(default=None)
    """
    Return only records that have this training status
    """

    from_participant_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Return only records that have this from Participant ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
