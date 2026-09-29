

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .add_replace_or_remove_fields import AddReplaceOrRemoveFields
from .request_transform_v2body import RequestTransformV2Body
from .request_transform_v2query_params import RequestTransformV2QueryParams
from .request_transform_v2template_engine import RequestTransformV2TemplateEngine


class RequestTransformV2(UniversalBaseModel):
    body: typing.Optional[RequestTransformV2Body] = None
    method: typing.Optional[str] = None
    query_params: typing.Optional[RequestTransformV2QueryParams] = None
    request_headers: typing.Optional[AddReplaceOrRemoveFields] = None
    template_engine: typing.Optional[RequestTransformV2TemplateEngine] = None
    url: typing.Optional[str] = None
    version: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
