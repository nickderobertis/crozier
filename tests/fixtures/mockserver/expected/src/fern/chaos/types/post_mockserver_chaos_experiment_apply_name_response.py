

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_mockserver_chaos_experiment_apply_name_response_status import (
    PostMockserverChaosExperimentApplyNameResponseStatus,
)


class PostMockserverChaosExperimentApplyNameResponse(UniversalBaseModel):
    status: typing.Optional[PostMockserverChaosExperimentApplyNameResponseStatus] = None
    name: typing.Optional[str] = None
    stages: typing.Optional[int] = None
    loop: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
