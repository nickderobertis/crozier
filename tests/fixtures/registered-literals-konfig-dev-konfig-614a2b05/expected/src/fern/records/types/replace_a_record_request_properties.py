

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .replace_a_record_request_properties_agreement_date import ReplaceARecordRequestPropertiesAgreementDate
from .replace_a_record_request_properties_counterparty_name import ReplaceARecordRequestPropertiesCounterpartyName


class ReplaceARecordRequestProperties(UniversalBaseModel):
    """
    Object containing key/value pairs of metadata attached to the record. The key you specify must have a value with a supported type as outlined in the Supported Property Types section.
    """

    agreement_date: typing_extensions.Annotated[
        typing.Optional[ReplaceARecordRequestPropertiesAgreementDate],
        FieldMetadata(alias="agreementDate"),
        pydantic.Field(alias="agreementDate", description="The date of the agreement."),
    ] = None
    """
    The date of the agreement.
    """

    counterparty_name: typing_extensions.Annotated[
        typing.Optional[ReplaceARecordRequestPropertiesCounterpartyName],
        FieldMetadata(alias="counterpartyName"),
        pydantic.Field(alias="counterpartyName", description="The name of the counterparty."),
    ] = None
    """
    The name of the counterparty.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
