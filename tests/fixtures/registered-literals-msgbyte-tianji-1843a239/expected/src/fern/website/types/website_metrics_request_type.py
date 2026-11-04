

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class WebsiteMetricsRequestType(enum.StrEnum):
    URL = "url"
    LANGUAGE = "language"
    REFERRER = "referrer"
    TITLE = "title"
    BROWSER = "browser"
    OS = "os"
    DEVICE = "device"
    COUNTRY = "country"
    EVENT = "event"
    UTM_SOURCE = "utm_source"
    UTM_MEDIUM = "utm_medium"
    UTM_CAMPAIGN = "utm_campaign"
    UTM_TERM = "utm_term"
    UTM_CONTENT = "utm_content"

    def visit(
        self,
        url: typing.Callable[[], T_Result],
        language: typing.Callable[[], T_Result],
        referrer: typing.Callable[[], T_Result],
        title: typing.Callable[[], T_Result],
        browser: typing.Callable[[], T_Result],
        os: typing.Callable[[], T_Result],
        device: typing.Callable[[], T_Result],
        country: typing.Callable[[], T_Result],
        event: typing.Callable[[], T_Result],
        utm_source: typing.Callable[[], T_Result],
        utm_medium: typing.Callable[[], T_Result],
        utm_campaign: typing.Callable[[], T_Result],
        utm_term: typing.Callable[[], T_Result],
        utm_content: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebsiteMetricsRequestType.URL:
            return url()
        if self is WebsiteMetricsRequestType.LANGUAGE:
            return language()
        if self is WebsiteMetricsRequestType.REFERRER:
            return referrer()
        if self is WebsiteMetricsRequestType.TITLE:
            return title()
        if self is WebsiteMetricsRequestType.BROWSER:
            return browser()
        if self is WebsiteMetricsRequestType.OS:
            return os()
        if self is WebsiteMetricsRequestType.DEVICE:
            return device()
        if self is WebsiteMetricsRequestType.COUNTRY:
            return country()
        if self is WebsiteMetricsRequestType.EVENT:
            return event()
        if self is WebsiteMetricsRequestType.UTM_SOURCE:
            return utm_source()
        if self is WebsiteMetricsRequestType.UTM_MEDIUM:
            return utm_medium()
        if self is WebsiteMetricsRequestType.UTM_CAMPAIGN:
            return utm_campaign()
        if self is WebsiteMetricsRequestType.UTM_TERM:
            return utm_term()
        if self is WebsiteMetricsRequestType.UTM_CONTENT:
            return utm_content()
