

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .amount import Amount
from .resource_reference import ResourceReference


class ReleaseBlockedBalanceNotificationData(UniversalBaseModel):
    account_holder: typing_extensions.Annotated[
        ResourceReference,
        FieldMetadata(alias="accountHolder"),
        pydantic.Field(
            alias="accountHolder",
            description="Contains information about the account holder associated with the `balanceAccount`.",
        ),
    ]
    """
    Contains information about the account holder associated with the `balanceAccount`.
    """

    amount: Amount = pydantic.Field()
    """
    The amount released.
    """

    balance_account: typing_extensions.Annotated[
        ResourceReference,
        FieldMetadata(alias="balanceAccount"),
        pydantic.Field(
            alias="balanceAccount", description="Contains information about the associated balance account."
        ),
    ]
    """
    Contains information about the associated balance account.
    """

    balance_platform: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="balancePlatform"),
        pydantic.Field(alias="balancePlatform", description="The unique identifier of the balance platform."),
    ] = None
    """
    The unique identifier of the balance platform.
    """

    batch_reference: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="batchReference"),
        pydantic.Field(alias="batchReference", description="The reference of the batch that was released."),
    ] = None
    """
    The reference of the batch that was released.
    """

    blocked_balance_after: typing_extensions.Annotated[
        typing.Optional[Amount],
        FieldMetadata(alias="blockedBalanceAfter"),
        pydantic.Field(
            alias="blockedBalanceAfter", description="The new blocked balance after the funds were released."
        ),
    ] = None
    """
    The new blocked balance after the funds were released.
    """

    blocked_balance_before: typing_extensions.Annotated[
        typing.Optional[Amount],
        FieldMetadata(alias="blockedBalanceBefore"),
        pydantic.Field(alias="blockedBalanceBefore", description="The blocked balance before the funds were released."),
    ] = None
    """
    The blocked balance before the funds were released.
    """

    creation_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="creationDate"),
        pydantic.Field(
            alias="creationDate",
            description="The date and time when the event was triggered, in ISO 8601 extended format. For example, **2025-03-19T10:15:30+01:00**.",
        ),
    ] = None
    """
    The date and time when the event was triggered, in ISO 8601 extended format. For example, **2025-03-19T10:15:30+01:00**.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the resource.
    """

    value_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="valueDate"),
        pydantic.Field(
            alias="valueDate",
            description="The date and time when the amount was released, in ISO 8601 extended format. For example, **2025-03-19T10:15:30+01:00**.",
        ),
    ] = None
    """
    The date and time when the amount was released, in ISO 8601 extended format. For example, **2025-03-19T10:15:30+01:00**.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
