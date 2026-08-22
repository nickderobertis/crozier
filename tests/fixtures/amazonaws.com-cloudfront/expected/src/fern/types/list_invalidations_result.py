

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_invalidations_result_invalidation_list import ListInvalidationsResultInvalidationList


class ListInvalidationsResult(UniversalBaseModel):
    """
    The returned result of the corresponding request.
    """

    invalidation_list: typing_extensions.Annotated[
        typing.Optional[ListInvalidationsResultInvalidationList],
        FieldMetadata(alias="InvalidationList"),
        pydantic.Field(alias="InvalidationList", description="Information about invalidation batches. "),
    ] = None
    """
    Information about invalidation batches. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
