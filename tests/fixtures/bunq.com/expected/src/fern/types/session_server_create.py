

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bunq_id import BunqId
from .session_server_token import SessionServerToken
from .user_api_key import UserApiKey
from .user_company import UserCompany
from .user_payment_service_provider import UserPaymentServiceProvider
from .user_person import UserPerson


class SessionServerCreate(UniversalBaseModel):
    id: typing_extensions.Annotated[
        typing.Optional[BunqId],
        FieldMetadata(alias="Id"),
        pydantic.Field(alias="Id", description="The Id object of the created Session."),
    ] = None
    """
    The Id object of the created Session.
    """

    token: typing_extensions.Annotated[
        typing.Optional[SessionServerToken],
        FieldMetadata(alias="Token"),
        pydantic.Field(alias="Token", description="The token object of this Session."),
    ] = None
    """
    The token object of this Session.
    """

    user_api_key: typing_extensions.Annotated[
        typing.Optional[UserApiKey],
        FieldMetadata(alias="UserApiKey"),
        pydantic.Field(alias="UserApiKey", description="The UserApiKey object that is logged in with this Session."),
    ] = None
    """
    The UserApiKey object that is logged in with this Session.
    """

    user_company: typing_extensions.Annotated[
        typing.Optional[UserCompany],
        FieldMetadata(alias="UserCompany"),
        pydantic.Field(alias="UserCompany", description="The UserCompany object that is logged in with this Session."),
    ] = None
    """
    The UserCompany object that is logged in with this Session.
    """

    user_payment_service_provider: typing_extensions.Annotated[
        typing.Optional[UserPaymentServiceProvider],
        FieldMetadata(alias="UserPaymentServiceProvider"),
        pydantic.Field(
            alias="UserPaymentServiceProvider",
            description="The UserPaymentServiceProvider object that is logged in with this Session.",
        ),
    ] = None
    """
    The UserPaymentServiceProvider object that is logged in with this Session.
    """

    user_person: typing_extensions.Annotated[
        typing.Optional[UserPerson],
        FieldMetadata(alias="UserPerson"),
        pydantic.Field(alias="UserPerson", description="The UserPerson object that is logged in with this Session."),
    ] = None
    """
    The UserPerson object that is logged in with this Session.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
