

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommonUserWrite(UniversalBaseModel):
    """
    Include the "businessUnitId" in the "additional" section, as it is a mandatory field for Microsoft Dynamics Sales.
    """

    first_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="firstName"),
        pydantic.Field(alias="firstName", description="The first name of a user in a CRM."),
    ]
    """
    The first name of a user in a CRM.
    """

    last_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="lastName"),
        pydantic.Field(alias="lastName", description="The last name of a user in a CRM."),
    ]
    """
    The last name of a user in a CRM.
    """

    phone: str = pydantic.Field()
    """
    The phone number of a user in a CRM.
    """

    email: str = pydantic.Field()
    """
    The email of a user in a CRM.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
