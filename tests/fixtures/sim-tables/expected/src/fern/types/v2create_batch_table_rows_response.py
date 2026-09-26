

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2batch_insert_rows_data import V2BatchInsertRowsData


class V2CreateBatchTableRowsResponse(UniversalBaseModel):
    """
    Response returned after inserting a batch of table rows.
    """

    data: V2BatchInsertRowsData = pydantic.Field()
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
