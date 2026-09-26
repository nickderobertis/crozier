

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListApplicationsFilter(UniversalBaseModel):
    """
    Filter applications to return more specific results
    """

    cohort: typing.Optional[str] = pydantic.Field(default=None)
    """
    Return only NPQ applications from the specified cohort or cohorts. This is a comma delimited string of years.
    """

    updated_since: typing.Optional[str] = pydantic.Field(default=None)
    """
    Return only records that have been updated since this date and time (ISO 8601 date format).
    """

    participant_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Return only NPQ applications from the specified participant or participants. This is comma delimited string of participant IDs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
