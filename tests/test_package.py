"""Test the package itself."""

import importlib.metadata

import galactic_dynamics_interop as m


def test_version():
    """Test the package version."""
    assert importlib.metadata.version("galactic_dynamics_interop") == m.__version__
