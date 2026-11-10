

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .result_document_dto import ResultDocumentDto
from .result_info_dto import ResultInfoDto


class RunningResultDto(UniversalBaseModel):
    info: ResultInfoDto
    total: float
    documents: ResultDocumentDto

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
