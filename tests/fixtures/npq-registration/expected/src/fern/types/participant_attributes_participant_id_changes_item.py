

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ParticipantAttributesParticipantIdChangesItem(UniversalBaseModel):
    """
    The details of an Participant ID change
    """

    from_participant_id: str = pydantic.Field()
    """
    The unique identifier of the changed from participant training record.
    """

    to_participant_id: str = pydantic.Field()
    """
    The unique identifier of the changed to participant training record.
    """

    changed_at: dt.datetime = pydantic.Field()
    """
    The date and time the Participant ID change
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
