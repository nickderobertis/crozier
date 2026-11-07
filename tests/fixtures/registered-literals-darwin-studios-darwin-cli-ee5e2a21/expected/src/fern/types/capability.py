

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .capability_account_requirement import CapabilityAccountRequirement
from .capability_availability import CapabilityAvailability
from .capability_owning_ai import CapabilityOwningAi
from .capability_payment_requirement import CapabilityPaymentRequirement
from .capability_price import CapabilityPrice


class Capability(UniversalBaseModel):
    ai_id: typing_extensions.Annotated[str, FieldMetadata(alias="aiId"), pydantic.Field(alias="aiId")]
    profile_handle: typing_extensions.Annotated[
        str, FieldMetadata(alias="profileHandle"), pydantic.Field(alias="profileHandle")
    ]
    capability_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="capabilityId"), pydantic.Field(alias="capabilityId")
    ]
    capability_revision: typing_extensions.Annotated[
        int, FieldMetadata(alias="capabilityRevision"), pydantic.Field(alias="capabilityRevision")
    ]
    type: str
    execution_domain: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="executionDomain"), pydantic.Field(alias="executionDomain")
    ] = None
    capability_kind: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="capabilityKind"), pydantic.Field(alias="capabilityKind")
    ] = None
    title: str
    description: typing.Optional[str] = None
    category: typing.Optional[str] = None
    tags: typing.List[str]
    media_preview_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mediaPreviewUrl"), pydantic.Field(alias="mediaPreviewUrl")
    ] = None
    pricing: typing.Optional[CapabilityPrice] = None
    availability: typing.Optional[CapabilityAvailability] = None
    protocols: typing.List[str]
    account_requirement: typing_extensions.Annotated[
        typing.Optional[CapabilityAccountRequirement],
        FieldMetadata(alias="accountRequirement"),
        pydantic.Field(alias="accountRequirement"),
    ] = None
    payment_requirement: typing_extensions.Annotated[
        typing.Optional[CapabilityPaymentRequirement],
        FieldMetadata(alias="paymentRequirement"),
        pydantic.Field(alias="paymentRequirement"),
    ] = None
    owning_ai: typing_extensions.Annotated[
        CapabilityOwningAi, FieldMetadata(alias="owningAi"), pydantic.Field(alias="owningAi")
    ]
    why_matched: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="whyMatched"), pydantic.Field(alias="whyMatched")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
