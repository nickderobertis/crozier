

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListConnectFilesRequestDataType(enum.StrEnum):
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
        if self is ListConnectFilesRequestDataType.ALLOTROPE:
            return allotrope()
        if self is ListConnectFilesRequestDataType.COMPENSATION:
            return compensation()
        if self is ListConnectFilesRequestDataType.DATACUBE:
            return datacube()
        if self is ListConnectFilesRequestDataType.FRACTIONS:
            return fractions()
        if self is ListConnectFilesRequestDataType.GROUP:
            return group()
        if self is ListConnectFilesRequestDataType.INJECTIONS:
            return injections()
        if self is ListConnectFilesRequestDataType.MEASUREMENT:
            return measurement()
        if self is ListConnectFilesRequestDataType.MEASUREMENT_SEPARATE_UNIT_COLUMN:
            return measurement_separate_unit_column()
        if self is ListConnectFilesRequestDataType.ORIGINAL:
            return original()
        if self is ListConnectFilesRequestDataType.PEAKS:
            return peaks()
        if self is ListConnectFilesRequestDataType.PROCESSED:
            return processed()
        if self is ListConnectFilesRequestDataType.POPULATION:
            return population()
        if self is ListConnectFilesRequestDataType.REGION:
            return region()
        if self is ListConnectFilesRequestDataType.REPORT_POINT:
            return report_point()
        if self is ListConnectFilesRequestDataType.REPORT:
            return report()
        if self is ListConnectFilesRequestDataType.SAMPLE:
            return sample()
        if self is ListConnectFilesRequestDataType.SAMPLE_SEPARATE_UNIT_COLUMN:
            return sample_separate_unit_column()
        if self is ListConnectFilesRequestDataType.STATISTICS:
            return statistics()
        if self is ListConnectFilesRequestDataType.TIMESERIES:
            return timeseries()
        if self is ListConnectFilesRequestDataType.WELL:
            return well()
