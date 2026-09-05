

import typing

from .node_get import NodeGet
from .node_get_idle import NodeGetIdle
from .node_get_unknown import NodeGetUnknown
from .running_dynamic_service_details import RunningDynamicServiceDetails

EnvelopeUnionNodeGetIdleNodeGetUnknownRunningDynamicServiceDetailsNodeGetData = typing.Union[
    NodeGetIdle, NodeGetUnknown, RunningDynamicServiceDetails, NodeGet
]
