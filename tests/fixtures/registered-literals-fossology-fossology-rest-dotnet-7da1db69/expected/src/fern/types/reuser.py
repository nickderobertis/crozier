

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Reuser(UniversalBaseModel):
    reuse_upload: int = pydantic.Field()
    """
    The UploadID to reuse.
    """

    reuse_group: str = pydantic.Field()
    """
    The group of the reused upload
    """

    reuse_main: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Copy the main license from reused package?
    """

    reuse_enhanced: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Run enhanced reuser with diff tool (slow)
    """

    reuse_report: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Copy all report configuration from conf page.
    """

    reuse_copyright: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Copy the copyright deactivation and edits.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
