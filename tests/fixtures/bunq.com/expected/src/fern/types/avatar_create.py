

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AvatarCreate(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="uuid"),
        pydantic.Field(alias="uuid", description="The UUID of the created avatar."),
    ] = None
    """
    The UUID of the created avatar.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
