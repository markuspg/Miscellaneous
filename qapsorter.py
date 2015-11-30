#!/usr/bin/env python3

##############################################################################
##
## Copyright 2015 Markus Prasser
##
## This file is part of QAPSorter.
##
##  QAPSorter is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  QAPSorter is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with QAPSorter.  If not, see <http://www.gnu.org/licenses/>.
##
##############################################################################

import sys

def main():
    print( "  <---- QAPSorter ----->  " )
    print( "\nThis program is intended to sort the problem instances of QAPLIB"
           "\nconverted by QAPConverter by their size." )

    if not len( sys.argv ) == 2:
        print( "Please give one argument: the path of the file to sort" )
        return 0
    
    lines = []
    with open( sys.argv[ 1 ], 'rt' ) as inputFile:
        for line in inputFile:
            lines.append( line.strip().split( '|' ) )
    lines.sort( key=lambda line: int( line[2] ) )
    for line in lines:
        print( line[ 2 ] )
    with open( sys.argv[ 1 ], 'wt' ) as outputFile:
        for line in lines:
            outputFile.write( '|'.join( line ) + "\n" )
    
    return 0

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
