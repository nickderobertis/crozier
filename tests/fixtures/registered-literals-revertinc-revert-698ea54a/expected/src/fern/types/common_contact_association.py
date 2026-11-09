

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommonContactAssociation(UniversalBaseModel):
    deal_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="dealId"),
        pydantic.Field(alias="dealId", description="The id of the deal to associate with contact"),
    ] = None
    """
    The id of the deal to associate with contact
    """

    lead_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="leadId"),
        pydantic.Field(alias="leadId", description="The id of lead to associate with contact for close crm"),
    ] = None
    """
    The id of lead to associate with contact for close crm
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
