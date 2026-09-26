

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_abort404response_code import DocSignaturesAbort404ResponseCode
from .doc_signatures_abort404response_name import DocSignaturesAbort404ResponseName


class DocSignaturesAbort404Response(UniversalBaseModel):
    name: DocSignaturesAbort404ResponseName
    code: DocSignaturesAbort404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
