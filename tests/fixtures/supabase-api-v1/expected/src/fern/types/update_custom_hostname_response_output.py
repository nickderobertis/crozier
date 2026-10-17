

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_custom_hostname_response_output_data import UpdateCustomHostnameResponseOutputData
from .update_custom_hostname_response_output_status import UpdateCustomHostnameResponseOutputStatus


class UpdateCustomHostnameResponseOutput(UniversalBaseModel):
    status: UpdateCustomHostnameResponseOutputStatus
    custom_hostname: typing.Optional[str] = None
    data: UpdateCustomHostnameResponseOutputData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
