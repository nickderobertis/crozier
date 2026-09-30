

import typing

from .request_transform_v1 import RequestTransformV1
from .request_transform_v2 import RequestTransformV2

CitusEventTriggerConfEventTriggerConfRequestTransform = typing.Union[RequestTransformV1, RequestTransformV2]
