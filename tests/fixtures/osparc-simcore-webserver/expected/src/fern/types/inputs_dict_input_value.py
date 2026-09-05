

import typing

from .dat_core_file_link import DatCoreFileLink
from .download_link import DownloadLink
from .port_link import PortLink
from .sim_core_file_link import SimCoreFileLink

InputsDictInputValue = typing.Union[
    bool,
    int,
    float,
    str,
    PortLink,
    SimCoreFileLink,
    DatCoreFileLink,
    DownloadLink,
    typing.List[typing.Any],
    typing.Dict[str, typing.Any],
]
