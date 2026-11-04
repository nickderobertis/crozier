

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .client_profile import ClientProfile
from .hashed_dir import HashedDir


class CompletedProfile(UniversalBaseModel):
    """
    A fully resolved profile with client and asset directory hashes.
    """

    profile: ClientProfile
    client_dir: typing_extensions.Annotated[
        HashedDir, FieldMetadata(alias="clientDir"), pydantic.Field(alias="clientDir")
    ]
    asset_dir: typing_extensions.Annotated[HashedDir, FieldMetadata(alias="assetDir"), pydantic.Field(alias="assetDir")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
