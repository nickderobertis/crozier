

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TargetFilterModelAlertRulePolicyFilterCloudTypeItem(enum.StrEnum):
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
        if self is TargetFilterModelAlertRulePolicyFilterCloudTypeItem.ALL:
            return all_()
        if self is TargetFilterModelAlertRulePolicyFilterCloudTypeItem.AWS:
            return aws()
        if self is TargetFilterModelAlertRulePolicyFilterCloudTypeItem.AZURE:
            return azure()
        if self is TargetFilterModelAlertRulePolicyFilterCloudTypeItem.GCP:
            return gcp()
        if self is TargetFilterModelAlertRulePolicyFilterCloudTypeItem.ALIBABA_CLOUD:
            return alibaba_cloud()
        if self is TargetFilterModelAlertRulePolicyFilterCloudTypeItem.OCI:
            return oci()
        if self is TargetFilterModelAlertRulePolicyFilterCloudTypeItem.IBM:
            return ibm()
