

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1ListSettlementsRequest(UniversalBaseModel):
    """ """

    batch_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor to retrieve the next set of results for your
    original query to the endpoint.
    """

    begin_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    The beginning of the requested reporting period, in ISO 8601 format. If this value is before January 1, 2013 (2013-01-01T00:00:00Z), this endpoint returns an error. Default value: The current time minus one year.
    """

    end_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    The end of the requested reporting period, in ISO 8601 format. If this value is more than one year greater than begin_time, this endpoint returns an error. Default value: The current time.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of settlements to return in a single response. This value cannot exceed 200.
    """

    order: typing.Optional[str] = pydantic.Field(default=None)
    """
    The order in which settlements are listed in the response.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Provide this parameter to retrieve only settlements with a particular status (SENT or FAILED).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
