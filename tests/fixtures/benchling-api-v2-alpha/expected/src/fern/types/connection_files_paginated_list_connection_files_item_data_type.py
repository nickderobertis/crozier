

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConnectionFilesPaginatedListConnectionFilesItemDataType(enum.StrEnum):
    ALLOTROPE = "ALLOTROPE"
    COMPENSATION = "COMPENSATION"
    DATACUBE = "DATACUBE"
    FRACTIONS = "FRACTIONS"
    GROUP = "GROUP"
    INJECTIONS = "INJECTIONS"
    MEASUREMENT = "MEASUREMENT"
    MEASUREMENT_SEPARATE_UNIT_COLUMN = "MEASUREMENT_SEPARATE_UNIT_COLUMN"
    ORIGINAL = "ORIGINAL"
    PEAKS = "PEAKS"
    PROCESSED = "PROCESSED"
    POPULATION = "POPULATION"
    REGION = "REGION"
    REPORT_POINT = "REPORT_POINT"
    REPORT = "REPORT"
    SAMPLE = "SAMPLE"
    SAMPLE_SEPARATE_UNIT_COLUMN = "SAMPLE_SEPARATE_UNIT_COLUMN"
    STATISTICS = "STATISTICS"
    TIMESERIES = "TIMESERIES"
    WELL = "WELL"

    def visit(
        self,
        allotrope: typing.Callable[[], T_Result],
        compensation: typing.Callable[[], T_Result],
        datacube: typing.Callable[[], T_Result],
        fractions: typing.Callable[[], T_Result],
        group: typing.Callable[[], T_Result],
        injections: typing.Callable[[], T_Result],
        measurement: typing.Callable[[], T_Result],
        measurement_separate_unit_column: typing.Callable[[], T_Result],
        original: typing.Callable[[], T_Result],
        peaks: typing.Callable[[], T_Result],
        processed: typing.Callable[[], T_Result],
        population: typing.Callable[[], T_Result],
        region: typing.Callable[[], T_Result],
        report_point: typing.Callable[[], T_Result],
        report: typing.Callable[[], T_Result],
        sample: typing.Callable[[], T_Result],
        sample_separate_unit_column: typing.Callable[[], T_Result],
        statistics: typing.Callable[[], T_Result],
        timeseries: typing.Callable[[], T_Result],
        well: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.ALLOTROPE:
            return allotrope()
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.COMPENSATION:
            return compensation()
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.DATACUBE:
            return datacube()
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.FRACTIONS:
            return fractions()
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.GROUP:
            return group()
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.INJECTIONS:
            return injections()
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.MEASUREMENT:
            return measurement()
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.MEASUREMENT_SEPARATE_UNIT_COLUMN:
            return measurement_separate_unit_column()
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.ORIGINAL:
            return original()
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.PEAKS:
            return peaks()
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.PROCESSED:
            return processed()
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.POPULATION:
            return population()
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.REGION:
            return region()
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.REPORT_POINT:
            return report_point()
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.REPORT:
            return report()
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.SAMPLE:
            return sample()
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.SAMPLE_SEPARATE_UNIT_COLUMN:
            return sample_separate_unit_column()
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.STATISTICS:
            return statistics()
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.TIMESERIES:
            return timeseries()
        if self is ConnectionFilesPaginatedListConnectionFilesItemDataType.WELL:
            return well()
