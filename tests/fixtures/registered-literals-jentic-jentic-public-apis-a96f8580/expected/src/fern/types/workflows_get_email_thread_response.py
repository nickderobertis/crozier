

import typing

from .email_not_found import EmailNotFound
from .workflow_not_found import WorkflowNotFound

WorkflowsGetEmailThreadResponse = typing.Union[WorkflowNotFound, EmailNotFound]
