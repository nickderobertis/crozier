

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .content_template_request_kind import ContentTemplateRequestKind


class ContentTemplateRequest(UniversalBaseModel):
    name: str
    kind: ContentTemplateRequestKind
    body: str
    placeholders: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
