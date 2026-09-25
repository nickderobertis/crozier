

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PolicyRiskScoreModelCloudType(enum.StrEnum):
    """
    Cloud type (Required for config policies). Not case-sensitive. Default is **ALL**.
    """

    ALL = "ALL"
    AWS = "AWS"
    AZURE = "AZURE"
    GCP = "GCP"
    ALIBABA_CLOUD = "ALIBABA_CLOUD"
    OCI = "OCI"
    IBM = "IBM"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        aws: typing.Callable[[], T_Result],
        azure: typing.Callable[[], T_Result],
        gcp: typing.Callable[[], T_Result],
        alibaba_cloud: typing.Callable[[], T_Result],
        oci: typing.Callable[[], T_Result],
        ibm: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PolicyRiskScoreModelCloudType.ALL:
            return all_()
        if self is PolicyRiskScoreModelCloudType.AWS:
            return aws()
        if self is PolicyRiskScoreModelCloudType.AZURE:
            return azure()
        if self is PolicyRiskScoreModelCloudType.GCP:
            return gcp()
        if self is PolicyRiskScoreModelCloudType.ALIBABA_CLOUD:
            return alibaba_cloud()
        if self is PolicyRiskScoreModelCloudType.OCI:
            return oci()
        if self is PolicyRiskScoreModelCloudType.IBM:
            return ibm()
