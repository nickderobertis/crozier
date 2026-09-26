

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class BaseReportGenerationConfigApiModelCloudType(enum.StrEnum):
    """
    Cloud type
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
        if self is BaseReportGenerationConfigApiModelCloudType.AWS:
            return aws()
        if self is BaseReportGenerationConfigApiModelCloudType.AZURE:
            return azure()
        if self is BaseReportGenerationConfigApiModelCloudType.GCP:
            return gcp()
        if self is BaseReportGenerationConfigApiModelCloudType.ALIBABA_CLOUD:
            return alibaba_cloud()
        if self is BaseReportGenerationConfigApiModelCloudType.OCI:
            return oci()
