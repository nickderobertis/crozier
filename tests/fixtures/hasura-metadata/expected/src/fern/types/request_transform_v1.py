

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .add_replace_or_remove_fields import AddReplaceOrRemoveFields
from .request_transform_v1query_params import RequestTransformV1QueryParams
from .request_transform_v1template_engine import RequestTransformV1TemplateEngine


class RequestTransformV1(UniversalBaseModel):
    body: typing.Optional[str] = None
    method: typing.Optional[str] = None
    query_params: typing.Optional[RequestTransformV1QueryParams] = None
    request_headers: typing.Optional[AddReplaceOrRemoveFields] = None
    template_engine: typing.Optional[RequestTransformV1TemplateEngine] = None
    url: typing.Optional[str] = None
    version: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
