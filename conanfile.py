#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/stable")

class BoostNumeric_UblasConan(base.BoostBaseConan):
    name = "boost_numeric_ublas"
    url = "https://github.com/bincrafters/conan-boost_numeric_ublas"
    lib_short_names = ["ublas"]
    header_only_libs = ["ublas"]
    b2_requires = [
        "boost_concept_check",
        "boost_config",
        "boost_core",
        "boost_iterator",
        "boost_mpl",
        "boost_numeric_interval",
        "boost_range",
        "boost_serialization",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_type_traits",
        "boost_typeof"
    ]


