

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class IndividualName(UniversalBaseModel):
    """
    Parent container for name that allows for choice group between parsed and unparsed containers.Parent container for name that allows for choice group between parsed and unparsed containers.
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
