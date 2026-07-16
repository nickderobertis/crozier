

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_id import AccountId
from .debtor_reference import DebtorReference
from .ob_active_or_historic_currency_and_amount1 import ObActiveOrHistoricCurrencyAndAmount1
from .ob_external_schedule_type1code import ObExternalScheduleType1Code
from .reference import Reference
from .scheduled_payment_date_time import ScheduledPaymentDateTime
from .scheduled_payment_id import ScheduledPaymentId


class ObScheduledPayment3Basic(UniversalBaseModel):
    account_id: typing_extensions.Annotated[AccountId, FieldMetadata(alias="AccountId")]
    debtor_reference: typing_extensions.Annotated[
        typing.Optional[DebtorReference], FieldMetadata(alias="DebtorReference")
    ] = None
    instructed_amount: typing_extensions.Annotated[
        ObActiveOrHistoricCurrencyAndAmount1, FieldMetadata(alias="InstructedAmount")
    ]
    reference: typing_extensions.Annotated[typing.Optional[Reference], FieldMetadata(alias="Reference")] = None
    scheduled_payment_date_time: typing_extensions.Annotated[
        ScheduledPaymentDateTime, FieldMetadata(alias="ScheduledPaymentDateTime")
    ]
    scheduled_payment_id: typing_extensions.Annotated[
        typing.Optional[ScheduledPaymentId], FieldMetadata(alias="ScheduledPaymentId")
    ] = None
    scheduled_type: typing_extensions.Annotated[ObExternalScheduleType1Code, FieldMetadata(alias="ScheduledType")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
