"""Gala interoperability."""

from __future__ import annotations

__all__ = ["GalaLibrary"]


from typing import Any, final

from plum import conversion_method

from galactic_dynamics_interoperability._base import AbstractInteroperableLibrary
from galactic_dynamics_interoperability._core import convert_potential


@final
class GalaLibrary(AbstractInteroperableLibrary):
    """The :mod:`gala` library."""


# plum support
@conversion_method(type_from=object, type_to=GalaLibrary)  # type: ignore[misc]
def convert_to_gala_library(obj: object) -> Any:
    """Convert to an :class:`GalaLibrary` object."""
    convert_potential(GalaLibrary, obj)
