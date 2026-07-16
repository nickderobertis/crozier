

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsRecordsDestinyRecordExpirationBlock(UniversalBaseModel):
    """
    If this record has an expiration after which it cannot be earned, this is some information about that expiration.
    """

    description: typing.Optional[str] = None
    has_expiration: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hasExpiration"), pydantic.Field(alias="hasExpiration")
    ] = None
    icon: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
