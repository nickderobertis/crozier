

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetTemplateInputTemplateStage(str, enum.Enum):
    """
    <p>For templates that include transforms, the stage of the template that CloudFormation returns. To get the user-submitted template, specify <code>Original</code>. To get the template after CloudFormation has processed all transforms, specify <code>Processed</code>.</p> <p>If the template doesn't include transforms, <code>Original</code> and <code>Processed</code> return the same template. By default, CloudFormation specifies <code>Processed</code>.</p>
    """

    ORIGINAL = "Original"
    PROCESSED = "Processed"

    def visit(self, original: typing.Callable[[], T_Result], processed: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetTemplateInputTemplateStage.ORIGINAL:
            return original()
        if self is GetTemplateInputTemplateStage.PROCESSED:
            return processed()
