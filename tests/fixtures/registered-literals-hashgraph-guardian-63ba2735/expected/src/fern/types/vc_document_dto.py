

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .credential_subject_dto import CredentialSubjectDto
from .proof_dto import ProofDto


class VcDocumentDto(UniversalBaseModel):
    id: str
    type: typing.List[str]
    issuer: str
    issuance_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="issuanceDate"), pydantic.Field(alias="issuanceDate")
    ]
    context: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="@context"), pydantic.Field(alias="@context")
    ]
    credential_subject: typing_extensions.Annotated[
        CredentialSubjectDto, FieldMetadata(alias="credentialSubject"), pydantic.Field(alias="credentialSubject")
    ]
    proof: ProofDto

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
