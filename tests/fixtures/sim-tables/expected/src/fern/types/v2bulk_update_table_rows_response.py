

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2bulk_update_rows_data import V2BulkUpdateRowsData


class V2BulkUpdateTableRowsResponse(UniversalBaseModel):
    """
    Updated row count and identifiers.
    """

    data: V2BulkUpdateRowsData = pydantic.Field()
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
