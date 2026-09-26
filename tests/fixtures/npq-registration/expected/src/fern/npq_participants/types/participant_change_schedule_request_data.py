

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_change_schedule_request_data_attributes import ParticipantChangeScheduleRequestDataAttributes


class ParticipantChangeScheduleRequestData(UniversalBaseModel):
    """
    An NPQ participant change schedule request data
    """

    type: str = pydantic.Field()
    """
    The data typed
    """

    attributes: ParticipantChangeScheduleRequestDataAttributes = pydantic.Field()
    """
    An NPQ participant change schedule request attributes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
