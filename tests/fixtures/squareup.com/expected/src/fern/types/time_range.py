

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TimeRange(UniversalBaseModel):
    """
    Represents a generic time range. The start and end values are
    represented in RFC 3339 format. Time ranges are customized to be
    inclusive or exclusive based on the needs of a particular endpoint.
    Refer to the relevant endpoint-specific documentation to determine
    how time ranges are handled.
    """

    end_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A datetime value in RFC 3339 format indicating when the time range
    ends.
    """

    start_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A datetime value in RFC 3339 format indicating when the time range
    starts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
