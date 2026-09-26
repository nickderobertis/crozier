

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_analysis404response_code import DocSignaturesAnalysis404ResponseCode
from .doc_signatures_analysis404response_name import DocSignaturesAnalysis404ResponseName


class DocSignaturesAnalysis404Response(UniversalBaseModel):
    name: DocSignaturesAnalysis404ResponseName
    code: DocSignaturesAnalysis404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
