

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .age_verification_response_assurance_level import AgeVerificationResponseAssuranceLevel
from .age_verification_response_attribute_value import AgeVerificationResponseAttributeValue
from .age_verification_response_privacy_compliance import AgeVerificationResponsePrivacyCompliance


class AgeVerificationResponse(UniversalBaseModel):
    verification_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="verificationId"), pydantic.Field(alias="verificationId")
    ] = None
    meets_requirement: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="meetsRequirement"),
        pydantic.Field(alias="meetsRequirement", description="Erfüllt das Mindestalter (ja/nein)"),
    ] = None
    """
    Erfüllt das Mindestalter (ja/nein)
    """

    attribute_value: typing_extensions.Annotated[
        typing.Optional[AgeVerificationResponseAttributeValue],
        FieldMetadata(alias="attributeValue"),
        pydantic.Field(alias="attributeValue", description="Attribut-only Antwort"),
    ] = None
    """
    Attribut-only Antwort
    """

    verification_method: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="verificationMethod"), pydantic.Field(alias="verificationMethod")
    ] = None
    assurance_level: typing_extensions.Annotated[
        typing.Optional[AgeVerificationResponseAssuranceLevel],
        FieldMetadata(alias="assuranceLevel"),
        pydantic.Field(alias="assuranceLevel"),
    ] = None
    timestamp: typing.Optional[dt.datetime] = None
    privacy_compliance: typing_extensions.Annotated[
        typing.Optional[AgeVerificationResponsePrivacyCompliance],
        FieldMetadata(alias="privacyCompliance"),
        pydantic.Field(alias="privacyCompliance"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
