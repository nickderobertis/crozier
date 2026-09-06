

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AuthorizationCodesSharedModelsParameter(UniversalBaseModel):
    """
    A parameter used to create an authorization code.
    """

    name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="The name of the parameter. May not be updated."),
    ]
    """
    The name of the parameter. May not be updated.
    """

    value: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Value"),
        pydantic.Field(alias="Value", description="The value of the parameter. May not be updated."),
    ]
    """
    The value of the parameter. May not be updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
