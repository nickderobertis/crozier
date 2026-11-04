

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .error import Error


class ErrorExtended(Error):
    """
    Error payload with the invalid parameter reference.
    """

    param: typing.Optional[str] = pydantic.Field(default=None)
    """
    Parameter name (with relative location) to which the error applies. Parameters from embedded resources are displayed using dot notation. For example, `card.name` refers to the `name` parameter embedded in the `card` object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
