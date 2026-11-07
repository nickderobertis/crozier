

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .files_sharing_shareapi_get_shares200response_ocs import FilesSharingShareapiGetShares200ResponseOcs


class FilesSharingShareapiGetShares200Response(UniversalBaseModel):
    ocs: FilesSharingShareapiGetShares200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
