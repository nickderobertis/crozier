

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2upsert_row_data import V2UpsertRowData


class V2UpsertTableRowResponse(UniversalBaseModel):
    """
    The resulting row and whether it was inserted or updated.
    """

    data: V2UpsertRowData = pydantic.Field()
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
