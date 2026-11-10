

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CreditFreddieMacIndividualNameVoa24(UniversalBaseModel):
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    first_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="FirstName"),
        pydantic.Field(
            alias="FirstName", description="The first name of the individual represented by the parent object."
        ),
    ]
    """
    The first name of the individual represented by the parent object.
    """

    last_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="LastName"),
        pydantic.Field(
            alias="LastName", description="The last name of the individual represented by the parent object."
        ),
    ]
    """
    The last name of the individual represented by the parent object.
    """

    middle_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="MiddleName"),
        pydantic.Field(
            alias="MiddleName", description="The middle name of the individual represented by the parent object."
        ),
    ]
    """
    The middle name of the individual represented by the parent object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
