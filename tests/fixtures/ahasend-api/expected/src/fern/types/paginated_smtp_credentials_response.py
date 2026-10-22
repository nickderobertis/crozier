

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .paginated_smtp_credentials_response_object import PaginatedSmtpCredentialsResponseObject
from .pagination_info import PaginationInfo
from .smtp_credential import SmtpCredential


class PaginatedSmtpCredentialsResponse(UniversalBaseModel):
    object: PaginatedSmtpCredentialsResponseObject = pydantic.Field()
    """
    Object type identifier
    """

    data: typing.List[SmtpCredential] = pydantic.Field()
    """
    Array of SMTP credentials
    """

    pagination: PaginationInfo

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
