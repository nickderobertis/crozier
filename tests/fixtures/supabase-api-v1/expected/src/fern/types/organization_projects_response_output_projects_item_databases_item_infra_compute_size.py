

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize(enum.StrEnum):
    PICO = "pico"
    NANO = "nano"
    MICRO = "micro"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    XLARGE = "xlarge"
    TWO_XLARGE = "2xlarge"
    FOUR_XLARGE = "4xlarge"
    EIGHT_XLARGE = "8xlarge"
    TWELVE_XLARGE = "12xlarge"
    SIXTEEN_XLARGE = "16xlarge"
    TWENTY_FOUR_XLARGE = "24xlarge"
    TWENTY_FOUR_XLARGE_OPTIMIZED_MEMORY = "24xlarge_optimized_memory"
    TWENTY_FOUR_XLARGE_OPTIMIZED_CPU = "24xlarge_optimized_cpu"
    TWENTY_FOUR_XLARGE_HIGH_MEMORY = "24xlarge_high_memory"
    FORTY_EIGHT_XLARGE = "48xlarge"
    FORTY_EIGHT_XLARGE_OPTIMIZED_MEMORY = "48xlarge_optimized_memory"
    FORTY_EIGHT_XLARGE_OPTIMIZED_CPU = "48xlarge_optimized_cpu"
    FORTY_EIGHT_XLARGE_HIGH_MEMORY = "48xlarge_high_memory"

    def visit(
        self,
        pico: typing.Callable[[], T_Result],
        nano: typing.Callable[[], T_Result],
        micro: typing.Callable[[], T_Result],
        small: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        large: typing.Callable[[], T_Result],
        xlarge: typing.Callable[[], T_Result],
        two_xlarge: typing.Callable[[], T_Result],
        four_xlarge: typing.Callable[[], T_Result],
        eight_xlarge: typing.Callable[[], T_Result],
        twelve_xlarge: typing.Callable[[], T_Result],
        sixteen_xlarge: typing.Callable[[], T_Result],
        twenty_four_xlarge: typing.Callable[[], T_Result],
        twenty_four_xlarge_optimized_memory: typing.Callable[[], T_Result],
        twenty_four_xlarge_optimized_cpu: typing.Callable[[], T_Result],
        twenty_four_xlarge_high_memory: typing.Callable[[], T_Result],
        forty_eight_xlarge: typing.Callable[[], T_Result],
        forty_eight_xlarge_optimized_memory: typing.Callable[[], T_Result],
        forty_eight_xlarge_optimized_cpu: typing.Callable[[], T_Result],
        forty_eight_xlarge_high_memory: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.PICO:
            return pico()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.NANO:
            return nano()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.MICRO:
            return micro()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.SMALL:
            return small()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.MEDIUM:
            return medium()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.LARGE:
            return large()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.XLARGE:
            return xlarge()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.TWO_XLARGE:
            return two_xlarge()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.FOUR_XLARGE:
            return four_xlarge()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.EIGHT_XLARGE:
            return eight_xlarge()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.TWELVE_XLARGE:
            return twelve_xlarge()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.SIXTEEN_XLARGE:
            return sixteen_xlarge()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.TWENTY_FOUR_XLARGE:
            return twenty_four_xlarge()
        if (
            self
            is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.TWENTY_FOUR_XLARGE_OPTIMIZED_MEMORY
        ):
            return twenty_four_xlarge_optimized_memory()
        if (
            self
            is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.TWENTY_FOUR_XLARGE_OPTIMIZED_CPU
        ):
            return twenty_four_xlarge_optimized_cpu()
        if (
            self
            is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.TWENTY_FOUR_XLARGE_HIGH_MEMORY
        ):
            return twenty_four_xlarge_high_memory()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.FORTY_EIGHT_XLARGE:
            return forty_eight_xlarge()
        if (
            self
            is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.FORTY_EIGHT_XLARGE_OPTIMIZED_MEMORY
        ):
            return forty_eight_xlarge_optimized_memory()
        if (
            self
            is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.FORTY_EIGHT_XLARGE_OPTIMIZED_CPU
        ):
            return forty_eight_xlarge_optimized_cpu()
        if (
            self
            is OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize.FORTY_EIGHT_XLARGE_HIGH_MEMORY
        ):
            return forty_eight_xlarge_high_memory()
