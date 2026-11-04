

import typing

from ...types.manual_gpu_selection import ManualGpuSelection
from .deploy_request_gpu_selection_one import DeployRequestGpuSelectionOne

DeployRequestGpuSelection = typing.Union[ManualGpuSelection, DeployRequestGpuSelectionOne]
