

import typing

from .group_scope import GroupScope
from .span_scope import SpanScope
from .trace_scope import TraceScope

TopicAutomationConfigScope = typing.Union[SpanScope, TraceScope, GroupScope]
