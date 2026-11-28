

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .connection_files_paginated_list_connection_files_item import ConnectionFilesPaginatedListConnectionFilesItem
from .pagination import Pagination


class ConnectionFilesPaginatedList(Pagination):
    connection_files: typing_extensions.Annotated[
        typing.Optional[typing.List[ConnectionFilesPaginatedListConnectionFilesItem]],
        FieldMetadata(alias="connectionFiles"),
        pydantic.Field(alias="connectionFiles"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
