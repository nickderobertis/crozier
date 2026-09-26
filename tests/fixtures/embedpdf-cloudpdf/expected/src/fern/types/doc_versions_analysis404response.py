

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_versions_analysis404response_code import DocVersionsAnalysis404ResponseCode
from .doc_versions_analysis404response_name import DocVersionsAnalysis404ResponseName


class DocVersionsAnalysis404Response(UniversalBaseModel):
    name: DocVersionsAnalysis404ResponseName
    code: DocVersionsAnalysis404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
