

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1RemoveProjectAddonRequestAddonVariantZero(enum.StrEnum):
    CI_MICRO = "ci_micro"
    CI_SMALL = "ci_small"
    CI_MEDIUM = "ci_medium"
    CI_LARGE = "ci_large"
    CI_XLARGE = "ci_xlarge"
    CI2XLARGE = "ci_2xlarge"
    CI4XLARGE = "ci_4xlarge"
    CI8XLARGE = "ci_8xlarge"
    CI12XLARGE = "ci_12xlarge"
    CI16XLARGE = "ci_16xlarge"
    CI24XLARGE = "ci_24xlarge"
    CI24XLARGE_OPTIMIZED_CPU = "ci_24xlarge_optimized_cpu"
    CI24XLARGE_OPTIMIZED_MEMORY = "ci_24xlarge_optimized_memory"
    CI24XLARGE_HIGH_MEMORY = "ci_24xlarge_high_memory"
    CI48XLARGE = "ci_48xlarge"
    CI48XLARGE_OPTIMIZED_CPU = "ci_48xlarge_optimized_cpu"
    CI48XLARGE_OPTIMIZED_MEMORY = "ci_48xlarge_optimized_memory"
    CI48XLARGE_HIGH_MEMORY = "ci_48xlarge_high_memory"

    def visit(
        self,
        ci_micro: typing.Callable[[], T_Result],
        ci_small: typing.Callable[[], T_Result],
        ci_medium: typing.Callable[[], T_Result],
        ci_large: typing.Callable[[], T_Result],
        ci_xlarge: typing.Callable[[], T_Result],
        ci2xlarge: typing.Callable[[], T_Result],
        ci4xlarge: typing.Callable[[], T_Result],
        ci8xlarge: typing.Callable[[], T_Result],
        ci12xlarge: typing.Callable[[], T_Result],
        ci16xlarge: typing.Callable[[], T_Result],
        ci24xlarge: typing.Callable[[], T_Result],
        ci24xlarge_optimized_cpu: typing.Callable[[], T_Result],
        ci24xlarge_optimized_memory: typing.Callable[[], T_Result],
        ci24xlarge_high_memory: typing.Callable[[], T_Result],
        ci48xlarge: typing.Callable[[], T_Result],
        ci48xlarge_optimized_cpu: typing.Callable[[], T_Result],
        ci48xlarge_optimized_memory: typing.Callable[[], T_Result],
        ci48xlarge_high_memory: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1RemoveProjectAddonRequestAddonVariantZero.CI_MICRO:
            return ci_micro()
        if self is V1RemoveProjectAddonRequestAddonVariantZero.CI_SMALL:
            return ci_small()
        if self is V1RemoveProjectAddonRequestAddonVariantZero.CI_MEDIUM:
            return ci_medium()
        if self is V1RemoveProjectAddonRequestAddonVariantZero.CI_LARGE:
            return ci_large()
        if self is V1RemoveProjectAddonRequestAddonVariantZero.CI_XLARGE:
            return ci_xlarge()
        if self is V1RemoveProjectAddonRequestAddonVariantZero.CI2XLARGE:
            return ci2xlarge()
        if self is V1RemoveProjectAddonRequestAddonVariantZero.CI4XLARGE:
            return ci4xlarge()
        if self is V1RemoveProjectAddonRequestAddonVariantZero.CI8XLARGE:
            return ci8xlarge()
        if self is V1RemoveProjectAddonRequestAddonVariantZero.CI12XLARGE:
            return ci12xlarge()
        if self is V1RemoveProjectAddonRequestAddonVariantZero.CI16XLARGE:
            return ci16xlarge()
        if self is V1RemoveProjectAddonRequestAddonVariantZero.CI24XLARGE:
            return ci24xlarge()
        if self is V1RemoveProjectAddonRequestAddonVariantZero.CI24XLARGE_OPTIMIZED_CPU:
            return ci24xlarge_optimized_cpu()
        if self is V1RemoveProjectAddonRequestAddonVariantZero.CI24XLARGE_OPTIMIZED_MEMORY:
            return ci24xlarge_optimized_memory()
        if self is V1RemoveProjectAddonRequestAddonVariantZero.CI24XLARGE_HIGH_MEMORY:
            return ci24xlarge_high_memory()
        if self is V1RemoveProjectAddonRequestAddonVariantZero.CI48XLARGE:
            return ci48xlarge()
        if self is V1RemoveProjectAddonRequestAddonVariantZero.CI48XLARGE_OPTIMIZED_CPU:
            return ci48xlarge_optimized_cpu()
        if self is V1RemoveProjectAddonRequestAddonVariantZero.CI48XLARGE_OPTIMIZED_MEMORY:
            return ci48xlarge_optimized_memory()
        if self is V1RemoveProjectAddonRequestAddonVariantZero.CI48XLARGE_HIGH_MEMORY:
            return ci48xlarge_high_memory()
