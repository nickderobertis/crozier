

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PolicyScanConfigModelTargetAlertRulePolicyFilterCloudTypeItem(enum.StrEnum):
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
        if self is PolicyScanConfigModelTargetAlertRulePolicyFilterCloudTypeItem.ALL:
            return all_()
        if self is PolicyScanConfigModelTargetAlertRulePolicyFilterCloudTypeItem.AWS:
            return aws()
        if self is PolicyScanConfigModelTargetAlertRulePolicyFilterCloudTypeItem.AZURE:
            return azure()
        if self is PolicyScanConfigModelTargetAlertRulePolicyFilterCloudTypeItem.GCP:
            return gcp()
        if self is PolicyScanConfigModelTargetAlertRulePolicyFilterCloudTypeItem.ALIBABA_CLOUD:
            return alibaba_cloud()
        if self is PolicyScanConfigModelTargetAlertRulePolicyFilterCloudTypeItem.OCI:
            return oci()
        if self is PolicyScanConfigModelTargetAlertRulePolicyFilterCloudTypeItem.IBM:
            return ibm()
