

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LicenseCandidate(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    ID of the license-candidate.
    """

    shortname: typing.Optional[str] = pydantic.Field(default=None)
    """
    shortname of the license-candidate.
    """

    spdxid: typing.Optional[str] = pydantic.Field(default=None)
    """
    SPDX ID of the license-candiate.
    """

    fullname: typing.Optional[str] = pydantic.Field(default=None)
    """
    fullname of the license-candidate.
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    text of the license-candidate.
    """

    group_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    group_name of the license-candidate.
    """

    group_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    group_id of the license-candidate.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
