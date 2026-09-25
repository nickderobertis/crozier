

import typing

from .direct_model_config import DirectModelConfig
from .reference_to_model import ReferenceToModel

ModelPipelineSettingsClustersItem = typing.Union[ReferenceToModel, DirectModelConfig]
