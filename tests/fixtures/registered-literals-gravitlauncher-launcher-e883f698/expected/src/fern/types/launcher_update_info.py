

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LauncherUpdateInfo(UniversalBaseModel):
    url: str = pydantic.Field()
    """
    URL from which the updated launcher binary can be downloaded.
    """

    version: str = pydantic.Field()
    """
    Version string of the available update.
    """

    available: bool = pydantic.Field()
    """
    Whether an update is available.
    """

    required: bool = pydantic.Field()
    """
    Whether the update is mandatory and the launcher must update before continuing.
    """

    jwt_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="jwtToken"),
        pydantic.Field(alias="jwtToken", description="Verify token for /auth/authorize (X-Launcher-Update-Token)"),
    ] = None
    """
    Verify token for /auth/authorize (X-Launcher-Update-Token)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
