

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PublishTypeOutput(UniversalBaseModel):
    public_type_arn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PublicTypeArn"),
        pydantic.Field(
            alias="PublicTypeArn",
            description="The Amazon Resource Name (ARN) assigned to the public extension upon publication.",
        ),
    ] = None
    """
    The Amazon Resource Name (ARN) assigned to the public extension upon publication.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
