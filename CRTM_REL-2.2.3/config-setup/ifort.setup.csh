#!/bin/csh
#-------------------------------------------------------------------------------#
# PRODUCTION build settings for Linux ifort compiler
#-------------------------------------------------------------------------------#

setenv FC "ifort"
setenv FCFLAGS "-O3 -fPIC -fp-model source -free -assume byterecl"
setenv LDFLAGS ""
setenv LIBS ""
