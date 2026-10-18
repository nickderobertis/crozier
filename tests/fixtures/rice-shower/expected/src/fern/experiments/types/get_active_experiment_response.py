

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_active_experiment_response_experiment import GetActiveExperimentResponseExperiment


class GetActiveExperimentResponse(UniversalBaseModel):
    experiment: typing.Optional[GetActiveExperimentResponseExperiment] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
