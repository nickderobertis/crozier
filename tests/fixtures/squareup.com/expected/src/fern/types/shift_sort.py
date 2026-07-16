

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ShiftSort(UniversalBaseModel):
    """
    Sets the sort order of search results.
    """

    field: typing.Optional[str] = pydantic.Field(default=None)
    """
    The field to sort on.
    """

    order: typing.Optional[str] = pydantic.Field(default=None)
    """
    The order in which results are returned. Defaults to DESC.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
