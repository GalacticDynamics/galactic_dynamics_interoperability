"""Base class for library type on which to dispatch."""

from __future__ import annotations

__all__ = ["AbstractInteroperableLibrary"]


from typing_extensions import Never


class AbstractInteroperableLibrary:
    """Abstract base class for library type on which to dispatch.

    These classes are used as flags to dispatch to the correct conversion
    function. They are not meant to be instantiated!

    Raises
    ------
    ValueError
        If an attempt is made to instantiate this class.

    Examples
    --------
    In this example we show how to use this class as a target for dispatching

    >>> from numbers import Number
    >>> from galactic_dynamics_interoperability import AbstractInteroperableLibrary
    >>> from plum import dispatch

    We define a library class that is a subclass of
    `AbstractInteroperableLibrary`. Here it represents a library that deals with
    numbers.

    >>> class NumbersLibrary(AbstractInteroperableLibrary):
    ...    pass

    We can now define a function that checks if an object is an instance of the
    library.

    >>> @dispatch
    ... def check_library_isinstance(lib: type[NumbersLibrary], obj: Number, /) -> bool:
    ...    return True

    >>> check_library_isinstance(NumbersLibrary, 1)
    True

    This single dispatch is trivial, but this becomes useful when we have
    multiple libraries, and / or different inheritance structures, so that an
    `isinstance` check is insufficient.

    Just as a reminder, this class is not meant to be instantiated:

    >>> try: NumbersLibrary()
    ... except ValueError as e: print(e)
    cannot instantiate AbstractInteroperableLibrary

    """

    def __new__(cls: type[AbstractInteroperableLibrary]) -> Never:
        msg = "cannot instantiate AbstractInteroperableLibrary"

        raise ValueError(msg)
