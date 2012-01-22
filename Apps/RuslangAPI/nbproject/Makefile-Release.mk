#
# Generated Makefile - do not edit!
#
# Edit the Makefile in the project folder instead (../Makefile). Each target
# has a -pre and a -post target defined where you can add customized code.
#
# This makefile implements configuration specific macros and targets.


# Environment
MKDIR=mkdir
CP=cp
GREP=grep
NM=nm
CCADMIN=CCadmin
RANLIB=ranlib
CC=gcc
CCC=g++
CXX=g++
FC=gfortran
AS=as

# Macros
CND_PLATFORM=Cygwin-Windows
CND_CONF=Release
CND_DISTDIR=dist
CND_BUILDDIR=build

# Include project Makefile
include Makefile

# Object Directory
OBJECTDIR=${CND_BUILDDIR}/${CND_CONF}/${CND_PLATFORM}

# Object Files
OBJECTFILES= \
	${OBJECTDIR}/src/lettersetstorage.o \
	${OBJECTDIR}/src/cyrillic/cp1251.o \
	${OBJECTDIR}/src/wordform.o \
	${OBJECTDIR}/src/misctools.o \
	${OBJECTDIR}/src/cyrillic/str_cp1251.o \
	${OBJECTDIR}/src/convert.o \
	${OBJECTDIR}/src/letterset.o \
	${OBJECTDIR}/src/wordformstorage.o


# C Compiler Flags
CFLAGS=

# CC Compiler Flags
CCFLAGS=
CXXFLAGS=

# Fortran Compiler Flags
FFLAGS=

# Assembler Flags
ASFLAGS=

# Link Libraries and Options
LDLIBSOPTIONS=

# Build Targets
.build-conf: ${BUILD_SUBPROJECTS}
	"${MAKE}"  -f nbproject/Makefile-${CND_CONF}.mk ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/libruslangapi.a

${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/libruslangapi.a: ${OBJECTFILES}
	${MKDIR} -p ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}
	${RM} ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/libruslangapi.a
	${AR} -rv ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/libruslangapi.a ${OBJECTFILES} 
	$(RANLIB) ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/libruslangapi.a

${OBJECTDIR}/src/lettersetstorage.o: src/lettersetstorage.cpp 
	${MKDIR} -p ${OBJECTDIR}/src
	${RM} $@.d
	$(COMPILE.cc) -O2 -MMD -MP -MF $@.d -o ${OBJECTDIR}/src/lettersetstorage.o src/lettersetstorage.cpp

${OBJECTDIR}/src/cyrillic/cp1251.o: src/cyrillic/cp1251.cpp 
	${MKDIR} -p ${OBJECTDIR}/src/cyrillic
	${RM} $@.d
	$(COMPILE.cc) -O2 -MMD -MP -MF $@.d -o ${OBJECTDIR}/src/cyrillic/cp1251.o src/cyrillic/cp1251.cpp

${OBJECTDIR}/src/wordform.o: src/wordform.cpp 
	${MKDIR} -p ${OBJECTDIR}/src
	${RM} $@.d
	$(COMPILE.cc) -O2 -MMD -MP -MF $@.d -o ${OBJECTDIR}/src/wordform.o src/wordform.cpp

${OBJECTDIR}/src/misctools.o: src/misctools.cpp 
	${MKDIR} -p ${OBJECTDIR}/src
	${RM} $@.d
	$(COMPILE.cc) -O2 -MMD -MP -MF $@.d -o ${OBJECTDIR}/src/misctools.o src/misctools.cpp

${OBJECTDIR}/src/cyrillic/str_cp1251.o: src/cyrillic/str_cp1251.cpp 
	${MKDIR} -p ${OBJECTDIR}/src/cyrillic
	${RM} $@.d
	$(COMPILE.cc) -O2 -MMD -MP -MF $@.d -o ${OBJECTDIR}/src/cyrillic/str_cp1251.o src/cyrillic/str_cp1251.cpp

${OBJECTDIR}/src/convert.o: src/convert.cpp 
	${MKDIR} -p ${OBJECTDIR}/src
	${RM} $@.d
	$(COMPILE.cc) -O2 -MMD -MP -MF $@.d -o ${OBJECTDIR}/src/convert.o src/convert.cpp

${OBJECTDIR}/src/letterset.o: src/letterset.cpp 
	${MKDIR} -p ${OBJECTDIR}/src
	${RM} $@.d
	$(COMPILE.cc) -O2 -MMD -MP -MF $@.d -o ${OBJECTDIR}/src/letterset.o src/letterset.cpp

${OBJECTDIR}/src/wordformstorage.o: src/wordformstorage.cpp 
	${MKDIR} -p ${OBJECTDIR}/src
	${RM} $@.d
	$(COMPILE.cc) -O2 -MMD -MP -MF $@.d -o ${OBJECTDIR}/src/wordformstorage.o src/wordformstorage.cpp

# Subprojects
.build-subprojects:

# Clean Targets
.clean-conf: ${CLEAN_SUBPROJECTS}
	${RM} -r ${CND_BUILDDIR}/${CND_CONF}
	${RM} ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/libruslangapi.a

# Subprojects
.clean-subprojects:

# Enable dependency checking
.dep.inc: .depcheck-impl

include .dep.inc
