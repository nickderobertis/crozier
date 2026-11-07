

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AddEditDeleteLicenseDecision(UniversalBaseModel):
    short_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="shortName"),
        pydantic.Field(alias="shortName", description="Short name of the license"),
    ] = None
    """
    Short name of the license
    """

    add: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, add the license if not on the list, otherwise update it's properties.
    If false, remove the license from the list.
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    Clearing info text
    """

    ack: typing.Optional[str] = pydantic.Field(default=None)
    """
    Acknowledgement of license decision
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    Comment for the license decision
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
