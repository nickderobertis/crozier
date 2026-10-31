

import typing

from .extraction_terminal_result import ExtractionTerminalResult
from .parsed_document import ParsedDocument
from .raw_parse_result import RawParseResult

JobResult = typing.Union[ParsedDocument, RawParseResult, ExtractionTerminalResult]
