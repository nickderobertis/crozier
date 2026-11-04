

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output1 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput1,
)


class PaginatedResultModelOutput(UniversalBaseModel):
    items: typing.List[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput1]
    total_count: int
    has_more: typing.Optional[bool] = None
    next_page_token: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
