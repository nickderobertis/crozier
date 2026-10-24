

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GoogleOneTapLoginEndpointOutput(UniversalBaseModel):
    requires_email_confirmation: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="requiresEmailConfirmation"),
        pydantic.Field(
            alias="requiresEmailConfirmation", description="Whether the account still requires email confirmation."
        ),
    ]
    """
    Whether the account still requires email confirmation.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email of the signed-in user, if available.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
