

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TestTypeOutput(UniversalBaseModel):
    type_version_arn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TypeVersionArn"),
        pydantic.Field(alias="TypeVersionArn", description="The Amazon Resource Name (ARN) of the extension."),
    ] = None
    """
    The Amazon Resource Name (ARN) of the extension.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
