

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Analysis(UniversalBaseModel):
    bucket: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Should bucket analysis be run on this upload
    """

    copyright_email_author: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Should Copyright/Email/URL/Author Analysis be run on this upload.
    """

    ecc: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Should ECC Analysis be run on this upload.
    """

    keyword: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Should keyword Analysis be run on this upload.
    """

    mime: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Should MIME Analysis be run on this upload.
    """

    monk: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Should Monk Analysis be run on this upload.
    """

    nomos: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Should Nomos Analysis be run on this upload.
    """

    ojo: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Should OJO Analysis be run on this upload.
    """

    package: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Should Package Analysis be run on this upload.
    """

    reso: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Should REUSE.Software Analysis be run on this upload.
    """

    heritage: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Should Software Heritage Analysis be run on this upload.
    """

    compatibility: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Should Compatibility Analysis be run on this upload.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
