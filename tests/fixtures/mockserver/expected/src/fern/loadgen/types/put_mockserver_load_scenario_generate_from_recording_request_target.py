

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .put_mockserver_load_scenario_generate_from_recording_request_target_scheme import (
    PutMockserverLoadScenarioGenerateFromRecordingRequestTargetScheme,
)


class PutMockserverLoadScenarioGenerateFromRecordingRequestTarget(UniversalBaseModel):
    """
    explicit network target applied to every generated step (overrides each recorded request's own Host/secure routing)
    """

    host: typing.Optional[str] = None
    port: typing.Optional[int] = None
    scheme: typing.Optional[PutMockserverLoadScenarioGenerateFromRecordingRequestTargetScheme] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
