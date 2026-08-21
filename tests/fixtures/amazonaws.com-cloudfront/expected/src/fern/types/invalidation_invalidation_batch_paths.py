

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class InvalidationInvalidationBatchPaths(UniversalBaseModel):
    """
    A complex type that contains information about the objects that you want to invalidate. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html#invalidation-specifying-objects">Specifying the Objects to Invalidate</a> in the <i>Amazon CloudFront Developer Guide</i>.
    """

    quantity: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Quantity"),
        pydantic.Field(alias="Quantity", description="The number of objects that you want to invalidate."),
    ]
    """
    The number of objects that you want to invalidate.
    """

    items: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="Items"),
        pydantic.Field(
            alias="Items", description="A complex type that contains a list of the paths that you want to invalidate."
        ),
    ] = None
    """
    A complex type that contains a list of the paths that you want to invalidate.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
