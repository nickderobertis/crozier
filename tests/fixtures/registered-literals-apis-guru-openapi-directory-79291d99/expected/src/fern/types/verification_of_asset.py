

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .reporting_information import ReportingInformation
from .service_product_fulfillment import ServiceProductFulfillment
from .verification_of_asset_response import VerificationOfAssetResponse


class VerificationOfAsset(UniversalBaseModel):
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    reporting_information: typing_extensions.Annotated[
        ReportingInformation,
        FieldMetadata(alias="REPORTING_INFORMATION"),
        pydantic.Field(alias="REPORTING_INFORMATION"),
    ]
    service_product_fulfillment: typing_extensions.Annotated[
        ServiceProductFulfillment,
        FieldMetadata(alias="SERVICE_PRODUCT_FULFILLMENT"),
        pydantic.Field(alias="SERVICE_PRODUCT_FULFILLMENT"),
    ]
    verification_of_asset_response: typing_extensions.Annotated[
        VerificationOfAssetResponse,
        FieldMetadata(alias="VERIFICATION_OF_ASSET_RESPONSE"),
        pydantic.Field(alias="VERIFICATION_OF_ASSET_RESPONSE"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
