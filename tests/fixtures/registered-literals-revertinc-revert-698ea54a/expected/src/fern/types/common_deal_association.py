

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommonDealAssociation(UniversalBaseModel):
    contact_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contactId"),
        pydantic.Field(alias="contactId", description="The id of the contact to associate with deal"),
    ] = None
    """
    The id of the contact to associate with deal
    """

    company_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="companyId"),
        pydantic.Field(alias="companyId", description="The id of the company to associate with deal"),
    ] = None
    """
    The id of the company to associate with deal
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
