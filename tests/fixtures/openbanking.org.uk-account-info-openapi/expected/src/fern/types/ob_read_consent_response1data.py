

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .creation_date_time import CreationDateTime
from .ob_read_consent_response1data_permissions_item import ObReadConsentResponse1DataPermissionsItem
from .ob_read_consent_response1data_status import ObReadConsentResponse1DataStatus
from .status_update_date_time import StatusUpdateDateTime


class ObReadConsentResponse1Data(UniversalBaseModel):
    consent_id: typing_extensions.Annotated[str, FieldMetadata(alias="ConsentId")] = pydantic.Field()
    """
    Unique identification as assigned to identify the account access consent resource.
    """

    creation_date_time: typing_extensions.Annotated[CreationDateTime, FieldMetadata(alias="CreationDateTime")]
    expiration_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="ExpirationDateTime")
    ] = pydantic.Field(default=None)
    """
    Specified date and time the permissions will expire.
    If this is not populated, the permissions will be open ended.All dates in the JSON payloads are represented in ISO 8601 date-time format. 
    All date-time fields in responses must include the timezone. An example is below:
    2017-04-05T10:43:07+00:00
    """

    permissions: typing_extensions.Annotated[
        typing.List[ObReadConsentResponse1DataPermissionsItem], FieldMetadata(alias="Permissions")
    ]
    status: typing_extensions.Annotated[ObReadConsentResponse1DataStatus, FieldMetadata(alias="Status")] = (
        pydantic.Field()
    )
    """
    Specifies the status of consent resource in code form.
    """

    status_update_date_time: typing_extensions.Annotated[
        StatusUpdateDateTime, FieldMetadata(alias="StatusUpdateDateTime")
    ]
    transaction_from_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="TransactionFromDateTime")
    ] = pydantic.Field(default=None)
    """
    Specified start date and time for the transaction query period.
    If this is not populated, the start date will be open ended, and data will be returned from the earliest available transaction.All dates in the JSON payloads are represented in ISO 8601 date-time format. 
    All date-time fields in responses must include the timezone. An example is below:
    2017-04-05T10:43:07+00:00
    """

    transaction_to_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="TransactionToDateTime")
    ] = pydantic.Field(default=None)
    """
    Specified end date and time for the transaction query period.
    If this is not populated, the end date will be open ended, and data will be returned to the latest available transaction.All dates in the JSON payloads are represented in ISO 8601 date-time format. 
    All date-time fields in responses must include the timezone. An example is below:
    2017-04-05T10:43:07+00:00
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
