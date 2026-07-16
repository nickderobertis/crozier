

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BreakType(UniversalBaseModel):
    """
    A defined break template that sets an expectation for possible `Break`
    instances on a `Shift`.
    """

    break_name: str = pydantic.Field()
    """
    A human-readable name for this type of break. The name is displayed to
    employees in Square products.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A read-only timestamp in RFC 3339 format.
    """

    expected_duration: str = pydantic.Field()
    """
    Format: RFC-3339 P[n]Y[n]M[n]DT[n]H[n]M[n]S. The expected length of
    this break. Precision less than minutes is truncated.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The UUID for this object.
    """

    is_paid: bool = pydantic.Field()
    """
    Whether this break counts towards time worked for compensation
    purposes.
    """

    location_id: str = pydantic.Field()
    """
    The ID of the business location this type of break applies to.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A read-only timestamp in RFC 3339 format.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Used for resolving concurrency issues. The request fails if the version
    provided does not match the server version at the time of the request. If a value is not
    provided, Square's servers execute a "blind" write; potentially
    overwriting another writer's data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
