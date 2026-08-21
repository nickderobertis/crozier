

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .create_invalidation_request_invalidation_batch import CreateInvalidationRequestInvalidationBatch


class CreateInvalidationRequest(UniversalBaseModel):
    """
    The request to create an invalidation.
    """

    invalidation_batch: typing_extensions.Annotated[
        CreateInvalidationRequestInvalidationBatch,
        FieldMetadata(alias="InvalidationBatch"),
        pydantic.Field(alias="InvalidationBatch", description="The batch information for the invalidation."),
    ]
    """
    The batch information for the invalidation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
