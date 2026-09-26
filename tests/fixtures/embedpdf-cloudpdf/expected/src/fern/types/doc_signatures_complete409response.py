

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_complete409response_code import DocSignaturesComplete409ResponseCode
from .doc_signatures_complete409response_name import DocSignaturesComplete409ResponseName


class DocSignaturesComplete409Response(UniversalBaseModel):
    name: DocSignaturesComplete409ResponseName
    code: DocSignaturesComplete409ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
