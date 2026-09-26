

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2table_columns_data_columns_item import V2TableColumnsDataColumnsItem


class V2TableColumnsData(UniversalBaseModel):
    """
    The table column list after a schema mutation.
    """

    columns: typing.List[V2TableColumnsDataColumnsItem] = pydantic.Field()
    """
    Current table columns.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
