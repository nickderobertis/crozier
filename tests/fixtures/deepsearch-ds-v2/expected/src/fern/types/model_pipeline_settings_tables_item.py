

import typing

from .direct_model_config import DirectModelConfig
from .reference_to_model import ReferenceToModel

ModelPipelineSettingsTablesItem = typing.Union[ReferenceToModel, DirectModelConfig]
