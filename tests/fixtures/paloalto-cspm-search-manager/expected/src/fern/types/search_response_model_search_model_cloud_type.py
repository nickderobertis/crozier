

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SearchResponseModelSearchModelCloudType(enum.StrEnum):
    """
    Cloud Type
    """

    AWS = "aws"
    AZURE = "azure"
    GCP = "gcp"
    ALIBABA_CLOUD = "alibaba_cloud"
    OCI = "oci"

    def visit(
        self,
        aws: typing.Callable[[], T_Result],
        azure: typing.Callable[[], T_Result],
        gcp: typing.Callable[[], T_Result],
        alibaba_cloud: typing.Callable[[], T_Result],
        oci: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchResponseModelSearchModelCloudType.AWS:
            return aws()
        if self is SearchResponseModelSearchModelCloudType.AZURE:
            return azure()
        if self is SearchResponseModelSearchModelCloudType.GCP:
            return gcp()
        if self is SearchResponseModelSearchModelCloudType.ALIBABA_CLOUD:
            return alibaba_cloud()
        if self is SearchResponseModelSearchModelCloudType.OCI:
            return oci()
