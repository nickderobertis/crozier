

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_transform_v2body import ResponseTransformV2Body
from .response_transform_v2template_engine import ResponseTransformV2TemplateEngine


class ResponseTransformV2(UniversalBaseModel):
    body: typing.Optional[ResponseTransformV2Body] = None
    template_engine: typing.Optional[ResponseTransformV2TemplateEngine] = None
    version: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
