

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_set_scale404response_code import DocPagesSetScale404ResponseCode
from .doc_pages_set_scale404response_name import DocPagesSetScale404ResponseName


class DocPagesSetScale404Response(UniversalBaseModel):
    name: DocPagesSetScale404ResponseName
    code: DocPagesSetScale404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
