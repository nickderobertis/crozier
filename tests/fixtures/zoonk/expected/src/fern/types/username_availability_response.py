

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UsernameAvailabilityResponse(UniversalBaseModel):
    is_available: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isAvailable"),
        pydantic.Field(
            alias="isAvailable",
            description="Whether the username currently passes the reserved-name and uniqueness policies",
        ),
    ]
    """
    Whether the username currently passes the reserved-name and uniqueness policies
    """

    username: str = pydantic.Field()
    """
    Normalized username candidate
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
