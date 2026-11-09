

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .policy_dto import PolicyDto
from .vc_document_dto import VcDocumentDto


class AggregatedDtoItem(UniversalBaseModel):
    did: str
    hedera_account_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="hederaAccountId"), pydantic.Field(alias="hederaAccountId")
    ]
    vc_document: typing_extensions.Annotated[
        VcDocumentDto, FieldMetadata(alias="vcDocument"), pydantic.Field(alias="vcDocument")
    ]
    policies: PolicyDto

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
