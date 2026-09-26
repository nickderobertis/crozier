

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_move404response_code import DocPagesMove404ResponseCode
from .doc_pages_move404response_name import DocPagesMove404ResponseName


class DocPagesMove404Response(UniversalBaseModel):
    name: DocPagesMove404ResponseName
    code: DocPagesMove404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
