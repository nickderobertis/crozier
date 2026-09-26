

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_insert_blank400response_code import DocPagesInsertBlank400ResponseCode
from .doc_pages_insert_blank400response_name import DocPagesInsertBlank400ResponseName


class DocPagesInsertBlank400Response(UniversalBaseModel):
    name: DocPagesInsertBlank400ResponseName
    code: DocPagesInsertBlank400ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
