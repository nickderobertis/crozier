

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_prepare400response_code import DocSignaturesPrepare400ResponseCode
from .doc_signatures_prepare400response_name import DocSignaturesPrepare400ResponseName


class DocSignaturesPrepare400Response(UniversalBaseModel):
    name: DocSignaturesPrepare400ResponseName
    code: DocSignaturesPrepare400ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
