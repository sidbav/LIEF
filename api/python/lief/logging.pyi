from typing import ClassVar

import lief.logging # type: ignore

class LOGGING_LEVEL:
    __members__: ClassVar[dict] = ...  # read-only
    CRITICAL: ClassVar[LOGGING_LEVEL] = ...
    DEBUG: ClassVar[LOGGING_LEVEL] = ...
    ERROR: ClassVar[LOGGING_LEVEL] = ...
    INFO: ClassVar[LOGGING_LEVEL] = ...
    TRACE: ClassVar[LOGGING_LEVEL] = ...
    WARNING: ClassVar[LOGGING_LEVEL] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

def disable() -> None: ...
def enable() -> None: ...
def set_level(level: lief.logging.LOGGING_LEVEL) -> None: ...
