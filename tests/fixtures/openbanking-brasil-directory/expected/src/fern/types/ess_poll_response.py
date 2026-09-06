

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .external_signing_service_envelope_id import ExternalSigningServiceEnvelopeId
from .external_signing_service_envelope_status import ExternalSigningServiceEnvelopeStatus
from .organisation_id import OrganisationId


class EssPollResponse(UniversalBaseModel):
    ess_envelope_id: typing_extensions.Annotated[
        typing.Optional[ExternalSigningServiceEnvelopeId],
        FieldMetadata(alias="EssEnvelopeId"),
        pydantic.Field(alias="EssEnvelopeId"),
    ] = None
    external_signing_service_envelope_status: typing_extensions.Annotated[
        typing.Optional[ExternalSigningServiceEnvelopeStatus],
        FieldMetadata(alias="ExternalSigningServiceEnvelopeStatus"),
        pydantic.Field(alias="ExternalSigningServiceEnvelopeStatus"),
    ] = None
    organisation_id: typing_extensions.Annotated[
        typing.Optional[OrganisationId], FieldMetadata(alias="OrganisationId"), pydantic.Field(alias="OrganisationId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
