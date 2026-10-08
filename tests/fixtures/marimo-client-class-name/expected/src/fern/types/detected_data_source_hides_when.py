

import typing

from .dialect_hides_when import DialectHidesWhen
from .storage_hides_when import StorageHidesWhen

DetectedDataSourceHidesWhen = typing.Union[DialectHidesWhen, StorageHidesWhen]
