

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TransferSendInfo(UniversalBaseModel):
    holder_organization_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="holderOrganizationId"),
        pydantic.Field(alias="holderOrganizationId", description="The current holder of the object"),
    ] = None
    """
    The current holder of the object
    """

    keep_ownership: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="keepOwnership"),
        pydantic.Field(alias="keepOwnership", description="Keep the public ownership while transferring the object"),
    ]
    """
    Keep the public ownership while transferring the object
    """

    open_for_claims: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="openForClaims"),
        pydantic.Field(
            alias="openForClaims",
            description="Allow anyone who knows (or can scan) the ID4N to claim ownership of this object",
        ),
    ]
    """
    Allow anyone who knows (or can scan) the ID4N to claim ownership of this object
    """

    owner_organization_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ownerOrganizationId"),
        pydantic.Field(alias="ownerOrganizationId", description="The current publicly visible owner of the object"),
    ] = None
    """
    The current publicly visible owner of the object
    """

    recipient_organization_ids: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="recipientOrganizationIds"),
        pydantic.Field(
            alias="recipientOrganizationIds", description="Allow only these organizations to obtain this object"
        ),
    ]
    """
    Allow only these organizations to obtain this object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
