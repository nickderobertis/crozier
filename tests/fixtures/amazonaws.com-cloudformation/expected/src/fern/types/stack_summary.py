

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack_summary_drift_information import StackSummaryDriftInformation
from .stack_summary_stack_status import StackSummaryStackStatus


class StackSummary(UniversalBaseModel):
    """
    The StackSummary Data Type
    """

    stack_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StackId"),
        pydantic.Field(alias="StackId", description="Unique stack identifier."),
    ] = None
    """
    Unique stack identifier.
    """

    stack_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="StackName"),
        pydantic.Field(alias="StackName", description="The name associated with the stack."),
    ]
    """
    The name associated with the stack.
    """

    template_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TemplateDescription"),
        pydantic.Field(
            alias="TemplateDescription",
            description="The template description of the template used to create the stack.",
        ),
    ] = None
    """
    The template description of the template used to create the stack.
    """

    creation_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="CreationTime"),
        pydantic.Field(alias="CreationTime", description="The time the stack was created."),
    ]
    """
    The time the stack was created.
    """

    last_updated_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="LastUpdatedTime"),
        pydantic.Field(
            alias="LastUpdatedTime",
            description="The time the stack was last updated. This field will only be returned if the stack has been updated at least once.",
        ),
    ] = None
    """
    The time the stack was last updated. This field will only be returned if the stack has been updated at least once.
    """

    deletion_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="DeletionTime"),
        pydantic.Field(alias="DeletionTime", description="The time the stack was deleted."),
    ] = None
    """
    The time the stack was deleted.
    """

    stack_status: typing_extensions.Annotated[
        StackSummaryStackStatus,
        FieldMetadata(alias="StackStatus"),
        pydantic.Field(alias="StackStatus", description="The current status of the stack."),
    ]
    """
    The current status of the stack.
    """

    stack_status_reason: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StackStatusReason"),
        pydantic.Field(
            alias="StackStatusReason", description="Success/Failure message associated with the stack status."
        ),
    ] = None
    """
    Success/Failure message associated with the stack status.
    """

    parent_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ParentId"),
        pydantic.Field(
            alias="ParentId",
            description='<p>For nested stacks--stacks created as resources for another stack--the stack ID of the direct parent of this stack. For the first level of nested stacks, the root stack is also the parent stack.</p> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">Working with Nested Stacks</a> in the <i>CloudFormation User Guide</i>.</p>',
        ),
    ] = None
    """
    <p>For nested stacks--stacks created as resources for another stack--the stack ID of the direct parent of this stack. For the first level of nested stacks, the root stack is also the parent stack.</p> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">Working with Nested Stacks</a> in the <i>CloudFormation User Guide</i>.</p>
    """

    root_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="RootId"),
        pydantic.Field(
            alias="RootId",
            description='<p>For nested stacks--stacks created as resources for another stack--the stack ID of the top-level stack to which the nested stack ultimately belongs.</p> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">Working with Nested Stacks</a> in the <i>CloudFormation User Guide</i>.</p>',
        ),
    ] = None
    """
    <p>For nested stacks--stacks created as resources for another stack--the stack ID of the top-level stack to which the nested stack ultimately belongs.</p> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">Working with Nested Stacks</a> in the <i>CloudFormation User Guide</i>.</p>
    """

    drift_information: typing_extensions.Annotated[
        typing.Optional[StackSummaryDriftInformation],
        FieldMetadata(alias="DriftInformation"),
        pydantic.Field(
            alias="DriftInformation",
            description="Summarizes information about whether a stack's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see <a href=\"http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html\">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.",
        ),
    ] = None
    """
    Summarizes information about whether a stack's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
