

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .documents_import_from202response_document import DocumentsImportFrom202ResponseDocument
from .documents_import_from202response_tag import DocumentsImportFrom202ResponseTag


class DocumentsImportFrom202Response(UniversalBaseModel):
    tag: DocumentsImportFrom202ResponseTag
    document: DocumentsImportFrom202ResponseDocument

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
