

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_flatten400response_code import DocPagesFlatten400ResponseCode
from .doc_pages_flatten400response_name import DocPagesFlatten400ResponseName


class DocPagesFlatten400Response(UniversalBaseModel):
    name: DocPagesFlatten400ResponseName
    code: DocPagesFlatten400ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
