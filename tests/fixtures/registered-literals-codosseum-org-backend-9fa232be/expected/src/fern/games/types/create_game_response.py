

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class CreateGameResponse(UniversalBaseModel):
    admin_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="adminKey"),
        pydantic.Field(alias="adminKey", description="Key to manage the game and participate"),
    ] = None
    """
    Key to manage the game and participate
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the newly created game
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
