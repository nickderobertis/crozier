

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .get_invalidation_result_invalidation import GetInvalidationResultInvalidation


class GetInvalidationResult(UniversalBaseModel):
    """
    The returned result of the corresponding request.
    """

    invalidation: typing_extensions.Annotated[
        typing.Optional[GetInvalidationResultInvalidation],
        FieldMetadata(alias="Invalidation"),
        pydantic.Field(
            alias="Invalidation",
            description='The invalidation\'s information. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/InvalidationDatatype.html">Invalidation Complex Type</a>. ',
        ),
    ] = None
    """
    The invalidation's information. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/InvalidationDatatype.html">Invalidation Complex Type</a>. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
