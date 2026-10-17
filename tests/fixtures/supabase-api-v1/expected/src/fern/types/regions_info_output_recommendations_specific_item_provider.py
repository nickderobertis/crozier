

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RegionsInfoOutputRecommendationsSpecificItemProvider(enum.StrEnum):
    AWS = "AWS"
    AWS_K8S = "AWS_K8S"
    AWS_NIMBUS = "AWS_NIMBUS"

    def visit(
        self,
        aws: typing.Callable[[], T_Result],
        aws_k8s: typing.Callable[[], T_Result],
        aws_nimbus: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RegionsInfoOutputRecommendationsSpecificItemProvider.AWS:
            return aws()
        if self is RegionsInfoOutputRecommendationsSpecificItemProvider.AWS_K8S:
            return aws_k8s()
        if self is RegionsInfoOutputRecommendationsSpecificItemProvider.AWS_NIMBUS:
            return aws_nimbus()
