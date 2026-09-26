

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AcquisitionType(enum.StrEnum):
    """
    The method to obtain the data.
    """

    API = "API"
    FTP = "FTP"
    DOWNLOAD = "Download"
    LINK = "Link"
    WEB_SCRAPING_CRAWLING = "Web scraping/Crawling"
    OTHER = "Other"

    def visit(
        self,
        api: typing.Callable[[], T_Result],
        ftp: typing.Callable[[], T_Result],
        download: typing.Callable[[], T_Result],
        link: typing.Callable[[], T_Result],
        web_scraping_crawling: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AcquisitionType.API:
            return api()
        if self is AcquisitionType.FTP:
            return ftp()
        if self is AcquisitionType.DOWNLOAD:
            return download()
        if self is AcquisitionType.LINK:
            return link()
        if self is AcquisitionType.WEB_SCRAPING_CRAWLING:
            return web_scraping_crawling()
        if self is AcquisitionType.OTHER:
            return other()
