

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_internal_error_type import MarimoInternalErrorType


class MarimoInternalError(UniversalBaseModel):
    """
    An internal error that should be hidden from the user.
    The error is logged to the console and then a new error is broadcasted
    such that the data is hidden.

    They can be linked back to the original error by the error_id.
    """

    error_id: str
    msg: typing.Optional[str] = None
    type: MarimoInternalErrorType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
