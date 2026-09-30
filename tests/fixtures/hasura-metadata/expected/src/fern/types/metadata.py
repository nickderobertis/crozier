

import typing

from .metadata_v1 import MetadataV1
from .metadata_v2 import MetadataV2
from .metadata_v3 import MetadataV3

Metadata = typing.Union[MetadataV1, MetadataV2, MetadataV3]
