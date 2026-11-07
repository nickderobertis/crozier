

import typing

from ...types.appearance import Appearance
from ...types.appearance_table import AppearanceTable
from ...types.chunk_address import ChunkAddress
from ...types.chunk_bloom import ChunkBloom
from ...types.chunk_index import ChunkIndex
from ...types.chunk_pin import ChunkPin
from ...types.chunk_record import ChunkRecord
from ...types.chunk_stats import ChunkStats
from ...types.count import Count
from ...types.ipfs_pin import IpfsPin
from ...types.manifest import Manifest
from ...types.message import Message
from ...types.range_dates import RangeDates
from ...types.report_check import ReportCheck

AdminChunksResponseDataItem = typing.Union[
    Appearance,
    AppearanceTable,
    ChunkAddress,
    ChunkBloom,
    ChunkIndex,
    ChunkPin,
    ChunkRecord,
    ChunkStats,
    Count,
    IpfsPin,
    Manifest,
    Message,
    RangeDates,
    ReportCheck,
]
