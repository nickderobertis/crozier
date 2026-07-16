

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .customer_segment import CustomerSegment
from .error import Error


class RetrieveCustomerSegmentResponse(UniversalBaseModel):
    """
    Defines the fields that are included in the response body for requests to the `RetrieveCustomerSegment` endpoint.

    Either `errors` or `segment` is present in a given response (never both).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    segment: typing.Optional[CustomerSegment] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
