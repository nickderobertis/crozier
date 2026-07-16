

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetGetTemplateRequestTemplateStage(str, enum.Enum):
    ORIGINAL = "Original"
    PROCESSED = "Processed"

    def visit(self, original: typing.Callable[[], T_Result], processed: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetGetTemplateRequestTemplateStage.ORIGINAL:
            return original()
        if self is GetGetTemplateRequestTemplateStage.PROCESSED:
            return processed()
