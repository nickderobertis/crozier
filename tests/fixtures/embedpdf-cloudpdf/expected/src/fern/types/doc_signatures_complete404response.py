

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_complete404response_code import DocSignaturesComplete404ResponseCode
from .doc_signatures_complete404response_name import DocSignaturesComplete404ResponseName


class DocSignaturesComplete404Response(UniversalBaseModel):
    name: DocSignaturesComplete404ResponseName
    code: DocSignaturesComplete404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
