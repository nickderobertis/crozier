

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .prebuilt_workflow_step_name import PrebuiltWorkflowStepName
from .workflow_step_options import WorkflowStepOptions


class PrebuiltWorkflowStep(UniversalBaseModel):
    """
    A Phase 1 step: references a server-defined pipeline by name.

    The ``name`` identifies the prebuilt pipeline to run AND becomes the key
    under which this step's result appears in the response ``output`` map.
    The ``document`` field is a reference into the ``inputs`` namespace
    (``"$inputs.<logical-name>"``).
    """

    name: PrebuiltWorkflowStepName = pydantic.Field()
    """
    Workflow to run — doubles as the result key in ``output``. v1 only: ``"parse-extract"``.
    """

    document: str = pydantic.Field()
    """
    Reference into the ``inputs`` namespace, e.g. ``"$inputs.report"``. The referenced input must be declared in the ``inputs`` form field.
    """

    schema_: typing_extensions.Annotated[
        typing.Dict[str, typing.Any],
        FieldMetadata(alias="schema"),
        pydantic.Field(alias="schema", description="JSON Schema for fields to extract."),
    ]
    """
    JSON Schema for fields to extract.
    """

    options: typing.Optional[WorkflowStepOptions] = pydantic.Field(default=None)
    """
    Parse + extract options for this step. Omit for defaults.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
