

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.ignored_parameters_unsupported import IgnoredParametersUnsupported
from ...types.navigation_view import NavigationView


class GetNavigationViewsResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    navigation_views: typing.Optional[typing.List[NavigationView]] = pydantic.Field(default=None)
    """
    An array of dictionaries containing the user's navigation views.
    """

    ignored_parameters_unsupported: typing.Optional[IgnoredParametersUnsupported] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
