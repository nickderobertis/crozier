

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .records_update_metadata_request_add_properties_agreement_date import (
    RecordsUpdateMetadataRequestAddPropertiesAgreementDate,
)
from .records_update_metadata_request_add_properties_counterparty_name import (
    RecordsUpdateMetadataRequestAddPropertiesCounterpartyName,
)


class RecordsUpdateMetadataRequestAddProperties(UniversalBaseModel):
    """
    A key:value map of properties to add. The two below are examples.
    """

    counterparty_name: typing_extensions.Annotated[
        typing.Optional[RecordsUpdateMetadataRequestAddPropertiesCounterpartyName],
        FieldMetadata(alias="counterpartyName"),
        pydantic.Field(alias="counterpartyName"),
    ] = None
    agreement_date: typing_extensions.Annotated[
        typing.Optional[RecordsUpdateMetadataRequestAddPropertiesAgreementDate],
        FieldMetadata(alias="agreementDate"),
        pydantic.Field(alias="agreementDate"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
