

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class UpsertUserRequestIdentification(UniversalBaseModel):
    """
    User identification requires a userId, email or both
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address of the user
    """

    user_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="userId"),
        pydantic.Field(alias="userId", description="Unique identifier for the user in your database"),
    ] = None
    """
    Unique identifier for the user in your database
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
