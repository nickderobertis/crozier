

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_api_key import UserApiKey
from .user_company import UserCompany
from .user_payment_service_provider import UserPaymentServiceProvider
from .user_person import UserPerson


class UserListing(UniversalBaseModel):
    user_api_key: typing_extensions.Annotated[typing.Optional[UserApiKey], FieldMetadata(alias="UserApiKey")] = (
        pydantic.Field(default=None)
    )
    """
    
    """

    user_company: typing_extensions.Annotated[typing.Optional[UserCompany], FieldMetadata(alias="UserCompany")] = (
        pydantic.Field(default=None)
    )
    """
    
    """

    user_payment_service_provider: typing_extensions.Annotated[
        typing.Optional[UserPaymentServiceProvider], FieldMetadata(alias="UserPaymentServiceProvider")
    ] = pydantic.Field(default=None)
    """
    
    """

    user_person: typing_extensions.Annotated[typing.Optional[UserPerson], FieldMetadata(alias="UserPerson")] = (
        pydantic.Field(default=None)
    )
    """
    
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
