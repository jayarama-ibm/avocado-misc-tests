#!/usr/bin/env python

import os
from avocado import Test
from avocado import main
from avocado.utils import archive
from avocado.utils import build
from avocado.utils import process
from avocado.utils.software_manager import SoftwareManager

backend = SoftwareManager()


class Binutils(Test):
    """
    This testcase make use of unit testsuite provided by the
    source package, performs functional test for all binary tools
    source file is downloaded and compiled.
    """

    def setUp(self):
        '''
        Install required tools and resolve dependencies
        '''
        backend.install('rpmbuild')
        backend.install('elfutils')
        backend.install('build')
        backend.install('autoconf')
        backend.install('automake')
        backend.install('binutils-devel')
        backend.install('dejagnu')
        backend.install('libtool')

        """
        Extract - binutils
        Source: http://ftp.gnu.org/gnu/binutils/binutils-2.25.1.tar.bz2
        """
        tarball = self.fetch_asset(
            'http://ftp.gnu.org/gnu/binutils/binutils-2.25.1.tar.bz2')
        archive.extract(tarball, self.srcdir)

        bintools_version = os.path.basename(tarball.split('.tar.')[0])
        self.srcdir = os.path.join(self.srcdir, bintools_version)

    def test(self):
        os.chdir(self.srcdir)

        process.run('./configure')
        build.make(self.srcdir)
        build.make(self.srcdir, extra_args='check')

if __name__ == "__main__":
    main()
