

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .external_signing_service_envelope_id import ExternalSigningServiceEnvelopeId
from .external_signing_service_envelope_status import ExternalSigningServiceEnvelopeStatus
from .terms_and_conditions_item import TermsAndConditionsItem


class TermsAndConditionsDetail(UniversalBaseModel):
    """
    TnC details Parent
    """

    external_signing_service_envelope_id: typing_extensions.Annotated[
        typing.Optional[ExternalSigningServiceEnvelopeId],
        FieldMetadata(alias="ExternalSigningServiceEnvelopeId"),
        pydantic.Field(alias="ExternalSigningServiceEnvelopeId"),
    ] = None
    external_signing_service_envelope_passcode: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ExternalSigningServiceEnvelopePasscode"),
        pydantic.Field(
            alias="ExternalSigningServiceEnvelopePasscode",
            description="Access code for the specifier to fill in the signer details. This will be populated only once, when signing is initiated",
        ),
    ] = None
    """
    Access code for the specifier to fill in the signer details. This will be populated only once, when signing is initiated
    """

    external_signing_service_envelope_status: typing_extensions.Annotated[
        typing.Optional[ExternalSigningServiceEnvelopeStatus],
        FieldMetadata(alias="ExternalSigningServiceEnvelopeStatus"),
        pydantic.Field(alias="ExternalSigningServiceEnvelopeStatus"),
    ] = None
    inititated_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="InititatedDate"),
        pydantic.Field(alias="InititatedDate", description="Terms and Conditions initiated date"),
    ] = None
    """
    Terms and Conditions initiated date
    """

    terms_and_conditions_item: typing_extensions.Annotated[
        typing.Optional[TermsAndConditionsItem],
        FieldMetadata(alias="TermsAndConditionsItem"),
        pydantic.Field(alias="TermsAndConditionsItem"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
