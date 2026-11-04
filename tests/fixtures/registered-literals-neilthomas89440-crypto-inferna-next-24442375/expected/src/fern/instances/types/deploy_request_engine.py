

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DeployRequestEngine(enum.StrEnum):
    VLLM = "vllm"
    SGLANG = "sglang"

    def visit(self, vllm: typing.Callable[[], T_Result], sglang: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeployRequestEngine.VLLM:
            return vllm()
        if self is DeployRequestEngine.SGLANG:
            return sglang()
