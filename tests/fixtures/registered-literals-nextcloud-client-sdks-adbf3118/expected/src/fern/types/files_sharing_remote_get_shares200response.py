

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .files_sharing_remote_get_shares200response_ocs import FilesSharingRemoteGetShares200ResponseOcs


class FilesSharingRemoteGetShares200Response(UniversalBaseModel):
    ocs: FilesSharingRemoteGetShares200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
