

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Business(UniversalBaseModel):
    has_first_successful_action: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasFirstSuccessfulAction"),
        pydantic.Field(
            alias="hasFirstSuccessfulAction",
            description="Whether the organization has a persisted completed platform tool task or text-only assistant answer with an explicit successful outcome across its entire history, or a successfully generated review draft or confirmed review reply dispatch. Imported replies and ambiguous review attempts do not count. Ambiguous historical turns do not count; organization ID backfills never assign success. Authoritative on GET business profile.",
        ),
    ] = None
    """
    Whether the organization has a persisted completed platform tool task or text-only assistant answer with an explicit successful outcome across its entire history, or a successfully generated review draft or confirmed review reply dispatch. Imported replies and ambiguous review attempts do not count. Ambiguous historical turns do not count; organization ID backfills never assign success. Authoritative on GET business profile.
    """

    id: str
    name: str
    category: typing.Optional[str] = None
    address: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    website: typing.Optional[str] = None
    description: typing.Optional[str] = None
    logo_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="logoUrl"), pydantic.Field(alias="logoUrl")
    ] = None
    settings: typing.Dict[str, typing.Any]
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
