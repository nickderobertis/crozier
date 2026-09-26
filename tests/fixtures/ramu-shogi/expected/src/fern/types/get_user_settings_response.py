

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_user_settings_response_document import GetUserSettingsResponseDocument


class GetUserSettingsResponse(UniversalBaseModel):
    document: typing.Optional[GetUserSettingsResponseDocument] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
