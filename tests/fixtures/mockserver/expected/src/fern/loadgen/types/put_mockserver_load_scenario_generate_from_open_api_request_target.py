

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .put_mockserver_load_scenario_generate_from_open_api_request_target_scheme import (
    PutMockserverLoadScenarioGenerateFromOpenApiRequestTargetScheme,
)


class PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget(UniversalBaseModel):
    """
    explicit network target for every generated step (overrides the spec's servers[0])
    """

    host: typing.Optional[str] = None
    port: typing.Optional[int] = None
    scheme: typing.Optional[PutMockserverLoadScenarioGenerateFromOpenApiRequestTargetScheme] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
