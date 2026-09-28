

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2bulk_delete_tables_data import V2BulkDeleteTablesData


class V2BulkDeleteTablesResponse(UniversalBaseModel):
    """
    Per-item outcome of a bulk table and folder delete.
    """

    data: V2BulkDeleteTablesData = pydantic.Field()
    """
    Response data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
