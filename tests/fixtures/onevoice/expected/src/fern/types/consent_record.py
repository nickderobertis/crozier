

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ConsentRecord(UniversalBaseModel):
    """
    Per-policy consent ledger row returned by GET /users/me/consents.
    `withdrawnAt` is optional (`omitempty`): the field is OMITTED from
    the JSON envelope when the row is active. Frontend treats a missing
    `withdrawnAt` as "consent still in force". `sha256` is also optional
    (early ledger rows may not carry the policy hash).
    """

    slug: str
    version: str
    sha256: typing.Optional[str] = None
    accepted_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="acceptedAt"), pydantic.Field(alias="acceptedAt")
    ]
    withdrawn_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="withdrawnAt"), pydantic.Field(alias="withdrawnAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
