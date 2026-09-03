

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .identification_status_response_assurance_level import IdentificationStatusResponseAssuranceLevel
from .identification_status_response_status import IdentificationStatusResponseStatus


class IdentificationStatusResponse(UniversalBaseModel):
    verification_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="verificationId"), pydantic.Field(alias="verificationId")
    ] = None
    status: typing.Optional[IdentificationStatusResponseStatus] = None
    verification_method: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="verificationMethod"), pydantic.Field(alias="verificationMethod")
    ] = None
    document_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="documentType"), pydantic.Field(alias="documentType")
    ] = None
    assurance_level: typing_extensions.Annotated[
        typing.Optional[IdentificationStatusResponseAssuranceLevel],
        FieldMetadata(alias="assuranceLevel"),
        pydantic.Field(alias="assuranceLevel"),
    ] = None
    issued_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="issuedAt"), pydantic.Field(alias="issuedAt")
    ] = None
    valid_until: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="validUntil"), pydantic.Field(alias="validUntil")
    ] = None
    can_be_reused: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="canBeReused"), pydantic.Field(alias="canBeReused")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
