

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .access_token_id_response import AccessTokenIdResponse


class AccessTokenIdListResponse(UniversalBaseModel):
    access_token_id_array: typing_extensions.Annotated[
        typing.List[AccessTokenIdResponse],
        FieldMetadata(alias="AccessTokenIdArray"),
        pydantic.Field(alias="AccessTokenIdArray", description="Array of access tokens Id."),
    ]
    """
    Array of access tokens Id.
    """

    object: str = pydantic.Field()
    """
    Name of the object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
