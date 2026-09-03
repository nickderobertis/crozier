

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .document_data_document_type import DocumentDataDocumentType


class DocumentData(UniversalBaseModel):
    document_type: typing_extensions.Annotated[
        typing.Optional[DocumentDataDocumentType],
        FieldMetadata(alias="documentType"),
        pydantic.Field(alias="documentType"),
    ] = None
    document_image: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="documentImage"),
        pydantic.Field(alias="documentImage", description="Base64-kodiertes Dokumentenbild"),
    ] = None
    """
    Base64-kodiertes Dokumentenbild
    """

    nfc_data: typing_extensions.Annotated[
        typing.Optional[str],
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
