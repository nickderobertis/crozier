

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_viewports404response_code import DocPagesViewports404ResponseCode
from .doc_pages_viewports404response_name import DocPagesViewports404ResponseName


class DocPagesViewports404Response(UniversalBaseModel):
    name: DocPagesViewports404ResponseName
    code: DocPagesViewports404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
