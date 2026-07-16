

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .resource_change_detail_change_source import ResourceChangeDetailChangeSource
from .resource_change_detail_evaluation import ResourceChangeDetailEvaluation
from .resource_change_detail_target import ResourceChangeDetailTarget


class ResourceChangeDetail(UniversalBaseModel):
    """
    For a resource with <code>Modify</code> as the action, the <code>ResourceChange</code> structure describes the changes CloudFormation will make to that resource.
    """

    target: typing_extensions.Annotated[typing.Optional[ResourceChangeDetailTarget], FieldMetadata(alias="Target")] = (
        pydantic.Field(default=None)
    )
    """
    A <code>ResourceTargetDefinition</code> structure that describes the field that CloudFormation will change and whether the resource will be recreated.
    """

    evaluation: typing_extensions.Annotated[
        typing.Optional[ResourceChangeDetailEvaluation], FieldMetadata(alias="Evaluation")
    ] = pydantic.Field(default=None)
    """
    <p>Indicates whether CloudFormation can determine the target value, and whether the target value will change before you execute a change set.</p> <p>For <code>Static</code> evaluations, CloudFormation can determine that the target value will change, and its value. For example, if you directly modify the <code>InstanceType</code> property of an EC2 instance, CloudFormation knows that this property value will change, and its value, so this is a <code>Static</code> evaluation.</p> <p>For <code>Dynamic</code> evaluations, can't determine the target value because it depends on the result of an intrinsic function, such as a <code>Ref</code> or <code>Fn::GetAtt</code> intrinsic function, when the stack is updated. For example, if your template includes a reference to a resource that's conditionally recreated, the value of the reference (the physical ID of the resource) might change, depending on if the resource is recreated. If the resource is recreated, it will have a new physical ID, so all references to that resource will also be updated.</p>
    """

    change_source: typing_extensions.Annotated[
        typing.Optional[ResourceChangeDetailChangeSource], FieldMetadata(alias="ChangeSource")
    ] = pydantic.Field(default=None)
    """
    <p>The group to which the <code>CausingEntity</code> value belongs. There are five entity groups:</p> <ul> <li> <p> <code>ResourceReference</code> entities are <code>Ref</code> intrinsic functions that refer to resources in the template, such as <code>{ "Ref" : "MyEC2InstanceResource" }</code>.</p> </li> <li> <p> <code>ParameterReference</code> entities are <code>Ref</code> intrinsic functions that get template parameter values, such as <code>{ "Ref" : "MyPasswordParameter" }</code>.</p> </li> <li> <p> <code>ResourceAttribute</code> entities are <code>Fn::GetAtt</code> intrinsic functions that get resource attribute values, such as <code>{ "Fn::GetAtt" : [ "MyEC2InstanceResource", "PublicDnsName" ] }</code>.</p> </li> <li> <p> <code>DirectModification</code> entities are changes that are made directly to the template.</p> </li> <li> <p> <code>Automatic</code> entities are <code>AWS::CloudFormation::Stack</code> resource types, which are also known as nested stacks. If you made no changes to the <code>AWS::CloudFormation::Stack</code> resource, CloudFormation sets the <code>ChangeSource</code> to <code>Automatic</code> because the nested stack's template might have changed. Changes to a nested stack's template aren't visible to CloudFormation until you run an update on the parent stack.</p> </li> </ul>
    """

    causing_entity: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="CausingEntity")] = (
        pydantic.Field(default=None)
    )
    """
    <p>The identity of the entity that triggered this change. This entity is a member of the group that's specified by the <code>ChangeSource</code> field. For example, if you modified the value of the <code>KeyPairName</code> parameter, the <code>CausingEntity</code> is the name of the parameter (<code>KeyPairName</code>).</p> <p>If the <code>ChangeSource</code> value is <code>DirectModification</code>, no value is given for <code>CausingEntity</code>.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
