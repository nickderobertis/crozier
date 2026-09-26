

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_flatten404response_code import DocPagesFlatten404ResponseCode
from .doc_pages_flatten404response_name import DocPagesFlatten404ResponseName


class DocPagesFlatten404Response(UniversalBaseModel):
    name: DocPagesFlatten404ResponseName
    code: DocPagesFlatten404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
