

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.custom_pronunciation import CustomPronunciation


class BulkCreatePronunciationsResponse(UniversalBaseModel):
    success: typing.Optional[bool] = None
    total_created: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of pronunciations successfully created
    """

    total_errors: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of files that failed validation
    """

    items: typing.Optional[typing.List[CustomPronunciation]] = None
    errors: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
