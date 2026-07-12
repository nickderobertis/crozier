

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Note(UniversalBaseModel):
    active: typing.Optional[bool] = None
    company_id: typing.Optional[str] = None
    contact_id: typing.Optional[str] = None
    content: typing.Optional[str] = None
    created_at: typing.Optional[str] = None
    created_by: typing.Optional[str] = None
    id: typing.Optional[str] = None
    lead_id: typing.Optional[str] = None
    opportunity_id: typing.Optional[str] = None
    owner_id: typing.Optional[str] = None
    title: typing.Optional[str] = None
    updated_at: typing.Optional[str] = None
    updated_by: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
