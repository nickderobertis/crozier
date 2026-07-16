

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .describe_type_registration_output_progress_status import DescribeTypeRegistrationOutputProgressStatus


class DescribeTypeRegistrationOutput(UniversalBaseModel):
    progress_status: typing_extensions.Annotated[
        typing.Optional[DescribeTypeRegistrationOutputProgressStatus], FieldMetadata(alias="ProgressStatus")
    ] = pydantic.Field(default=None)
    """
    The current status of the extension registration request.
    """

    description: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Description")] = pydantic.Field(
        default=None
    )
    """
    The description of the extension registration request.
    """

    type_arn: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TypeArn")] = pydantic.Field(
        default=None
    )
    """
    <p>The Amazon Resource Name (ARN) of the extension being registered.</p> <p>For registration requests with a <code>ProgressStatus</code> of other than <code>COMPLETE</code>, this will be <code>null</code>.</p>
    """

    type_version_arn: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TypeVersionArn")] = (
        pydantic.Field(default=None)
    )
    """
    <p>The Amazon Resource Name (ARN) of this specific version of the extension being registered.</p> <p>For registration requests with a <code>ProgressStatus</code> of other than <code>COMPLETE</code>, this will be <code>null</code>.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
