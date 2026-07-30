

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destination_google_sheets_config import DestinationGoogleSheetsConfig


class DestinationConfigGoogleSheets(UniversalBaseModel):
    google_sheets: DestinationGoogleSheetsConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
