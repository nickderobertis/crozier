

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OtoroshiModelsErrorTemplate(UniversalBaseModel):
    """
    Service descriptor error template
    """

    template50x: typing.Optional[str] = pydantic.Field(default=None)
    """
    The 50x error html template
    """

    template_maintenance: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="templateMaintenance"),
        pydantic.Field(alias="templateMaintenance", description="The maintenance html template"),
    ] = None
    """
    The maintenance html template
    """

    template_build: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="templateBuild"),
        pydantic.Field(alias="templateBuild", description="The build html template"),
    ] = None
    """
    The build html template
    """

    service_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="serviceId"),
        pydantic.Field(alias="serviceId", description="Service id for this template"),
    ] = None
    """
    Service id for this template
    """

    loc: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="_loc"), pydantic.Field(alias="_loc")
    ] = None
    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    ???
    """

    messages: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Map of messages
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    template40x: typing.Optional[str] = pydantic.Field(default=None)
    """
    The 40x error html template
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    ???
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
