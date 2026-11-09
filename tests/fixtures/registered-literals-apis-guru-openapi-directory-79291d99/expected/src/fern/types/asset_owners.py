

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .asset_owner import AssetOwner


class AssetOwners(UniversalBaseModel):
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    asset_owner: typing_extensions.Annotated[
        typing.List[AssetOwner],
        FieldMetadata(alias="ASSET_OWNER"),
        pydantic.Field(alias="ASSET_OWNER", description="Multiple Occurances of Account Owners Full Name up to 4."),
    ]
    """
    Multiple Occurances of Account Owners Full Name up to 4.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
