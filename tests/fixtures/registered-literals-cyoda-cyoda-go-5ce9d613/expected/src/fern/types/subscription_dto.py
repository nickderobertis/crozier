

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .subscription_limit_dto import SubscriptionLimitDto


class SubscriptionDto(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the subscription
    """

    legal_entity_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="legalEntityId"),
        pydantic.Field(alias="legalEntityId", description="Identifier for the associated legal entity"),
    ]
    """
    Identifier for the associated legal entity
    """

    status: str = pydantic.Field()
    """
    Current status of the subscription
    """

    tier_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="tierName"),
        pydantic.Field(alias="tierName", description="Name of the subscription tier"),
    ]
    """
    Name of the subscription tier
    """

    period_from: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="periodFrom"),
        pydantic.Field(alias="periodFrom", description="Start period of the subscription"),
    ]
    """
    Start period of the subscription
    """

    limits: typing.List[SubscriptionLimitDto]
    period_to: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="periodTo"),
        pydantic.Field(alias="periodTo", description="End period of the subscription"),
    ] = None
    """
    End period of the subscription
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
