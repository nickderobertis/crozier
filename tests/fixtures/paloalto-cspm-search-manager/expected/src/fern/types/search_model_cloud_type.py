

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SearchModelCloudType(enum.StrEnum):
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
        if self is SearchModelCloudType.AWS:
            return aws()
        if self is SearchModelCloudType.AZURE:
            return azure()
        if self is SearchModelCloudType.GCP:
            return gcp()
        if self is SearchModelCloudType.ALIBABA_CLOUD:
            return alibaba_cloud()
        if self is SearchModelCloudType.OCI:
            return oci()
