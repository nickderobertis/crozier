

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bad_request_errors_type import BadRequestErrorsType


class BadRequestErrors(UniversalBaseModel):
    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    Fuller message giving context to error
    """

    type: BadRequestErrorsType = pydantic.Field()
    """
    Key indicating type of error
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
