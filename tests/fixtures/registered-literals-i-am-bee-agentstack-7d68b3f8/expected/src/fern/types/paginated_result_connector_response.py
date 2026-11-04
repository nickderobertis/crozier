

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connector_response import ConnectorResponse


class PaginatedResultConnectorResponse(UniversalBaseModel):
    items: typing.List[ConnectorResponse]
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
