

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .create_invalidation_result_invalidation import CreateInvalidationResultInvalidation


class CreateInvalidationResult(UniversalBaseModel):
    """
    The returned result of the corresponding request.
    """

    invalidation: typing_extensions.Annotated[
        typing.Optional[CreateInvalidationResultInvalidation],
        FieldMetadata(alias="Invalidation"),
        pydantic.Field(alias="Invalidation", description="The invalidation's information."),
    ] = None
    """
    The invalidation's information.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
