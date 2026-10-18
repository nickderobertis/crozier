

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RegionsInfoOutputAllSpecificItemProvider(enum.StrEnum):
    AWS = "AWS"
    AWS_K8S = "AWS_K8S"
    AWS_NIMBUS = "AWS_NIMBUS"

    def visit(
        self,
        aws: typing.Callable[[], T_Result],
        aws_k8s: typing.Callable[[], T_Result],
        aws_nimbus: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RegionsInfoOutputAllSpecificItemProvider.AWS:
            return aws()
        if self is RegionsInfoOutputAllSpecificItemProvider.AWS_K8S:
            return aws_k8s()
        if self is RegionsInfoOutputAllSpecificItemProvider.AWS_NIMBUS:
            return aws_nimbus()
