

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RollingReserveNotificationResource(UniversalBaseModel):
    account_holder_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="accountHolderId"),
        pydantic.Field(
            alias="accountHolderId",
            description="The unique identifier of the account holder whose risk settings changed.",
        ),
    ]
    """
    The unique identifier of the account holder whose risk settings changed.
    """

    balance_platform: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="balancePlatform"),
        pydantic.Field(alias="balancePlatform", description="The unique identifier of the balance platform."),
    ] = None
    """
    The unique identifier of the balance platform.
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

    rolling_reserve_percentage: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="rollingReservePercentage"),
        pydantic.Field(
            alias="rollingReservePercentage",
            description="The percentage of your user's daily sales volume that is withheld from the settlement batch as a rolling reserve.",
        ),
    ]
    """
    The percentage of your user's daily sales volume that is withheld from the settlement batch as a rolling reserve.
    """

    with_holding_period_in_days: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="withHoldingPeriodInDays"),
        pydantic.Field(
            alias="withHoldingPeriodInDays",
            description="The number of days after which we release the withheld percentage of your user's daily sales volume.",
        ),
    ]
    """
    The number of days after which we release the withheld percentage of your user's daily sales volume.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
