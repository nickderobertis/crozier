

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Break(UniversalBaseModel):
    """
    A record of an employee's break during a shift.
    """

    break_type_id: str = pydantic.Field()
    """
    The `BreakType` that this `Break` was templated on.
    """

    end_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    RFC 3339; follows the same timezone information as `Shift`. Precision up to
    the minute is respected; seconds are truncated.
    """

    expected_duration: str = pydantic.Field()
    """
    Format: RFC-3339 P[n]Y[n]M[n]DT[n]H[n]M[n]S. The expected length of
    the break.
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

    name: str = pydantic.Field()
    """
    A human-readable name.
    """

    start_at: str = pydantic.Field()
    """
    RFC 3339; follows the same timezone information as `Shift`. Precision up to
    the minute is respected; seconds are truncated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
