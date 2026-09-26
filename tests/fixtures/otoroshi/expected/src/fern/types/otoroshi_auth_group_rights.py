

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_models_user_rights import OtoroshiModelsUserRights


class OtoroshiAuthGroupRights(UniversalBaseModel):
    """
    ???
    """

    user_rights: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsUserRights],
        FieldMetadata(alias="userRights"),
        pydantic.Field(alias="userRights", description="???"),
    ] = None
    """
    ???
    """

    users: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    ???
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
