

import typing

AcquisitionType = typing.Union[
    typing.Literal["API", "FTP", "Download", "Link", "Web scraping/Crawling", "Other"], typing.Any
]
