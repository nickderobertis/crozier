

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .column_id import ColumnId
from .select_base import SelectBase


class FlagSelect(SelectBase):
    """
    Emits the labels of all of the columns having a `true` value. The columns must be of type boolean.
    """

    flags: typing.Optional[typing.Dict[str, ColumnId]] = pydantic.Field(default=None)
    """
    The keys are labels for the boolean columns.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
