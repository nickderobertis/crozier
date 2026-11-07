

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MetadataSchemeVersionsItemValid(UniversalBaseModel):
    """
    A version of a scheme is assumed to be approved for use by its maintainer from its `issued` date until the issued date of a subsequent version. If this is not the case, (for example, where multiple versions are approved simultaneously), `valid` expresses the period for which a version is approved for use. If an end date is provided, this indicates the date on which approval was withdrawn; otherwise the version is still considered approved for use, despite the issue of subsequent versions.
    """

    start: typing.Optional[str] = pydantic.Field(default=None)
    """
    The start date of the period.
    """

    end: typing.Optional[str] = pydantic.Field(default=None)
    """
    The end date of the period (if applicable).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
