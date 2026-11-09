

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .compare_documents_dto import CompareDocumentsDto


class CompareDocumentsDtov2(UniversalBaseModel):
    projects: CompareDocumentsDto
    presentations: CompareDocumentsDto

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
