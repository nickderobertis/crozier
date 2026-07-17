

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .put_listings_slug_request_condition_uuid import PutListingsSlugRequestConditionUuid


class PutListingsSlugRequestCondition(UniversalBaseModel):
    """
    Condition
    """

    uuid_: typing_extensions.Annotated[
        PutListingsSlugRequestConditionUuid,
        FieldMetadata(alias="uuid"),
        pydantic.Field(alias="uuid", description="Condition UUID"),
    ]
    """
    Condition UUID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
