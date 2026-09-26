

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListParticipantDeclarationsFilter(UniversalBaseModel):
    """
    Refine participant declarations to return.
    """

    participant_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique id of the participant
    """

    updated_since: typing.Optional[str] = pydantic.Field(default=None)
    """
    Return only records that have been updated since this date and time (ISO 8601 date format).
    """

    cohort: typing.Optional[str] = pydantic.Field(default=None)
    """
    Return participant declarations associated to the specified cohort or cohorts. This is a comma delimited string of years.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
