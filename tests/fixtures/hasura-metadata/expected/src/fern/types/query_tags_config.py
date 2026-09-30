

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .query_tags_format import QueryTagsFormat


class QueryTagsConfig(UniversalBaseModel):
    disabled: typing.Optional[bool] = None
    format: typing.Optional[QueryTagsFormat] = None
    omit_request_id: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
