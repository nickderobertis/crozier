

import typing

from .app_config import AppConfig
from .page import Page
from .page_info import PageInfo
from .section import Section

KeyValue = typing.Union[PageInfo, AppConfig, typing.List[Section], typing.List[Page]]
