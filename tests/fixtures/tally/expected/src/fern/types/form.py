

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .form_payments_item import FormPaymentsItem
from .form_status import FormStatus


class Form(UniversalBaseModel):
    id: str
    name: str
    workspace_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ]
    status: FormStatus
    number_of_submissions: typing_extensions.Annotated[
        float, FieldMetadata(alias="numberOfSubmissions"), pydantic.Field(alias="numberOfSubmissions")
    ]
    is_closed: typing_extensions.Annotated[bool, FieldMetadata(alias="isClosed"), pydantic.Field(alias="isClosed")]
    payments: typing.Optional[typing.List[FormPaymentsItem]] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
