

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fine_tuning_integration_type import FineTuningIntegrationType
from .fine_tuning_integration_wandb import FineTuningIntegrationWandb


class FineTuningIntegration(UniversalBaseModel):
    type: FineTuningIntegrationType = pydantic.Field()
    """
    The type of the integration being enabled for the fine-tuning job
    """

    wandb: FineTuningIntegrationWandb = pydantic.Field()
    """
    The settings for your integration with Weights and Biases. This payload specifies the project that
    metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
    to your run, and set a default entity (team, username, etc) to be associated with your run.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
