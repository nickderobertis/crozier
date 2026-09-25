

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1unprocessable_entity_error_errors_value import V1UnprocessableEntityErrorErrorsValue


class V1UnprocessableEntityError(UniversalBaseModel):
    errors: typing.Dict[str, V1UnprocessableEntityErrorErrorsValue] = pydantic.Field()
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
