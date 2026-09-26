

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1forbidden_error_errors import V1ForbiddenErrorErrors


class V1ForbiddenError(UniversalBaseModel):
    errors: V1ForbiddenErrorErrors = pydantic.Field()
    """
    Error details
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
