

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MeSubscription(UniversalBaseModel):
    cancel_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="cancelAt"),
        pydantic.Field(alias="cancelAt", description="Scheduled cancellation timestamp"),
    ] = None
    """
    Scheduled cancellation timestamp
    """

    cancel_at_period_end: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="cancelAtPeriodEnd"),
        pydantic.Field(alias="cancelAtPeriodEnd", description="Whether cancellation is scheduled"),
    ] = None
    """
    Whether cancellation is scheduled
    """

    id: str = pydantic.Field()
    """
    Subscription ID
    """

    period_end: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="periodEnd"),
        pydantic.Field(alias="periodEnd", description="Current billing period end"),
    ] = None
    """
    Current billing period end
    """

    period_start: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="periodStart"),
        pydantic.Field(alias="periodStart", description="Current billing period start"),
    ] = None
    """
    Current billing period start
    """

    plan: str = pydantic.Field()
    """
    Subscription plan
    """

    provider: str = pydantic.Field()
    """
    Billing provider
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Subscription status
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
