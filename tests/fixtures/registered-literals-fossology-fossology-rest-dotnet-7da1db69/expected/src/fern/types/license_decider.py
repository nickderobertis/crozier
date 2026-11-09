

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LicenseDecider(UniversalBaseModel):
    nomos_monk: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Scanners matches if all Nomos findings are within the Monk findings.
    """

    bulk_reused: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Bulk phrases from reused packages.
    """

    new_scanner: typing.Optional[bool] = pydantic.Field(default=None)
    """
    New scanner results, i.e., decisions were marked as work in progress if new scanner finds additional licenses.
    """

    ojo_decider: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Scanners matches if Ojo or REUSE.Software findings are no contradiction with other findings.
    """

    conclude_license_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Auto conclude license if they are of provided type.
    Omit the field or keep as empty string to not use this option.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
