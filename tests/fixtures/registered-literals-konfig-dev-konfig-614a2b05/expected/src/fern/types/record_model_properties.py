

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .record_model_properties_agreement_date import RecordModelPropertiesAgreementDate
from .record_model_properties_counterparty_email import RecordModelPropertiesCounterpartyEmail
from .record_model_properties_counterparty_name import RecordModelPropertiesCounterpartyName
from .record_model_properties_hourly_rate import RecordModelPropertiesHourlyRate


class RecordModelProperties(UniversalBaseModel):
    agreement_date: typing_extensions.Annotated[
        typing.Optional[RecordModelPropertiesAgreementDate],
        FieldMetadata(alias="agreementDate"),
        pydantic.Field(alias="agreementDate"),
    ] = None
    counterparty_name: typing_extensions.Annotated[
        typing.Optional[RecordModelPropertiesCounterpartyName],
        FieldMetadata(alias="counterpartyName"),
        pydantic.Field(alias="counterpartyName"),
    ] = None
    counterparty_email: typing_extensions.Annotated[
        typing.Optional[RecordModelPropertiesCounterpartyEmail],
        FieldMetadata(alias="counterpartyEmail"),
        pydantic.Field(alias="counterpartyEmail"),
    ] = None
    hourly_rate: typing_extensions.Annotated[
        typing.Optional[RecordModelPropertiesHourlyRate],
        FieldMetadata(alias="hourlyRate"),
        pydantic.Field(alias="hourlyRate"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
