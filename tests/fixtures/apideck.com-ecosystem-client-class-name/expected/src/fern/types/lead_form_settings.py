

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LeadFormSettings(UniversalBaseModel):
    capture_form_enabled: typing.Optional[bool] = None
    first_name_field_enabled: typing.Optional[bool] = None
    first_name_field_required: typing.Optional[bool] = None
    integration_enabled: typing.Optional[bool] = None
    last_name_field_enabled: typing.Optional[bool] = None
    last_name_field_required: typing.Optional[bool] = None
    telephone_field_enabled: typing.Optional[bool] = None
    telephone_field_required: typing.Optional[bool] = None
    work_email_validation: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
