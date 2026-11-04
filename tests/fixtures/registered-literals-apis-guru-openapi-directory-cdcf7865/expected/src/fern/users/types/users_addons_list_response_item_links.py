

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class UsersAddonsListResponseItemLinks(UniversalBaseModel):
    """
    URLs to alternative representations of the user addon entity.
    """

    accounts: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    A dictionary with addon_account id as key, an array of connected nodes and link to user account as value
    """

    self_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="self"),
        pydantic.Field(alias="self", description="The canonical API endpoint to this user addon."),
    ] = None
    """
    The canonical API endpoint to this user addon.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
