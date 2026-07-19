

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037job_tres_allocated_item import Dbv0037JobTresAllocatedItem
from .dbv0037job_tres_requested_item import Dbv0037JobTresRequestedItem


class Dbv0037JobTres(UniversalBaseModel):
    """
    TRES settings
    """

    allocated: typing.Optional[typing.List[Dbv0037JobTresAllocatedItem]] = pydantic.Field(default=None)
    """
    TRES list of attributes
    """

    requested: typing.Optional[typing.List[Dbv0037JobTresRequestedItem]] = pydantic.Field(default=None)
    """
    TRES list of attributes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
