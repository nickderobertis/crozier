

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_complete400response_code import DocSignaturesComplete400ResponseCode
from .doc_signatures_complete400response_name import DocSignaturesComplete400ResponseName


class DocSignaturesComplete400Response(UniversalBaseModel):
    name: DocSignaturesComplete400ResponseName
    code: DocSignaturesComplete400ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
