

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_transform_v1template_engine import ResponseTransformV1TemplateEngine


class ResponseTransformV1(UniversalBaseModel):
    body: typing.Optional[str] = None
    template_engine: typing.Optional[ResponseTransformV1TemplateEngine] = None
    version: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
