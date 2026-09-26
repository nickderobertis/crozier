

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .documents_import_from200response_document import DocumentsImportFrom200ResponseDocument
from .documents_import_from200response_tag import DocumentsImportFrom200ResponseTag


class DocumentsImportFrom200Response(UniversalBaseModel):
    tag: DocumentsImportFrom200ResponseTag
    document: DocumentsImportFrom200ResponseDocument

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
