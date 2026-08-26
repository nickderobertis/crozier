

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CellConfig(UniversalBaseModel):
    """
    Internal representation of a cell's configuration.
    This is not part of the public API.
    """

    column: typing.Optional[int] = None
    disabled: typing.Optional[bool] = None
    hide_code: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
