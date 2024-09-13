"""Test the package itself."""

import importlib.metadata

import galactic_dynamics_interoperability as m


def test_version():
    """Test the package version."""
    assert (
        importlib.metadata.version("galactic_dynamics_interoperability")
        == m.__version__
    )
