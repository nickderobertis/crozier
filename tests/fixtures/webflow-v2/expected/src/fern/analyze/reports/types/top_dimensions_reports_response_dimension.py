

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class TopDimensionsReportsResponseDimension(enum.StrEnum):
    """
    The dimension whose top values are ranked.
    - `country`: ISO 3166-1 alpha-2 country code (e.g., `US`).
    - `region`: first-level subdivision below country, keyed by ISO 3166-2 code (e.g., `US-CA`, with `name` `California, United States`).
    - `deviceType`: `desktop`, `mobile`, or `tablet`.
    - `os`: operating system name (e.g., `iOS`, `Windows NT`).
    - `browser`: browser name (e.g., `Chrome`, `Safari`).
    - `language`: the visitor's stated language preference (from the `Accept-Language` request header).
    - `locale`: the locale declared on the visited page (the page's `<html lang>` value).
    - `referrer`: referrer domain (e.g., `google.com`).
    - `trafficSource`: traffic source category, keyed by a code: `DN` Direct, `SP` Paid Search, `SO` Organic Search, `CP` Paid Social, `CO` Organic Social, `EM` Email, `RC` Recirculation, `OP` Other Paid, `OT` Other, `AI` Generative AI. `attributeKey` is the code; `name` is the label.
    - `utmCampaign`: `utm_campaign` value.
    - `utmContent`: `utm_content` value.
    - `utmMedium`: `utm_medium` value.
    - `utmSource`: `utm_source` value.
    - `utmTerm`: `utm_term` value.
    - `audienceIds`: Webflow audience identifier. For this dimension, `attributeKey` is the audience ID and `name` is the audience's display name (falling back to the ID if no display name is set).
    """

    COUNTRY = "country"
    REGION = "region"
    DEVICE_TYPE = "deviceType"
    OS = "os"
    BROWSER = "browser"
    LANGUAGE = "language"
    LOCALE = "locale"
    REFERRER = "referrer"
    TRAFFIC_SOURCE = "trafficSource"
    UTM_CAMPAIGN = "utmCampaign"
    UTM_CONTENT = "utmContent"
    UTM_MEDIUM = "utmMedium"
    UTM_SOURCE = "utmSource"
    UTM_TERM = "utmTerm"
    AUDIENCE_IDS = "audienceIds"

    def visit(
        self,
        country: typing.Callable[[], T_Result],
        region: typing.Callable[[], T_Result],
        device_type: typing.Callable[[], T_Result],
        os: typing.Callable[[], T_Result],
        browser: typing.Callable[[], T_Result],
        language: typing.Callable[[], T_Result],
        locale: typing.Callable[[], T_Result],
        referrer: typing.Callable[[], T_Result],
        traffic_source: typing.Callable[[], T_Result],
        utm_campaign: typing.Callable[[], T_Result],
        utm_content: typing.Callable[[], T_Result],
        utm_medium: typing.Callable[[], T_Result],
        utm_source: typing.Callable[[], T_Result],
        utm_term: typing.Callable[[], T_Result],
        audience_ids: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TopDimensionsReportsResponseDimension.COUNTRY:
            return country()
        if self is TopDimensionsReportsResponseDimension.REGION:
            return region()
        if self is TopDimensionsReportsResponseDimension.DEVICE_TYPE:
            return device_type()
        if self is TopDimensionsReportsResponseDimension.OS:
            return os()
        if self is TopDimensionsReportsResponseDimension.BROWSER:
            return browser()
        if self is TopDimensionsReportsResponseDimension.LANGUAGE:
            return language()
        if self is TopDimensionsReportsResponseDimension.LOCALE:
            return locale()
        if self is TopDimensionsReportsResponseDimension.REFERRER:
            return referrer()
        if self is TopDimensionsReportsResponseDimension.TRAFFIC_SOURCE:
            return traffic_source()
        if self is TopDimensionsReportsResponseDimension.UTM_CAMPAIGN:
            return utm_campaign()
        if self is TopDimensionsReportsResponseDimension.UTM_CONTENT:
            return utm_content()
        if self is TopDimensionsReportsResponseDimension.UTM_MEDIUM:
            return utm_medium()
        if self is TopDimensionsReportsResponseDimension.UTM_SOURCE:
            return utm_source()
        if self is TopDimensionsReportsResponseDimension.UTM_TERM:
            return utm_term()
        if self is TopDimensionsReportsResponseDimension.AUDIENCE_IDS:
            return audience_ids()
