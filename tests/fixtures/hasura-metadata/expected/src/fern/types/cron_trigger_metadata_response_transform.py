

import typing

from .response_transform_v1 import ResponseTransformV1
from .response_transform_v2 import ResponseTransformV2

CronTriggerMetadataResponseTransform = typing.Union[ResponseTransformV1, ResponseTransformV2]
