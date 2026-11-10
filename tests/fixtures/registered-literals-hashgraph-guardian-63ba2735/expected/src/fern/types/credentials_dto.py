

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .did_document_dto import DidDocumentDto
from .did_key_dto import DidKeyDto
from .subject_dto import SubjectDto


class CredentialsDto(UniversalBaseModel):
    entity: str
    hedera_account_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="hederaAccountId"), pydantic.Field(alias="hederaAccountId")
    ]
    hedera_account_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="hederaAccountKey"), pydantic.Field(alias="hederaAccountKey")
    ]
    parent: typing.Optional[str] = None
    vc_document: typing_extensions.Annotated[
        typing.Optional[SubjectDto], FieldMetadata(alias="vcDocument"), pydantic.Field(alias="vcDocument")
    ] = None
    did_document: typing_extensions.Annotated[
        typing.Optional[DidDocumentDto], FieldMetadata(alias="didDocument"), pydantic.Field(alias="didDocument")
    ] = None
    did_keys: typing_extensions.Annotated[
        typing.Optional[typing.List[DidKeyDto]], FieldMetadata(alias="didKeys"), pydantic.Field(alias="didKeys")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
