

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2query_rows_count_data import V2QueryRowsCountData


class V2CountTableRowsResponse(UniversalBaseModel):
    """
    The total number of table rows matching the predicate.
    """

    data: V2QueryRowsCountData = pydantic.Field()
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
