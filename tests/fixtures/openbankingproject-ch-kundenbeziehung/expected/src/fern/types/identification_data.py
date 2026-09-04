

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .identification_data_biometric_data import IdentificationDataBiometricData
from .identification_data_document_type import IdentificationDataDocumentType
from .identification_data_identification_method import IdentificationDataIdentificationMethod
from .identification_data_level_of_assurance import IdentificationDataLevelOfAssurance
from .identification_data_nfc_data import IdentificationDataNfcData


class IdentificationData(UniversalBaseModel):
    identification_method: typing_extensions.Annotated[
        typing.Optional[IdentificationDataIdentificationMethod],
        FieldMetadata(alias="identificationMethod"),
        pydantic.Field(alias="identificationMethod", description="Identifikationsmethode"),
    ] = None
    """
    Identifikationsmethode
    """

    document_type: typing_extensions.Annotated[
        typing.Optional[IdentificationDataDocumentType],
        FieldMetadata(alias="documentType"),
        pydantic.Field(alias="documentType", description="Dokumententyp"),
    ] = None
    """
    Dokumententyp
    """

    document_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="documentNumber"),
        pydantic.Field(alias="documentNumber", description="Dokumentennummer"),
    ] = None
    """
    Dokumentennummer
    """

    issuing_authority: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="issuingAuthority"),
        pydantic.Field(alias="issuingAuthority", description="Ausstellende Behörde"),
    ] = None
    """
    Ausstellende Behörde
    """

    issue_date: typing_extensions.Annotated[
        typing.Optional[dt.date],
        FieldMetadata(alias="issueDate"),
        pydantic.Field(alias="issueDate", description="Ausstellungsdatum"),
    ] = None
    """
    Ausstellungsdatum
    """

    expiry_date: typing_extensions.Annotated[
        typing.Optional[dt.date],
        FieldMetadata(alias="expiryDate"),
        pydantic.Field(alias="expiryDate", description="Ablaufdatum"),
    ] = None
    """
    Ablaufdatum
    """

    issuing_country: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="issuingCountry"),
        pydantic.Field(alias="issuingCountry", description="Ausstellungsland (ISO 3166-1)"),
    ] = None
    """
    Ausstellungsland (ISO 3166-1)
    """

    level_of_assurance: typing_extensions.Annotated[
        typing.Optional[IdentificationDataLevelOfAssurance],
        FieldMetadata(alias="levelOfAssurance"),
        pydantic.Field(alias="levelOfAssurance", description="Sicherheitsniveau (eIDAS-konform)"),
    ] = None
    """
    Sicherheitsniveau (eIDAS-konform)
    """

    verification_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="verificationDate"),
        pydantic.Field(alias="verificationDate", description="Verifikationsdatum"),
    ] = None
    """
    Verifikationsdatum
    """

    verification_method: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="verificationMethod"),
        pydantic.Field(alias="verificationMethod", description="Verifikationsmethode"),
    ] = None
    """
    Verifikationsmethode
    """

    document_image_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="documentImageUrl"),
        pydantic.Field(alias="documentImageUrl", description="Signierter Link zum Dokumentenscan (10min gültig)"),
    ] = None
    """
    Signierter Link zum Dokumentenscan (10min gültig)
    """

    biometric_data: typing_extensions.Annotated[
        typing.Optional[IdentificationDataBiometricData],
        FieldMetadata(alias="biometricData"),
        pydantic.Field(alias="biometricData", description="Biometrische Daten (wenn verfügbar)"),
    ] = None
    """
    Biometrische Daten (wenn verfügbar)
    """

    nfc_data: typing_extensions.Annotated[
        typing.Optional[IdentificationDataNfcData],
        FieldMetadata(alias="nfcData"),
        pydantic.Field(alias="nfcData", description="NFC-Daten von eID"),
    ] = None
    """
    NFC-Daten von eID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
