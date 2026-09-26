

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_analysis400response_code import DocSignaturesAnalysis400ResponseCode
from .doc_signatures_analysis400response_name import DocSignaturesAnalysis400ResponseName


class DocSignaturesAnalysis400Response(UniversalBaseModel):
    name: DocSignaturesAnalysis400ResponseName
    code: DocSignaturesAnalysis400ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
