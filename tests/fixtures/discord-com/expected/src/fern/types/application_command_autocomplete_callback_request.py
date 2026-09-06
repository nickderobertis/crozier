

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_command_autocomplete_callback_request_data import ApplicationCommandAutocompleteCallbackRequestData


class ApplicationCommandAutocompleteCallbackRequest(UniversalBaseModel):
    type: int
    data: ApplicationCommandAutocompleteCallbackRequestData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
