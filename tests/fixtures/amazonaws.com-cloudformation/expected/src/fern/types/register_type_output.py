

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RegisterTypeOutput(UniversalBaseModel):
    registration_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="RegistrationToken"),
        pydantic.Field(
            alias="RegistrationToken",
            description="<p>The identifier for this registration request.</p> <p>Use this registration token when calling <code> <a>DescribeTypeRegistration</a> </code>, which returns information about the status and IDs of the extension registration.</p>",
        ),
    ] = None
    """
    <p>The identifier for this registration request.</p> <p>Use this registration token when calling <code> <a>DescribeTypeRegistration</a> </code>, which returns information about the status and IDs of the extension registration.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
