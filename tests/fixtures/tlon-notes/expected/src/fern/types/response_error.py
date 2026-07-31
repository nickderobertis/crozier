

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .action_error import ActionError


class ResponseError(UniversalBaseModel):
    error_type: typing_extensions.Annotated[
        ActionError, FieldMetadata(alias="errorType"), pydantic.Field(alias="errorType")
    ]
    message: typing.List[str] = pydantic.Field()
    """
    Hoon `tang` rendered as JSON strings. Empty for now.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
