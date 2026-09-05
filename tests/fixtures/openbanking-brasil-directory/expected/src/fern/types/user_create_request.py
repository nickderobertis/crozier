

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UserCreateRequest(UniversalBaseModel):
    terms_and_conditions_id: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="TermsAndConditionsId"),
        pydantic.Field(alias="TermsAndConditionsId", description="Id of the TnC(type = Directory), user has agreed to"),
    ]
    """
    Id of the TnC(type = Directory), user has agreed to
    """

    user_email: typing_extensions.Annotated[
        str, FieldMetadata(alias="UserEmail"), pydantic.Field(alias="UserEmail", description="User's email")
    ]
    """
    User's email
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
