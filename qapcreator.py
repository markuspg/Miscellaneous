#!/usr/bin/env python3

##############################################################################
##
## Copyright 2015 Markus Prasser
##
## This file is part of QAPCreator.
##
##  QAPCreator is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  QAPCreator is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with QAPCreator.  If not, see <http://www.gnu.org/licenses/>.
##
##############################################################################

import random

def main():
    problemSize = int( input( "Please enter the desired problem size: " ) )
    flows = list()
    distances = list()
    for i in range( pow( problemSize, 2 ) ):
        flows.append( random.randrange( 0, 101 ) )
        distances.append( random.randrange( 0, 101 ) )
    problemLine = "test" + str( problemSize ) + ".qap|QAP|" + str( problemSize ) + "|" + ';'.join( [ str( num ) for num in flows ] ) + "|" + ';'.join( [ str( num ) for num in distances ] )
    print( problemLine )

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
