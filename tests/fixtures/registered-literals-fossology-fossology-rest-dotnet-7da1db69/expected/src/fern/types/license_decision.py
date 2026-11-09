

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .license import License
from .license_decision_sources_item import LicenseDecisionSourcesItem


class LicenseDecision(License):
    """
    Extended License model with additional fields
    """

    sources: typing.Optional[typing.List[LicenseDecisionSourcesItem]] = pydantic.Field(default=None)
    """
    Array of sources
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    Comment for the license decision
    """

    acknowledgement: typing.Optional[str] = pydantic.Field(default=None)
    """
    License acknowledgement
    """

    is_main_license: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isMainLicense"),
        pydantic.Field(alias="isMainLicense", description="Is the license the main license?"),
    ] = None
    """
    Is the license the main license?
    """

    is_removed: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isRemoved"),
        pydantic.Field(alias="isRemoved", description="Is the license removed?"),
    ] = None
    """
    Is the license removed?
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
