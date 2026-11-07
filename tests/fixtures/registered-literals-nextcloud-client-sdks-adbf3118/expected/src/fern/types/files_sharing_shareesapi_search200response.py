

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .files_sharing_shareesapi_search200response_ocs import FilesSharingShareesapiSearch200ResponseOcs


class FilesSharingShareesapiSearch200Response(UniversalBaseModel):
    ocs: FilesSharingShareesapiSearch200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
