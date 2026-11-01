

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .move_page_parent_request_database_id_type import MovePageParentRequestDatabaseIdType


class MovePageParentRequestDatabaseId(UniversalBaseModel):
    type: MovePageParentRequestDatabaseIdType
    database_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
