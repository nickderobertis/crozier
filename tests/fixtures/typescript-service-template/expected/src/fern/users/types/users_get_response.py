

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.user import User


class UsersGetResponse(UniversalBaseModel):
    users: typing.List[User]
    next_page_cursor: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextPageCursor"),
        pydantic.Field(alias="nextPageCursor", description="Use to fetch the next page"),
    ] = None
    """
    Use to fetch the next page
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
