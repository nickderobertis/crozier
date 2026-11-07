

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .history_item_type import HistoryItemType
from .visibility import Visibility


class HistoryItem(UniversalBaseModel):
    """
    GUID history item
    """

    additional_properties: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="additionalProperties"),
        pydantic.Field(alias="additionalProperties", description="History items custom additional properties"),
    ] = None
    """
    History items custom additional properties
    """

    organization_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="organizationId"),
        pydantic.Field(alias="organizationId", description="Originator of the history item"),
    ]
    """
    Originator of the history item
    """

    owner_organization_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ownerOrganizationId"),
        pydantic.Field(alias="ownerOrganizationId", description="Owner of the history item"),
    ] = None
    """
    Owner of the history item
    """

    sequence_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="sequenceId"),
        pydantic.Field(
            alias="sequenceId",
            description="Forms the primary key of the history item together with the GUID and the organizationId",
        ),
    ] = None
    """
    Forms the primary key of the history item together with the GUID and the organizationId
    """

    timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    History item timestamp
    """

    type: HistoryItemType = pydantic.Field()
    """
    Type of the history item
    """

    visibility: typing.Optional[Visibility] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
