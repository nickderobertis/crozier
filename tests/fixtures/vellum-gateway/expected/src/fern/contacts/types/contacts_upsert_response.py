

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .contacts_upsert_response_contact import ContactsUpsertResponseContact


class ContactsUpsertResponse(UniversalBaseModel):
    ok: bool
    contact: ContactsUpsertResponseContact

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
