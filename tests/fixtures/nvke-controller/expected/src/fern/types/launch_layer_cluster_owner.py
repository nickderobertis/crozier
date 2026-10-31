

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LaunchLayerClusterOwner(UniversalBaseModel):
    """
    The LaunchLayer identity requests are attributed to.
    """

    user_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="userID"),
        pydantic.Field(alias="userID", description="LaunchLayer user ID."),
    ] = None
    """
    LaunchLayer user ID.
    """

    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    LaunchLayer username.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
