

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_source_id_parent_request_type import DataSourceIdParentRequestType


class DataSourceIdParentRequest(UniversalBaseModel):
    type: typing.Optional[DataSourceIdParentRequestType] = None
    database_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
