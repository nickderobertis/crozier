

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .consent_response_status import ConsentResponseStatus


class ConsentResponse(UniversalBaseModel):
    consent_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="consentId"),
        pydantic.Field(alias="consentId", description="Eindeutige Consent-ID"),
    ] = None
    """
    Eindeutige Consent-ID
    """

    status: typing.Optional[ConsentResponseStatus] = None
    consent_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="consentUrl"),
        pydantic.Field(alias="consentUrl", description="URL für Kunden-Consent-Interface"),
    ] = None
    """
    URL für Kunden-Consent-Interface
    """

    qr_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="qrCode"),
        pydantic.Field(alias="qrCode", description="Base64-kodierter QR-Code für mobilen Consent"),
    ] = None
    """
    Base64-kodierter QR-Code für mobilen Consent
    """

    expiry_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="expiryDate"), pydantic.Field(alias="expiryDate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
