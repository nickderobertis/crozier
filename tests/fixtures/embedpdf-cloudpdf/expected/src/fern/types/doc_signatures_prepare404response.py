

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_prepare404response_code import DocSignaturesPrepare404ResponseCode
from .doc_signatures_prepare404response_name import DocSignaturesPrepare404ResponseName


class DocSignaturesPrepare404Response(UniversalBaseModel):
    name: DocSignaturesPrepare404ResponseName
    code: DocSignaturesPrepare404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
