

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .invalid_entity_type_error_error import InvalidEntityTypeErrorError


class InvalidEntityTypeError(UniversalBaseModel):
    """
    Returned when an operation requires a specific entity type but the target entity has a different or unsupported type. For example, requesting file content from an entity that is not a MediaObject.
    """

    error: InvalidEntityTypeErrorError

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
