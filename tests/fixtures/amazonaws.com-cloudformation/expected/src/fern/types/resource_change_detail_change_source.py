

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ResourceChangeDetailChangeSource(str, enum.Enum):
    """
    <p>The group to which the <code>CausingEntity</code> value belongs. There are five entity groups:</p> <ul> <li> <p> <code>ResourceReference</code> entities are <code>Ref</code> intrinsic functions that refer to resources in the template, such as <code>{ "Ref" : "MyEC2InstanceResource" }</code>.</p> </li> <li> <p> <code>ParameterReference</code> entities are <code>Ref</code> intrinsic functions that get template parameter values, such as <code>{ "Ref" : "MyPasswordParameter" }</code>.</p> </li> <li> <p> <code>ResourceAttribute</code> entities are <code>Fn::GetAtt</code> intrinsic functions that get resource attribute values, such as <code>{ "Fn::GetAtt" : [ "MyEC2InstanceResource", "PublicDnsName" ] }</code>.</p> </li> <li> <p> <code>DirectModification</code> entities are changes that are made directly to the template.</p> </li> <li> <p> <code>Automatic</code> entities are <code>AWS::CloudFormation::Stack</code> resource types, which are also known as nested stacks. If you made no changes to the <code>AWS::CloudFormation::Stack</code> resource, CloudFormation sets the <code>ChangeSource</code> to <code>Automatic</code> because the nested stack's template might have changed. Changes to a nested stack's template aren't visible to CloudFormation until you run an update on the parent stack.</p> </li> </ul>
    """

    RESOURCE_REFERENCE = "ResourceReference"
    PARAMETER_REFERENCE = "ParameterReference"
    RESOURCE_ATTRIBUTE = "ResourceAttribute"
    DIRECT_MODIFICATION = "DirectModification"
    AUTOMATIC = "Automatic"

    def visit(
        self,
        resource_reference: typing.Callable[[], T_Result],
        parameter_reference: typing.Callable[[], T_Result],
        resource_attribute: typing.Callable[[], T_Result],
        direct_modification: typing.Callable[[], T_Result],
        automatic: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResourceChangeDetailChangeSource.RESOURCE_REFERENCE:
            return resource_reference()
        if self is ResourceChangeDetailChangeSource.PARAMETER_REFERENCE:
            return parameter_reference()
        if self is ResourceChangeDetailChangeSource.RESOURCE_ATTRIBUTE:
            return resource_attribute()
        if self is ResourceChangeDetailChangeSource.DIRECT_MODIFICATION:
            return direct_modification()
        if self is ResourceChangeDetailChangeSource.AUTOMATIC:
            return automatic()
