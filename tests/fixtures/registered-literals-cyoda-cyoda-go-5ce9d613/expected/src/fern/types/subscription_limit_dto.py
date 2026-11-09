

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .subscription_limit_dto_time_interval_bound import SubscriptionLimitDtoTimeIntervalBound


class SubscriptionLimitDto(UniversalBaseModel):
    entitlement_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="entitlementId"),
        pydantic.Field(alias="entitlementId", description="Unique identifier for the entitlement"),
    ]
    """
    Unique identifier for the entitlement
    """

    cumulative: bool = pydantic.Field()
    """
    Whether the limit is cumulative
    """

    limit: int = pydantic.Field()
    """
    The limit for this entitlement
    """

    time_interval_bound: typing_extensions.Annotated[
        typing.Optional[SubscriptionLimitDtoTimeIntervalBound],
        FieldMetadata(alias="timeIntervalBound"),
        pydantic.Field(alias="timeIntervalBound", description="The time interval bound for the entitlement"),
    ] = None
    """
    The time interval bound for the entitlement
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
