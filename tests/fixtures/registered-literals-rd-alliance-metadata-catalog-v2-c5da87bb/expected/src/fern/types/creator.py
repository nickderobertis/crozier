

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Creator(UniversalBaseModel):
    full_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fullName"),
        pydantic.Field(
            alias="fullName",
            description="Full name. If absent, a concatenation of the `givenName` and `familyName` will be used for display.",
        ),
    ] = None
    """
    Full name. If absent, a concatenation of the `givenName` and `familyName` will be used for display.
    """

    given_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="givenName"),
        pydantic.Field(alias="givenName", description="Given name(s)"),
    ] = None
    """
    Given name(s)
    """

    family_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="familyName"),
        pydantic.Field(alias="familyName", description="Family name"),
    ] = None
    """
    Family name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
