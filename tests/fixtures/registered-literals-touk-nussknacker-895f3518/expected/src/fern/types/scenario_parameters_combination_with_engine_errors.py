

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .map_engine_setup_name_list_string import MapEngineSetupNameListString
from .scenario_parameters import ScenarioParameters


class ScenarioParametersCombinationWithEngineErrors(UniversalBaseModel):
    combinations: typing.Optional[typing.List[ScenarioParameters]] = None
    engine_setup_errors: typing_extensions.Annotated[
        MapEngineSetupNameListString,
        FieldMetadata(alias="engineSetupErrors"),
        pydantic.Field(alias="engineSetupErrors"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
