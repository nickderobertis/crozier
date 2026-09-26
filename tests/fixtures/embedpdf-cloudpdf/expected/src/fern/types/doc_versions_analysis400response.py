

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_versions_analysis400response_code import DocVersionsAnalysis400ResponseCode
from .doc_versions_analysis400response_name import DocVersionsAnalysis400ResponseName


class DocVersionsAnalysis400Response(UniversalBaseModel):
    name: DocVersionsAnalysis400ResponseName
    code: DocVersionsAnalysis400ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
