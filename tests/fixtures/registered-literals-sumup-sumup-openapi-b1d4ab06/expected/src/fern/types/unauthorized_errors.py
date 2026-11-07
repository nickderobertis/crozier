

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .unauthorized_errors_type import UnauthorizedErrorsType


class UnauthorizedErrors(UniversalBaseModel):
    detail: str = pydantic.Field()
    """
    Fuller message giving context to error
    """

    type: typing.Optional[UnauthorizedErrorsType] = pydantic.Field(default=None)
    """
    Key indicating type of error. Present only for typed 401 responses (e.g. invalid token, invalid password). Absent for generic unauthorized responses.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
