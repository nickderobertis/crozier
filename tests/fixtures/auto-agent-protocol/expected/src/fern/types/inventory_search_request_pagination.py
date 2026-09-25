

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InventorySearchRequestPagination(UniversalBaseModel):
    """
    Result paging. Default values are dealer-defined; spec recommends limit defaults <= 50 and limit cap of 100.
    """

    skip: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of results to skip from the start of the matching set.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum number of results to return on this page.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
