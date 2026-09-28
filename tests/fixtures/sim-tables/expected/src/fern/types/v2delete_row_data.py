

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V2DeleteRowData(UniversalBaseModel):
    """
    Row deletion acknowledgement.
    """

    id: str = pydantic.Field()
    """
    Identifier of the deleted row.
    """

    deleted: bool = pydantic.Field()
    """
    Confirms that the row was deleted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
