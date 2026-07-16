

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Quotas(UniversalBaseModel):
    """
    Quotas state for an api key on a service group
    """

    authorized_calls_per_day: typing_extensions.Annotated[int, FieldMetadata(alias="authorizedCallsPerDay")] = (
        pydantic.Field()
    )
    """
    The number of authorized calls per day
    """

    authorized_calls_per_month: typing_extensions.Annotated[int, FieldMetadata(alias="authorizedCallsPerMonth")] = (
        pydantic.Field()
    )
    """
    The number of authorized calls per month
    """

    authorized_calls_per_sec: typing_extensions.Annotated[int, FieldMetadata(alias="authorizedCallsPerSec")] = (
        pydantic.Field()
    )
    """
    The number of authorized calls per second
    """

    current_calls_per_day: typing_extensions.Annotated[int, FieldMetadata(alias="currentCallsPerDay")] = (
        pydantic.Field()
    )
    """
    The current number of calls per day
    """

    current_calls_per_month: typing_extensions.Annotated[int, FieldMetadata(alias="currentCallsPerMonth")] = (
        pydantic.Field()
    )
    """
    The current number of calls per month
    """

    current_calls_per_sec: typing_extensions.Annotated[int, FieldMetadata(alias="currentCallsPerSec")] = (
        pydantic.Field()
    )
    """
    The current number of calls per second
    """

    remaining_calls_per_day: typing_extensions.Annotated[int, FieldMetadata(alias="remainingCallsPerDay")] = (
        pydantic.Field()
    )
    """
    The remaining number of calls per day
    """

    remaining_calls_per_month: typing_extensions.Annotated[int, FieldMetadata(alias="remainingCallsPerMonth")] = (
        pydantic.Field()
    )
    """
    The number of authorized calls per month
    """

    remaining_calls_per_sec: typing_extensions.Annotated[int, FieldMetadata(alias="remainingCallsPerSec")] = (
        pydantic.Field()
    )
    """
    The remaining number of calls per second
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
