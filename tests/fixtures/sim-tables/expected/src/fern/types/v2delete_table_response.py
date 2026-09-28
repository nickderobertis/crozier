

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2delete_table_data import V2DeleteTableData


class V2DeleteTableResponse(UniversalBaseModel):
    """
    Table deletion acknowledgement.
    """

    data: V2DeleteTableData = pydantic.Field()
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
