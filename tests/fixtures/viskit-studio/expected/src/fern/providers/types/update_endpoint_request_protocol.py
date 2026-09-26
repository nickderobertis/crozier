

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateEndpointRequestProtocol(enum.StrEnum):
    OPENAI_COMPATIBLE = "openai_compatible"
    ANTHROPIC_COMPATIBLE = "anthropic_compatible"
    IMAGE_GENERATION = "image_generation"

    def visit(
        self,
        openai_compatible: typing.Callable[[], T_Result],
        anthropic_compatible: typing.Callable[[], T_Result],
        image_generation: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateEndpointRequestProtocol.OPENAI_COMPATIBLE:
            return openai_compatible()
        if self is UpdateEndpointRequestProtocol.ANTHROPIC_COMPATIBLE:
            return anthropic_compatible()
        if self is UpdateEndpointRequestProtocol.IMAGE_GENERATION:
            return image_generation()
