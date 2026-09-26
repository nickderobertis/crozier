

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_set_name400response_code import DocPagesSetName400ResponseCode
from .doc_pages_set_name400response_name import DocPagesSetName400ResponseName


class DocPagesSetName400Response(UniversalBaseModel):
    name: DocPagesSetName400ResponseName
    code: DocPagesSetName400ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
