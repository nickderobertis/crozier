

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_insert400response_code import DocPagesInsert400ResponseCode
from .doc_pages_insert400response_name import DocPagesInsert400ResponseName


class DocPagesInsert400Response(UniversalBaseModel):
    name: DocPagesInsert400ResponseName
    code: DocPagesInsert400ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
