

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommonCommonUnifiedFields(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The unique `id` of this object in Revert
    """

    remote_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="remoteId"),
        pydantic.Field(alias="remoteId", description="The unique `id` of this object in the downstream CRM."),
    ]
    """
    The unique `id` of this object in the downstream CRM.
    """

    created_timestamp: typing_extensions.Annotated[
        typing.Any, FieldMetadata(alias="createdTimestamp"), pydantic.Field(alias="createdTimestamp")
    ]
    updated_timestamp: typing_extensions.Annotated[
        typing.Any, FieldMetadata(alias="updatedTimestamp"), pydantic.Field(alias="updatedTimestamp")
    ]
    additional: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Any fields that are not unified yet/non-unifiable come inside this `json` object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
