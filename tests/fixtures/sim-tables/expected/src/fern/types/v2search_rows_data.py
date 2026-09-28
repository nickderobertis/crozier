

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2table_row_match import V2TableRowMatch


class V2SearchRowsData(UniversalBaseModel):
    """
    Matching table cells and truncation state.
    """

    matches: typing.List[V2TableRowMatch] = pydantic.Field()
    """
    Matching table cells, at most 1000.
    """

    truncated: bool = pydantic.Field()
    """
    Whether more than 1000 cells matched, so the list was cut.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
