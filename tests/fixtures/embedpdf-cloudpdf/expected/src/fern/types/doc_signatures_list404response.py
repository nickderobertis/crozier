

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_list404response_code import DocSignaturesList404ResponseCode
from .doc_signatures_list404response_name import DocSignaturesList404ResponseName


class DocSignaturesList404Response(UniversalBaseModel):
    name: DocSignaturesList404ResponseName
    code: DocSignaturesList404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
