

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_custom_hostname_response_output_data_result_ownership_verification import (
    UpdateCustomHostnameResponseOutputDataResultOwnershipVerification,
)
from .update_custom_hostname_response_output_data_result_ssl import UpdateCustomHostnameResponseOutputDataResultSsl


class UpdateCustomHostnameResponseOutputDataResult(UniversalBaseModel):
    id: str
    hostname: str
    ssl: typing.Optional[UpdateCustomHostnameResponseOutputDataResultSsl] = None
    ownership_verification: typing.Optional[UpdateCustomHostnameResponseOutputDataResultOwnershipVerification] = None
    custom_origin_server: typing.Optional[str] = None
    verification_errors: typing.Optional[typing.List[str]] = None
    status: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
