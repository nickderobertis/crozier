

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AssetOwner(UniversalBaseModel):
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    asset_owner_text: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AssetOwnerText"),
        pydantic.Field(alias="AssetOwnerText", description="Account Owner Full Name."),
    ] = None
    """
    Account Owner Full Name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
