

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .deployment import Deployment
from .gen_ai_params import GenAiParams
from .project_data_index_conversion_settings_output import ProjectDataIndexConversionSettingsOutput


class SystemInfo(UniversalBaseModel):
    notifications: typing.List[typing.Any]
    default_project: typing.Dict[str, typing.Any]
    deployment: Deployment
    toolkit: typing.Dict[str, typing.Any]
    allow_non_admins_to_make_resources_public: bool
    api: typing.Dict[str, typing.Any]
    genai_defaults: typing.Dict[str, GenAiParams]
    conversion_settings_defaults: typing.Optional[ProjectDataIndexConversionSettingsOutput] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
