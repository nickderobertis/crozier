

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_company import UserCompany
from .user_payment_service_provider import UserPaymentServiceProvider
from .user_person import UserPerson


class UserApiKeyAnchoredUser(UniversalBaseModel):
    user_company: typing_extensions.Annotated[
        typing.Optional[UserCompany],
        FieldMetadata(alias="UserCompany"),
        pydantic.Field(alias="UserCompany", description=""),
    ] = None
    """
    
    """

    user_payment_service_provider: typing_extensions.Annotated[
        typing.Optional[UserPaymentServiceProvider],
        FieldMetadata(alias="UserPaymentServiceProvider"),
        pydantic.Field(alias="UserPaymentServiceProvider", description=""),
    ] = None
    """
    
    """

    user_person: typing_extensions.Annotated[
        typing.Optional[UserPerson],
        FieldMetadata(alias="UserPerson"),
        pydantic.Field(alias="UserPerson", description=""),
    ] = None
    """
    
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
