

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .documents_commit200response_document import DocumentsCommit200ResponseDocument


class DocumentsCommit200Response(UniversalBaseModel):
    document: DocumentsCommit200ResponseDocument

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
