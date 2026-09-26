

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_insert404response_code import DocPagesInsert404ResponseCode
from .doc_pages_insert404response_name import DocPagesInsert404ResponseName


class DocPagesInsert404Response(UniversalBaseModel):
    name: DocPagesInsert404ResponseName
    code: DocPagesInsert404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
