

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommonContactRead(UniversalBaseModel):
    first_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="firstName"),
        pydantic.Field(alias="firstName", description="The first name of the contact in a CRM."),
    ]
    """
    The first name of the contact in a CRM.
    """

    last_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="lastName"),
        pydantic.Field(alias="lastName", description="The last name of the contact in a CRM."),
    ]
    """
    The last name of the contact in a CRM.
    """

    phone: str = pydantic.Field()
    """
    The phone number of the contact in a CRM.
    """

    email: str = pydantic.Field()
    """
    The email of the contact in a CRM.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
