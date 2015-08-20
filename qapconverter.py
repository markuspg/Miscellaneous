#!/usr/bin/env python3

##############################################################################
##
## Copyright 2015 Markus Prasser
##
## This file is part of QAPConverter.
##
##  QAPConverter is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  QAPConverter is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with QAPConverter.  If not, see <http://www.gnu.org/licenses/>.
##
##############################################################################

import sys

def main():
    print( "  <---- QAPConverter ----->  " )
    print( "\nThis program is intended to convert the problem instances of QAPLIB"
           "\nto a single file containing all problems line by line." )

    if len( sys.argv ) < 2:
        print( "Please give at least one argument: the path(s) of the file(s) to convert" )
        return 0
    
    with open( "qap_problems.dat", 'wt' ) as outputFile:
        for fileName in sys.argv[ 1 : ]:
            print( "\nReading file " + fileName )
            with open( fileName, 'rt' ) as f:
                line = f.readline().rstrip( '\n' )
                problemSize = int( line )
                print( "  Reading problem of size {0}".format( problemSize ) )
                
                # Drop empty line
                f.readline()
                
                # Read the flow matrix
                flowMatrix = list()
                for i in range( problemSize ):
                    flowMatrix.append( f.readline().rstrip( '\n' ).split() )
                    # print( "  " + str( i + 1 ) + ": " + str( flowMatrix[ -1 ] ) )
                
                # Drop empty line
                f.readline()
                
                # Read the distance matrix
                distanceMatrix = list()
                for i in range( problemSize ):
                    distanceMatrix.append( f.readline().rstrip( '\n' ).split() )
                    # print( "  " + str( i + 1 ) + ": " + str( distanceMatrix[ -1 ] ) )
                
                line = fileName + "|" + str( problemSize ) + "|" + ';'.join( [ num for row in flowMatrix for num in row ] ) + "|" + ';'.join( [ num for row in distanceMatrix for num in row ] )
                outputFile.write( line + "\n" )
    
    return 0


if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
