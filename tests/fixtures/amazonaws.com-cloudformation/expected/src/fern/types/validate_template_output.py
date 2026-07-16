

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .capability import Capability
from .template_parameter import TemplateParameter
from .transform_name import TransformName


class ValidateTemplateOutput(UniversalBaseModel):
    """
    The output for <a>ValidateTemplate</a> action.
    """

    parameters: typing_extensions.Annotated[
        typing.Optional[typing.List[TemplateParameter]], FieldMetadata(alias="Parameters")
    ] = pydantic.Field(default=None)
    """
    A list of <code>TemplateParameter</code> structures.
    """

    description: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Description")] = pydantic.Field(
        default=None
    )
    """
    The description found within the template.
    """

    capabilities: typing_extensions.Annotated[
        typing.Optional[typing.List[Capability]], FieldMetadata(alias="Capabilities")
    ] = pydantic.Field(default=None)
    """
    <p>The capabilities found within the template. If your template contains IAM resources, you must specify the CAPABILITY_IAM or CAPABILITY_NAMED_IAM value for this parameter when you use the <a>CreateStack</a> or <a>UpdateStack</a> actions with your template; otherwise, those actions return an InsufficientCapabilities error.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM Resources in CloudFormation Templates</a>.</p>
    """

    capabilities_reason: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="CapabilitiesReason")
    ] = pydantic.Field(default=None)
    """
    The list of resources that generated the values in the <code>Capabilities</code> response element.
    """

    declared_transforms: typing_extensions.Annotated[
        typing.Optional[typing.List[TransformName]], FieldMetadata(alias="DeclaredTransforms")
    ] = pydantic.Field(default=None)
    """
    A list of the transforms that are declared in the template.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
