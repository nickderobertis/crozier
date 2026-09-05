

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .external_signing_service import ExternalSigningService
from .status_enum import StatusEnum
from .terms_and_conditions_item_type import TermsAndConditionsItemType


class TermsAndConditionsItem(UniversalBaseModel):
    content: typing_extensions.Annotated[
        str, FieldMetadata(alias="Content"), pydantic.Field(alias="Content", description="The MarkDown of the TnC")
    ]
    """
    The MarkDown of the TnC
    """

    external_signing_service: typing_extensions.Annotated[
        typing.Optional[ExternalSigningService],
        FieldMetadata(alias="ExternalSigningService"),
        pydantic.Field(alias="ExternalSigningService"),
    ] = None
    name: typing_extensions.Annotated[
        str, FieldMetadata(alias="Name"), pydantic.Field(alias="Name", description="The Name of the TnC")
    ]
    """
    The Name of the TnC
    """

    status: typing_extensions.Annotated[
        typing.Optional[StatusEnum], FieldMetadata(alias="Status"), pydantic.Field(alias="Status")
    ] = None
    tn_c_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="TnCId"),
        pydantic.Field(alias="TnCId", description="Unique identifier for the Terms and Conditions Item"),
    ] = None
    """
    Unique identifier for the Terms and Conditions Item
    """

    type: typing_extensions.Annotated[
        TermsAndConditionsItemType,
        FieldMetadata(alias="Type"),
        pydantic.Field(alias="Type", description="Role for which this TnC applies"),
    ]
    """
    Role for which this TnC applies
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
