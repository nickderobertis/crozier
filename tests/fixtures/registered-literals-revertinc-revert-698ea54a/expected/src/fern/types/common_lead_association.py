

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommonLeadAssociation(UniversalBaseModel):
    contact_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contactId"),
        pydantic.Field(alias="contactId", description="The id of the contact to associate with lead"),
    ] = None
    """
    The id of the contact to associate with lead
    """

    company_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="companyId"),
        pydantic.Field(alias="companyId", description="The id of the company to associate with lead"),
    ] = None
    """
    The id of the company to associate with lead
    """

    deal_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="dealId"),
        pydantic.Field(alias="dealId", description="The id of the deal to associate with lead"),
    ] = None
    """
    The id of the deal to associate with lead
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
