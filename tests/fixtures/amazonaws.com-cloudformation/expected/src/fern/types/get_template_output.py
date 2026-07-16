

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .template_stage import TemplateStage


class GetTemplateOutput(UniversalBaseModel):
    """
    The output for <a>GetTemplate</a> action.
    """

    template_body: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TemplateBody")] = (
        pydantic.Field(default=None)
    )
    """
    <p>Structure containing the template body. (For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.)</p> <p>CloudFormation returns the same template that was used when the stack was created.</p>
    """

    stages_available: typing_extensions.Annotated[
        typing.Optional[typing.List[TemplateStage]], FieldMetadata(alias="StagesAvailable")
    ] = pydantic.Field(default=None)
    """
    The stage of the template that you can retrieve. For stacks, the <code>Original</code> and <code>Processed</code> templates are always available. For change sets, the <code>Original</code> template is always available. After CloudFormation finishes creating the change set, the <code>Processed</code> template becomes available.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
