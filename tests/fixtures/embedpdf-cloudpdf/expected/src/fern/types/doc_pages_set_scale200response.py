

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_set_scale200response_meta import DocPagesSetScale200ResponseMeta
from .doc_pages_set_scale200response_page import DocPagesSetScale200ResponsePage


class DocPagesSetScale200Response(UniversalBaseModel):
    page: DocPagesSetScale200ResponsePage
    meta: DocPagesSetScale200ResponseMeta

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
