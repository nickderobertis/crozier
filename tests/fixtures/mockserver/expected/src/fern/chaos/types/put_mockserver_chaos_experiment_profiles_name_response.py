

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .put_mockserver_chaos_experiment_profiles_name_response_status import (
    PutMockserverChaosExperimentProfilesNameResponseStatus,
)


class PutMockserverChaosExperimentProfilesNameResponse(UniversalBaseModel):
    status: typing.Optional[PutMockserverChaosExperimentProfilesNameResponseStatus] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
