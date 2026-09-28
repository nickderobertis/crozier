

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chaos_experiment_stages_item import ChaosExperimentStagesItem


class ChaosExperiment(UniversalBaseModel):
    """
    a scheduled multi-stage chaos experiment definition (the body of PUT /mockserver/chaosExperiment)
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    human-readable experiment name (ignored when saved under a path {name})
    """

    loop: typing.Optional[bool] = pydantic.Field(default=None)
    """
    whether to loop back to stage 0 after the last stage completes (default false)
    """

    stages: typing.List[ChaosExperimentStagesItem] = pydantic.Field()
    """
    ordered sequence of stages
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
