

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateSystemModelsUpdateGroupClientRelationship(UniversalBaseModel):
    active: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Active"),
        pydantic.Field(alias="Active", description="The subscription status.  The status is active by default."),
    ] = None
    """
    The subscription status.  The status is active by default.
    """

    client_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ClientID"),
        pydantic.Field(alias="ClientID", description="Read Only after creation. The client id of the subscriber."),
    ]
    """
    Read Only after creation. The client id of the subscriber.
    """

    last_checkin: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="LastCheckin"),
        pydantic.Field(alias="LastCheckin", description="ReadOnly. The timestamp of the last checkin."),
    ] = None
    """
    ReadOnly. The timestamp of the last checkin.
    """

    relationship_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="RelationshipID"),
        pydantic.Field(
            alias="RelationshipID",
            description="Read Only after creation. The relationship id.  A relationship id will be assigned if not provided on creation.",
        ),
    ] = None
    """
    Read Only after creation. The relationship id.  A relationship id will be assigned if not provided on creation.
    """

    update_group_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="UpdateGroupID"),
        pydantic.Field(
            alias="UpdateGroupID", description="Read Only after creation. The update group to subscribe to."
        ),
    ]
    """
    Read Only after creation. The update group to subscribe to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
