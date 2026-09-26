

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1not_found_error_errors import V1NotFoundErrorErrors


class V1NotFoundError(UniversalBaseModel):
    errors: V1NotFoundErrorErrors = pydantic.Field()
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
