

import typing

from .dat_core_file_link import DatCoreFileLink
from .download_link import DownloadLink
from .sim_core_file_link import SimCoreFileLink

OutputsDictOutputValue = typing.Union[
    bool,
    int,
    float,
    typing.Any,
    str,
    SimCoreFileLink,
    DatCoreFileLink,
    DownloadLink,
    typing.List[typing.Any],
    typing.Dict[str, typing.Any],
]
