

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResourceChangeDetailEvaluation(enum.StrEnum):
    """
    <p>Indicates whether CloudFormation can determine the target value, and whether the target value will change before you execute a change set.</p> <p>For <code>Static</code> evaluations, CloudFormation can determine that the target value will change, and its value. For example, if you directly modify the <code>InstanceType</code> property of an EC2 instance, CloudFormation knows that this property value will change, and its value, so this is a <code>Static</code> evaluation.</p> <p>For <code>Dynamic</code> evaluations, can't determine the target value because it depends on the result of an intrinsic function, such as a <code>Ref</code> or <code>Fn::GetAtt</code> intrinsic function, when the stack is updated. For example, if your template includes a reference to a resource that's conditionally recreated, the value of the reference (the physical ID of the resource) might change, depending on if the resource is recreated. If the resource is recreated, it will have a new physical ID, so all references to that resource will also be updated.</p>
    """

    STATIC = "Static"
    DYNAMIC = "Dynamic"

    def visit(self, static: typing.Callable[[], T_Result], dynamic: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResourceChangeDetailEvaluation.STATIC:
            return static()
        if self is ResourceChangeDetailEvaluation.DYNAMIC:
            return dynamic()
