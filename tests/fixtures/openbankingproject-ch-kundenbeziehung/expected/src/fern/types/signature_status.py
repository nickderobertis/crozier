

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .signature_status_certificate_info import SignatureStatusCertificateInfo
from .signature_status_status import SignatureStatusStatus


class SignatureStatus(UniversalBaseModel):
    signature_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="signatureId"), pydantic.Field(alias="signatureId")
    ] = None
    status: typing.Optional[SignatureStatusStatus] = None
    signed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="signedAt"), pydantic.Field(alias="signedAt")
    ] = None
    signature_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="signatureHash"),
        pydantic.Field(alias="signatureHash", description="Hash der Signatur"),
    ] = None
    """
    Hash der Signatur
    """

    certificate_info: typing_extensions.Annotated[
        typing.Optional[SignatureStatusCertificateInfo],
        FieldMetadata(alias="certificateInfo"),
        pydantic.Field(alias="certificateInfo", description="Zertifikatsinformationen"),
    ] = None
    """
    Zertifikatsinformationen
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
