

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ResourceChangeReplacement(str, enum.Enum):
    """
    <p>For the <code>Modify</code> action, indicates whether CloudFormation will replace the resource by creating a new one and deleting the old one. This value depends on the value of the <code>RequiresRecreation</code> property in the <code>ResourceTargetDefinition</code> structure. For example, if the <code>RequiresRecreation</code> field is <code>Always</code> and the <code>Evaluation</code> field is <code>Static</code>, <code>Replacement</code> is <code>True</code>. If the <code>RequiresRecreation</code> field is <code>Always</code> and the <code>Evaluation</code> field is <code>Dynamic</code>, <code>Replacement</code> is <code>Conditionally</code>.</p> <p>If you have multiple changes with different <code>RequiresRecreation</code> values, the <code>Replacement</code> value depends on the change with the most impact. A <code>RequiresRecreation</code> value of <code>Always</code> has the most impact, followed by <code>Conditionally</code>, and then <code>Never</code>.</p>
    """

    TRUE = "True"
    FALSE = "False"
    CONDITIONAL = "Conditional"

    def visit(
        self,
        true: typing.Callable[[], T_Result],
        false: typing.Callable[[], T_Result],
        conditional: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResourceChangeReplacement.TRUE:
            return true()
        if self is ResourceChangeReplacement.FALSE:
            return false()
        if self is ResourceChangeReplacement.CONDITIONAL:
            return conditional()
