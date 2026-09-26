

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_prepare409response_code import DocSignaturesPrepare409ResponseCode
from .doc_signatures_prepare409response_name import DocSignaturesPrepare409ResponseName


class DocSignaturesPrepare409Response(UniversalBaseModel):
    name: DocSignaturesPrepare409ResponseName
    code: DocSignaturesPrepare409ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
