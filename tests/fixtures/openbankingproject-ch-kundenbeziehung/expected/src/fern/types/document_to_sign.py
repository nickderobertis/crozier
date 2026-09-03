

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DocumentToSign(UniversalBaseModel):
    document_id: typing_extensions.Annotated[str, FieldMetadata(alias="documentId"), pydantic.Field(alias="documentId")]
    document_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="documentName"), pydantic.Field(alias="documentName")
    ]
    document_hash: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="documentHash"),
        pydantic.Field(alias="documentHash", description="SHA-256 Hash des Dokuments"),
    ]
    """
    SHA-256 Hash des Dokuments
    """

    document_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="documentUrl"), pydantic.Field(alias="documentUrl")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
