

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_object_last_error_code import RunObjectLastErrorCode


class RunObjectLastError(UniversalBaseModel):
    """
    The last error associated with this run. Will be `null` if there are no errors.
    """

    code: RunObjectLastErrorCode = pydantic.Field()
    """
    One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.
    """

    message: str = pydantic.Field()
    """
    A human-readable description of the error.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
