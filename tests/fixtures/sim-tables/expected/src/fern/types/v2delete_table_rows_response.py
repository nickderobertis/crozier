

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2delete_rows_data import V2DeleteRowsData


class V2DeleteTableRowsResponse(UniversalBaseModel):
    """
    Deleted row counts, identifiers, and optional missing identifiers.
    """

    data: V2DeleteRowsData = pydantic.Field()
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
