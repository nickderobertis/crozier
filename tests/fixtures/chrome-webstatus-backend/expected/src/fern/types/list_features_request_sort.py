

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListFeaturesRequestSort(enum.StrEnum):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    BASELINE_STATUS_ASC = "baseline_status_asc"
    BASELINE_STATUS_DESC = "baseline_status_desc"
    STABLE_CHROME_ASC = "stable_chrome_asc"
    STABLE_CHROME_DESC = "stable_chrome_desc"
    STABLE_SAFARI_ASC = "stable_safari_asc"
    STABLE_SAFARI_DESC = "stable_safari_desc"
    STABLE_EDGE_ASC = "stable_edge_asc"
    STABLE_EDGE_DESC = "stable_edge_desc"
    STABLE_FIREFOX_ASC = "stable_firefox_asc"
    STABLE_FIREFOX_DESC = "stable_firefox_desc"
    STABLE_CHROME_ANDROID_ASC = "stable_chrome_android_asc"
    STABLE_CHROME_ANDROID_DESC = "stable_chrome_android_desc"
    STABLE_FIREFOX_ANDROID_ASC = "stable_firefox_android_asc"
    STABLE_FIREFOX_ANDROID_DESC = "stable_firefox_android_desc"
    STABLE_SAFARI_IOS_ASC = "stable_safari_ios_asc"
    STABLE_SAFARI_IOS_DESC = "stable_safari_ios_desc"
    EXPERIMENTAL_CHROME_ASC = "experimental_chrome_asc"
    EXPERIMENTAL_CHROME_DESC = "experimental_chrome_desc"
    EXPERIMENTAL_SAFARI_ASC = "experimental_safari_asc"
    EXPERIMENTAL_SAFARI_DESC = "experimental_safari_desc"
    EXPERIMENTAL_EDGE_ASC = "experimental_edge_asc"
    EXPERIMENTAL_EDGE_DESC = "experimental_edge_desc"
    EXPERIMENTAL_FIREFOX_ASC = "experimental_firefox_asc"
    EXPERIMENTAL_FIREFOX_DESC = "experimental_firefox_desc"
    EXPERIMENTAL_CHROME_ANDROID_ASC = "experimental_chrome_android_asc"
    EXPERIMENTAL_CHROME_ANDROID_DESC = "experimental_chrome_android_desc"
    EXPERIMENTAL_FIREFOX_ANDROID_ASC = "experimental_firefox_android_asc"
    EXPERIMENTAL_FIREFOX_ANDROID_DESC = "experimental_firefox_android_desc"
    EXPERIMENTAL_SAFARI_IOS_ASC = "experimental_safari_ios_asc"
    EXPERIMENTAL_SAFARI_IOS_DESC = "experimental_safari_ios_desc"
    CHROME_USAGE_ASC = "chrome_usage_asc"
    CHROME_USAGE_DESC = "chrome_usage_desc"
    DEVELOPER_SIGNAL_UPVOTES_ASC = "developer_signal_upvotes_asc"
    DEVELOPER_SIGNAL_UPVOTES_DESC = "developer_signal_upvotes_desc"
    AVAILABILITY_CHROME_ASC = "availability_chrome_asc"
    AVAILABILITY_CHROME_DESC = "availability_chrome_desc"
    AVAILABILITY_EDGE_ASC = "availability_edge_asc"
    AVAILABILITY_EDGE_DESC = "availability_edge_desc"
    AVAILABILITY_FIREFOX_ASC = "availability_firefox_asc"
    AVAILABILITY_FIREFOX_DESC = "availability_firefox_desc"
    AVAILABILITY_SAFARI_ASC = "availability_safari_asc"
    AVAILABILITY_SAFARI_DESC = "availability_safari_desc"
    AVAILABILITY_CHROME_ANDROID_ASC = "availability_chrome_android_asc"
    AVAILABILITY_CHROME_ANDROID_DESC = "availability_chrome_android_desc"
    AVAILABILITY_FIREFOX_ANDROID_ASC = "availability_firefox_android_asc"
    AVAILABILITY_FIREFOX_ANDROID_DESC = "availability_firefox_android_desc"
    AVAILABILITY_SAFARI_IOS_ASC = "availability_safari_ios_asc"
    AVAILABILITY_SAFARI_IOS_DESC = "availability_safari_ios_desc"

    def visit(
        self,
        name_asc: typing.Callable[[], T_Result],
        name_desc: typing.Callable[[], T_Result],
        baseline_status_asc: typing.Callable[[], T_Result],
        baseline_status_desc: typing.Callable[[], T_Result],
        stable_chrome_asc: typing.Callable[[], T_Result],
        stable_chrome_desc: typing.Callable[[], T_Result],
        stable_safari_asc: typing.Callable[[], T_Result],
        stable_safari_desc: typing.Callable[[], T_Result],
        stable_edge_asc: typing.Callable[[], T_Result],
        stable_edge_desc: typing.Callable[[], T_Result],
        stable_firefox_asc: typing.Callable[[], T_Result],
        stable_firefox_desc: typing.Callable[[], T_Result],
        stable_chrome_android_asc: typing.Callable[[], T_Result],
        stable_chrome_android_desc: typing.Callable[[], T_Result],
        stable_firefox_android_asc: typing.Callable[[], T_Result],
        stable_firefox_android_desc: typing.Callable[[], T_Result],
        stable_safari_ios_asc: typing.Callable[[], T_Result],
        stable_safari_ios_desc: typing.Callable[[], T_Result],
        experimental_chrome_asc: typing.Callable[[], T_Result],
        experimental_chrome_desc: typing.Callable[[], T_Result],
        experimental_safari_asc: typing.Callable[[], T_Result],
        experimental_safari_desc: typing.Callable[[], T_Result],
        experimental_edge_asc: typing.Callable[[], T_Result],
        experimental_edge_desc: typing.Callable[[], T_Result],
        experimental_firefox_asc: typing.Callable[[], T_Result],
        experimental_firefox_desc: typing.Callable[[], T_Result],
        experimental_chrome_android_asc: typing.Callable[[], T_Result],
        experimental_chrome_android_desc: typing.Callable[[], T_Result],
        experimental_firefox_android_asc: typing.Callable[[], T_Result],
        experimental_firefox_android_desc: typing.Callable[[], T_Result],
        experimental_safari_ios_asc: typing.Callable[[], T_Result],
        experimental_safari_ios_desc: typing.Callable[[], T_Result],
        chrome_usage_asc: typing.Callable[[], T_Result],
        chrome_usage_desc: typing.Callable[[], T_Result],
        developer_signal_upvotes_asc: typing.Callable[[], T_Result],
        developer_signal_upvotes_desc: typing.Callable[[], T_Result],
        availability_chrome_asc: typing.Callable[[], T_Result],
        availability_chrome_desc: typing.Callable[[], T_Result],
        availability_edge_asc: typing.Callable[[], T_Result],
        availability_edge_desc: typing.Callable[[], T_Result],
        availability_firefox_asc: typing.Callable[[], T_Result],
        availability_firefox_desc: typing.Callable[[], T_Result],
        availability_safari_asc: typing.Callable[[], T_Result],
        availability_safari_desc: typing.Callable[[], T_Result],
        availability_chrome_android_asc: typing.Callable[[], T_Result],
        availability_chrome_android_desc: typing.Callable[[], T_Result],
        availability_firefox_android_asc: typing.Callable[[], T_Result],
        availability_firefox_android_desc: typing.Callable[[], T_Result],
        availability_safari_ios_asc: typing.Callable[[], T_Result],
        availability_safari_ios_desc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListFeaturesRequestSort.NAME_ASC:
            return name_asc()
        if self is ListFeaturesRequestSort.NAME_DESC:
            return name_desc()
        if self is ListFeaturesRequestSort.BASELINE_STATUS_ASC:
            return baseline_status_asc()
        if self is ListFeaturesRequestSort.BASELINE_STATUS_DESC:
            return baseline_status_desc()
        if self is ListFeaturesRequestSort.STABLE_CHROME_ASC:
            return stable_chrome_asc()
        if self is ListFeaturesRequestSort.STABLE_CHROME_DESC:
            return stable_chrome_desc()
        if self is ListFeaturesRequestSort.STABLE_SAFARI_ASC:
            return stable_safari_asc()
        if self is ListFeaturesRequestSort.STABLE_SAFARI_DESC:
            return stable_safari_desc()
        if self is ListFeaturesRequestSort.STABLE_EDGE_ASC:
            return stable_edge_asc()
        if self is ListFeaturesRequestSort.STABLE_EDGE_DESC:
            return stable_edge_desc()
        if self is ListFeaturesRequestSort.STABLE_FIREFOX_ASC:
            return stable_firefox_asc()
        if self is ListFeaturesRequestSort.STABLE_FIREFOX_DESC:
            return stable_firefox_desc()
        if self is ListFeaturesRequestSort.STABLE_CHROME_ANDROID_ASC:
            return stable_chrome_android_asc()
        if self is ListFeaturesRequestSort.STABLE_CHROME_ANDROID_DESC:
            return stable_chrome_android_desc()
        if self is ListFeaturesRequestSort.STABLE_FIREFOX_ANDROID_ASC:
            return stable_firefox_android_asc()
        if self is ListFeaturesRequestSort.STABLE_FIREFOX_ANDROID_DESC:
            return stable_firefox_android_desc()
        if self is ListFeaturesRequestSort.STABLE_SAFARI_IOS_ASC:
            return stable_safari_ios_asc()
        if self is ListFeaturesRequestSort.STABLE_SAFARI_IOS_DESC:
            return stable_safari_ios_desc()
        if self is ListFeaturesRequestSort.EXPERIMENTAL_CHROME_ASC:
            return experimental_chrome_asc()
        if self is ListFeaturesRequestSort.EXPERIMENTAL_CHROME_DESC:
            return experimental_chrome_desc()
        if self is ListFeaturesRequestSort.EXPERIMENTAL_SAFARI_ASC:
            return experimental_safari_asc()
        if self is ListFeaturesRequestSort.EXPERIMENTAL_SAFARI_DESC:
            return experimental_safari_desc()
        if self is ListFeaturesRequestSort.EXPERIMENTAL_EDGE_ASC:
            return experimental_edge_asc()
        if self is ListFeaturesRequestSort.EXPERIMENTAL_EDGE_DESC:
            return experimental_edge_desc()
        if self is ListFeaturesRequestSort.EXPERIMENTAL_FIREFOX_ASC:
            return experimental_firefox_asc()
        if self is ListFeaturesRequestSort.EXPERIMENTAL_FIREFOX_DESC:
            return experimental_firefox_desc()
        if self is ListFeaturesRequestSort.EXPERIMENTAL_CHROME_ANDROID_ASC:
            return experimental_chrome_android_asc()
        if self is ListFeaturesRequestSort.EXPERIMENTAL_CHROME_ANDROID_DESC:
            return experimental_chrome_android_desc()
        if self is ListFeaturesRequestSort.EXPERIMENTAL_FIREFOX_ANDROID_ASC:
            return experimental_firefox_android_asc()
        if self is ListFeaturesRequestSort.EXPERIMENTAL_FIREFOX_ANDROID_DESC:
            return experimental_firefox_android_desc()
        if self is ListFeaturesRequestSort.EXPERIMENTAL_SAFARI_IOS_ASC:
            return experimental_safari_ios_asc()
        if self is ListFeaturesRequestSort.EXPERIMENTAL_SAFARI_IOS_DESC:
            return experimental_safari_ios_desc()
        if self is ListFeaturesRequestSort.CHROME_USAGE_ASC:
            return chrome_usage_asc()
        if self is ListFeaturesRequestSort.CHROME_USAGE_DESC:
            return chrome_usage_desc()
        if self is ListFeaturesRequestSort.DEVELOPER_SIGNAL_UPVOTES_ASC:
            return developer_signal_upvotes_asc()
        if self is ListFeaturesRequestSort.DEVELOPER_SIGNAL_UPVOTES_DESC:
            return developer_signal_upvotes_desc()
        if self is ListFeaturesRequestSort.AVAILABILITY_CHROME_ASC:
            return availability_chrome_asc()
        if self is ListFeaturesRequestSort.AVAILABILITY_CHROME_DESC:
            return availability_chrome_desc()
        if self is ListFeaturesRequestSort.AVAILABILITY_EDGE_ASC:
            return availability_edge_asc()
        if self is ListFeaturesRequestSort.AVAILABILITY_EDGE_DESC:
            return availability_edge_desc()
        if self is ListFeaturesRequestSort.AVAILABILITY_FIREFOX_ASC:
            return availability_firefox_asc()
        if self is ListFeaturesRequestSort.AVAILABILITY_FIREFOX_DESC:
            return availability_firefox_desc()
        if self is ListFeaturesRequestSort.AVAILABILITY_SAFARI_ASC:
            return availability_safari_asc()
        if self is ListFeaturesRequestSort.AVAILABILITY_SAFARI_DESC:
            return availability_safari_desc()
        if self is ListFeaturesRequestSort.AVAILABILITY_CHROME_ANDROID_ASC:
            return availability_chrome_android_asc()
        if self is ListFeaturesRequestSort.AVAILABILITY_CHROME_ANDROID_DESC:
            return availability_chrome_android_desc()
        if self is ListFeaturesRequestSort.AVAILABILITY_FIREFOX_ANDROID_ASC:
            return availability_firefox_android_asc()
        if self is ListFeaturesRequestSort.AVAILABILITY_FIREFOX_ANDROID_DESC:
            return availability_firefox_android_desc()
        if self is ListFeaturesRequestSort.AVAILABILITY_SAFARI_IOS_ASC:
            return availability_safari_ios_asc()
        if self is ListFeaturesRequestSort.AVAILABILITY_SAFARI_IOS_DESC:
            return availability_safari_ios_desc()
