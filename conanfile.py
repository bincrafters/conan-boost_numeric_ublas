from conans import ConanFile, tools
import os

class BoostNumeric_UblasConan(ConanFile):
    name = "Boost.Numeric_Ublas"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-ublas"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["ublas"]
    requires =  "Boost.Concept_Check/1.65.1@bincrafters/testing", \
                      "Boost.Config/1.65.1@bincrafters/testing", \
                      "Boost.Core/1.65.1@bincrafters/testing", \
                      "Boost.Iterator/1.65.1@bincrafters/testing", \
                      "Boost.Mpl/1.65.1@bincrafters/testing", \
                      "Boost.Numeric_Interval/1.65.1@bincrafters/testing", \
                      "Boost.Range/1.65.1@bincrafters/testing", \
                      "Boost.Serialization/1.65.1@bincrafters/testing", \
                      "Boost.Smart_Ptr/1.65.1@bincrafters/testing", \
                      "Boost.Static_Assert/1.65.1@bincrafters/testing", \
                      "Boost.Type_Traits/1.65.1@bincrafters/testing", \
                      "Boost.Typeof/1.65.1@bincrafters/testing", \
                      "Boost.Utility/1.65.1@bincrafters/testing"

                      #concept_check5 config0 core2 iterator5 mpl5 numeric~interval6 range7 serialization11 smart_ptr4 static_assert1 type_traits3 typeof5 utility5
                      
    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()