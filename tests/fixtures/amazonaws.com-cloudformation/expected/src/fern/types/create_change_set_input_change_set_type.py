

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateChangeSetInputChangeSetType(enum.StrEnum):
    """
    <p>The type of change set operation. To create a change set for a new stack, specify <code>CREATE</code>. To create a change set for an existing stack, specify <code>UPDATE</code>. To create a change set for an import operation, specify <code>IMPORT</code>.</p> <p>If you create a change set for a new stack, CloudFormation creates a stack with a unique stack ID, but no template or resources. The stack will be in the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-describing-stacks.html#d0e11995"> <code>REVIEW_IN_PROGRESS</code> </a> state until you execute the change set.</p> <p>By default, CloudFormation specifies <code>UPDATE</code>. You can't use the <code>UPDATE</code> type to create a change set for a new stack or the <code>CREATE</code> type to create a change set for an existing stack.</p>
    """

    CREATE = "CREATE"
    UPDATE = "UPDATE"
    IMPORT = "IMPORT"

    def visit(
        self,
        create: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        import_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateChangeSetInputChangeSetType.CREATE:
            return create()
        if self is CreateChangeSetInputChangeSetType.UPDATE:
            return update()
        if self is CreateChangeSetInputChangeSetType.IMPORT:
            return import_()
