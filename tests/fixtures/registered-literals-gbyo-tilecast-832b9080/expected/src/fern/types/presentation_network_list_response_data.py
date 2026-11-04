

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .presentation_network import PresentationNetwork
from .presentation_network_list_response_data_supported_security_item import (
    PresentationNetworkListResponseDataSupportedSecurityItem,
)


class PresentationNetworkListResponseData(UniversalBaseModel):
    items: typing.List[PresentationNetwork]
    credentials_available: typing_extensions.Annotated[
        bool, FieldMetadata(alias="credentialsAvailable"), pydantic.Field(alias="credentialsAvailable")
    ]
    credentials_unavailable_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="credentialsUnavailableReason"), pydantic.Field(alias="credentialsUnavailableReason")
    ]
    supported_security: typing_extensions.Annotated[
        typing.List[PresentationNetworkListResponseDataSupportedSecurityItem],
        FieldMetadata(alias="supportedSecurity"),
        pydantic.Field(alias="supportedSecurity"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
