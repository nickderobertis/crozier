

import typing

from ...types.profiling_operation_spec import ProfilingOperationSpec
from ...types.tracing_operation_spec import TracingOperationSpec

StartOperationRequestSpec = typing.Union[ProfilingOperationSpec, TracingOperationSpec]
