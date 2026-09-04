

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SignatureResponse(UniversalBaseModel):
    signature_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="signatureId"), pydantic.Field(alias="signatureId")
    ] = None
    signature_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="signatureUrl"),
        pydantic.Field(alias="signatureUrl", description="URL für Signatur-Interface"),
    ] = None
    """
    URL für Signatur-Interface
    """

    qr_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="qrCode"),
        pydantic.Field(alias="qrCode", description="QR-Code für mobile Signatur"),
    ] = None
    """
    QR-Code für mobile Signatur
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
