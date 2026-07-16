

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .get_template_input_template_stage import GetTemplateInputTemplateStage


class GetTemplateInput(UniversalBaseModel):
    """
    The input for a <a>GetTemplate</a> action.
    """

    stack_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StackName"),
        pydantic.Field(
            alias="StackName",
            description="<p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p>",
        ),
    ] = None
    """
    <p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p>
    """

    change_set_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ChangeSetName"),
        pydantic.Field(
            alias="ChangeSetName",
            description="The name or Amazon Resource Name (ARN) of a change set for which CloudFormation returns the associated template. If you specify a name, you must also specify the <code>StackName</code>.",
        ),
    ] = None
    """
    The name or Amazon Resource Name (ARN) of a change set for which CloudFormation returns the associated template. If you specify a name, you must also specify the <code>StackName</code>.
    """

    template_stage: typing_extensions.Annotated[
        typing.Optional[GetTemplateInputTemplateStage],
        FieldMetadata(alias="TemplateStage"),
        pydantic.Field(
            alias="TemplateStage",
            description="<p>For templates that include transforms, the stage of the template that CloudFormation returns. To get the user-submitted template, specify <code>Original</code>. To get the template after CloudFormation has processed all transforms, specify <code>Processed</code>.</p> <p>If the template doesn't include transforms, <code>Original</code> and <code>Processed</code> return the same template. By default, CloudFormation specifies <code>Processed</code>.</p>",
        ),
    ] = None
    """
    <p>For templates that include transforms, the stage of the template that CloudFormation returns. To get the user-submitted template, specify <code>Original</code>. To get the template after CloudFormation has processed all transforms, specify <code>Processed</code>.</p> <p>If the template doesn't include transforms, <code>Original</code> and <code>Processed</code> return the same template. By default, CloudFormation specifies <code>Processed</code>.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
