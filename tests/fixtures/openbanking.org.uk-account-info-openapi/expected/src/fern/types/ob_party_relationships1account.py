

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ObPartyRelationships1Account(UniversalBaseModel):
    """
    Relationship to the Account resource.
    """

    id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Id"),
        pydantic.Field(
            alias="Id",
            description="Unique identification as assigned by the ASPSP to uniquely identify the related resource.",
        ),
    ]
    """
    Unique identification as assigned by the ASPSP to uniquely identify the related resource.
    """

    related: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Related"),
        pydantic.Field(alias="Related", description="Absolute URI to the related resource."),
    ]
    """
    Absolute URI to the related resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
