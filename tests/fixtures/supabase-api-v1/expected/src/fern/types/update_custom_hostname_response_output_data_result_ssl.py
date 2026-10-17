

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_custom_hostname_response_output_data_result_ssl_validation_errors_item import (
    UpdateCustomHostnameResponseOutputDataResultSslValidationErrorsItem,
)
from .update_custom_hostname_response_output_data_result_ssl_validation_records_item import (
    UpdateCustomHostnameResponseOutputDataResultSslValidationRecordsItem,
)


class UpdateCustomHostnameResponseOutputDataResultSsl(UniversalBaseModel):
    status: typing.Optional[str] = None
    validation_records: typing.Optional[
        typing.List[UpdateCustomHostnameResponseOutputDataResultSslValidationRecordsItem]
    ] = None
    validation_errors: typing.Optional[
        typing.List[UpdateCustomHostnameResponseOutputDataResultSslValidationErrorsItem]
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
