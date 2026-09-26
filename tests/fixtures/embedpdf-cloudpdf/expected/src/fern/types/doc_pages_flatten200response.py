

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_flatten200response_meta import DocPagesFlatten200ResponseMeta


class DocPagesFlatten200Response(UniversalBaseModel):
    meta: DocPagesFlatten200ResponseMeta

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
