

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.info import Info


class AddEditDeleteLicenseDecisionResponse(UniversalBaseModel):
    success: typing.Optional[typing.List[Info]] = pydantic.Field(default=None)
    """
    List of the items' responses whose requests processed successfully.
    """

    errors: typing.Optional[typing.List[Info]] = pydantic.Field(default=None)
    """
    List of the errors found.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
