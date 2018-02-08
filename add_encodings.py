#!/usr/bin/env python3

import importlib
import pkgutil
import golflang_encodings
import codecs

# adapted from https://stackoverflow.com/a/25562415/2508324


def import_submodules(package, recursive=True):
    """ Import all submodules of a module, recursively, including subpackages
    :param package: package (name or actual module)
    :param recursive: recursively import submodules?
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(import_submodules(full_name))
    return results


import_submodules(golflang_encodings)