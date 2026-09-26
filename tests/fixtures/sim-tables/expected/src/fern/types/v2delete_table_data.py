

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V2DeleteTableData(UniversalBaseModel):
    """
    Table deletion acknowledgement.
    """

    id: str = pydantic.Field()
    """
    Identifier of the deleted table.
    """

    deleted: bool = pydantic.Field()
    """
    Confirms that the table was deleted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
