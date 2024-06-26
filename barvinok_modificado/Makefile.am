if BUNDLED_POLYLIB
    MAYBE_POLYLIB = polylib
    POLYLIB_LA = $(top_builddir)/polylib/libpolylibgmp.la
endif
if BUNDLED_ISL
    MAYBE_ISL = isl
    ISL_LA = $(top_builddir)/isl/libisl.la
    LOCAL_ISL_LA = isl/libisl.la
endif
if BUILD_ISL
    ISL_LA = $(ISL_BUILDDIR)/libisl.la
endif
if BUNDLED_PET
    MAYBE_PET = pet
    PET_LA = $(top_builddir)/pet/libpet.la
endif
if BUILD_PET
    PET_LA = $(PET_BUILDDIR)/libpet.la
endif
if USE_ZSOLVE
    MAYBE_ZSOLVE = zsolve
endif
SUBDIRS = $(MAYBE_POLYLIB) $(MAYBE_ISL) $(MAYBE_PET) \
		$(MAYBE_ZSOLVE) . doc
DIST_SUBDIRS = $(MAYBE_POLYLIB) $(MAYBE_ISL) $(MAYBE_PET) \
		zsolve doc

FORCE:
polylib/libpolylibgmp.la: FORCE
	cd polylib; $(MAKE) $(AM_MAKEFLAGS) libpolylibgmp.la
isl/libisl.la: FORCE
	cd isl; $(MAKE) $(AM_MAKEFLAGS) libisl.la
pet/libpet.la: $(LOCAL_ISL_LA) FORCE
	cd pet; $(MAKE) $(AM_MAKEFLAGS) libpet.la
zsolve/libzsolve.la: FORCE
	cd zsolve; $(MAKE) $(AM_MAKEFLAGS) libzsolve.la

AM_CPPFLAGS = @POLYLIB_CPPFLAGS@ \
	      @ISL_CFLAGS@ @NTL_CPPFLAGS@
AM_LDFLAGS = @BV_LDFLAGS@ @POLYLIB_LDFLAGS@ @NTL_LDFLAGS@

LIB_ISL = $(ISL_LA) @ISL_LIBS@
LIB_PET = $(PET_LA) @PET_LIBS@
LIB_POLYLIB = $(POLYLIB_LA) @POLYLIB_LIBS@

lib_LTLIBRARIES = libbarvinok.la
bin_PROGRAMS = barvinok_count barvinok_enumerate barvinok_enumerate_e \
		  barvinok_ehrhart iscc
noinst_PROGRAMS = test testlib randomtest \
		  barvinok_union polytope_volume test_approx \
		  barvinok_summate \
		  4coins lexmin \
		  @bv_cone_hilbert_basis@ cone_integer_hull \
		  polyhedron_integer_hull vector_partition_chambers \
		  semigroup_holes \
		  barvinok_bound test_bound \
		  polytope_scan
EXTRA_PROGRAMS = cone_hilbert_basis
pkginclude_HEADERS = \
    barvinok/NTL_QQ.h \
    barvinok/isl.h \
    barvinok/barvinok.h \
    barvinok/util.h \
    barvinok/evalue.h \
    barvinok/genfun.h \
    barvinok/options.h \
    barvinok/polylib.h \
    barvinok/sample.h \
    barvinok/basis_reduction.h
nodist_pkginclude_HEADERS = \
    barvinok/NTL.h \
    barvinok/set.h
LINK = $(CXXLINK)

if HAVE_CDDLIB
    BR_CDD = basis_reduction_cdd.cc initcdd.cc
    POLYSIGN_CDD = polysign_cddf.cc polysign_cdd.cc
endif
if HAVE_GLPK
    BR_GLPK = basis_reduction_glpk.c
    POLYSIGN_GLPK = polysign_glpk.c
endif
if HAVE_TOPCOM
    TOPCOM = topcom.c topcom.h
endif
if USE_ZSOLVE
    HILBERT_C = hilbert.c
endif
libbarvinok_la_SOURCES = \
    barvinok/evalue.h \
    barvinok/genfun.h \
    barvinok/util.h \
    barvinok/barvinok.h \
    NTL_QQ.cc \
    basis_reduction.c \
    evalue.c \
    genfun.cc \
    util.c \
    version.c \
    bernoulli.c \
    bernoulli.h \
    bfcounter.cc \
    bfcounter.h \
    binomial.c \
    binomial.h \
    conversion.cc \
    conversion.h \
    counter.cc \
    counter.h \
    decomposer.cc \
    decomposer.h \
    dpoly.cc \
    dpoly.h \
    euler.cc \
    euler.h \
    evalue_isl.c \
    genfun_constructor.cc \
    genfun_constructor.h \
    $(HILBERT_C) \
    hilbert.h \
    hull.c \
    hull.h \
    ilp.c \
    ilp.h \
    isl_aff_polylib.c \
    isl_aff_polylib.h \
    isl_map_polylib.c \
    isl_map_polylib.h \
    isl_set_polylib.h \
    isl_param_util.c \
    isl_param_util.h \
    lattice_point.cc \
    lattice_point.h \
    lattice_width.c \
    lattice_width.h \
    laurent.cc \
    laurent.h \
    laurent_old.cc \
    laurent_old.h \
    normalization.c \
    normalization.h \
    options.c \
    param_polynomial.cc \
    param_polynomial.h \
    param_util.c \
    param_util.h \
    $(POLYSIGN_CDD) \
    $(POLYSIGN_GLPK) \
    polysign.c \
    polysign_isl.c \
    polysign_polylib.c \
    polysign.h \
    power.h \
    reduce_domain.c \
    reduce_domain.h \
    reducer.cc \
    reducer.h \
    remove_equalities.h \
    remove_equalities.c \
    sample.c \
    scale.c \
    scale.h \
    scarf.cc \
    section_array.h \
    series.cc \
    $(TOPCOM) \
    summate.c \
    summate.h \
    vertex_cone.cc \
    vertex_cone.h \
    volume.c \
    volume.h \
    mat_util.cc \
    mat_util.h \
    matrix_read.cc \
    matrix_read.h \
    barvinok.cc \
    barvinok_e.cc \
    $(BR_CDD) \
    $(BR_GLPK)
EXTRA_libbarvinok_la_SOURCES = \
    basis_reduction_cdd.cc \
    basis_reduction_glpk.c \
    hilbert.c \
    polysign_cddf.cc \
    polysign_cdd.cc \
    polysign.c \
    initcdd.cc \
    initcdd.h \
    topcom.c \
    topcom.h
if USE_ZSOLVE
    ZSOLVE_LA = zsolve/libzsolve.la
endif
libbarvinok_la_LIBADD = @LTLIBOBJS@ $(LIB_ISL) \
			     $(LIB_POLYLIB) $(ZSOLVE_LA)
libbarvinok_la_LDFLAGS = @BV_LIB_LDFLAGS@ -version-info @versioninfo@ \
				$(AM_LDFLAGS)
LDADD = libbarvinok.la $(LIB_ISL) $(LIB_POLYLIB)

test_SOURCES = \
	test.c
testlib_SOURCES = \
	evalue_read.c \
	evalue_read.h \
	testlib.cc
barvinok_count_SOURCES = barvinok_count.c
barvinok_ehrhart_SOURCES = \
	barvinok_ehrhart_options.c \
	barvinok_ehrhart_options.h \
	barvinok_ehrhart.cc \
	evalue_convert_options.c \
	evalue_convert.cc \
	evalue_convert.h \
	$(FDSTREAM)
barvinok_union_SOURCES = \
	barvinok_union_options.c \
	barvinok_union_options.h \
	barvinok_union.cc
if USE_FDSTREAM
FDSTREAM = fdstream.cc fdstream.h
endif
barvinok_enumerate_SOURCES = \
	barvinok_enumerate_options.c \
	barvinok_enumerate_options.h \
	barvinok_enumerate.cc \
	evalue_convert_options.c \
	evalue_convert.cc \
	evalue_convert.h \
	$(FDSTREAM) \
	skewed_genfun.cc \
	skewed_genfun.h \
	verify.h \
	verify.c \
	verify_series.h \
	verify_series.cc
EXTRA_barvinok_enumerate_SOURCES = fdstream.cc fdstream.h
barvinok_enumerate_e_SOURCES = \
	barvinok_enumerate_e_options.c \
	barvinok_enumerate_e_options.h \
	barvinok_enumerate_e.cc \
	evalue_convert_options.c \
	evalue_convert.cc \
	evalue_convert.h \
	$(FDSTREAM) \
	skewed_genfun.cc \
	skewed_genfun.h \
	verify.h \
	verify.c \
	verif_ehrhart.h \
	verif_ehrhart.c \
	verify_series.h \
	verify_series.cc
EXTRA_barvinok_enumerate_e_SOURCES = fdstream.cc fdstream.h
barvinok_bound_SOURCES = \
	bound.c \
	verify.h \
	verify.c
barvinok_summate_SOURCES = \
	barvinok_summate.c \
	verify.h \
	verify.c
4coins_SOURCES = 4coins.cc
semigroup_holes_SOURCES = semigroup_holes.cc
lexmin_SOURCES = \
	lexmin_options.c \
	lexmin.h \
	lexmin.cc \
	edomain.cc \
	edomain.h \
	evalue_util.cc \
	evalue_util.h \
	verify.h \
	verify.c
test_approx_SOURCES = \
	test_approx.c \
	verify.h \
	verify.c
test_bound_SOURCES = \
	test_bound.c \
	verify.h \
	verify.c
iscc_SOURCES =	\
	isl_obj_list.h \
	isl_obj_list.c \
	isl_obj_str.h \
	isl_obj_str.c \
	iscc.c
iscc_CPPFLAGS = @PET_CFLAGS@ $(AM_CPPFLAGS)
iscc_LDADD = \
	libbarvinok.la $(LIB_PET) $(LIB_ISL) \
	$(LIB_POLYLIB)

if HAVE_ISL_BUILDDIR
# dummy library that captures the dependencies on all headers
# that are relevant for the bindings
noinst_LIBRARIES = libdep.a
libdep_a_CPPFLAGS = $(DEFAULT_INCLUDES) @ISL_CFLAGS@ -I"@ISL_SRCDIR@"
libdep_a_SOURCES = interface/all_barvinok.c

@ISL_BUILDDIR@/interface/extract_interface$(EXEEXT):
	$(MAKE) -C @ISL_BUILDDIR@ interface/extract_interface$(EXEEXT)

isl.py: libdep.a interface/isl.py.top \
		@ISL_BUILDDIR@/interface/extract_interface$(EXEEXT)
	(cat interface/isl.py.top && \
		@ISL_BUILDDIR@/interface/extract_interface$(EXEEXT) \
			--language=python \
			$(DEFAULT_INCLUDES) @ISL_CFLAGS@ -I"@ISL_SRCDIR@" \
			$(srcdir)/interface/all_barvinok.h) \
			> $@ || (rm $@ && false)
endif

TESTFILES = $(shell find $(top_srcdir)/tests -type f ! -path '*CVS*')

CLEANFILES = \
	zsolve/graver \
	zsolve/hilbert \
	isl.py \
	version.h
DISTCLEANFILES = \
	barvinok-uninstalled.sh \
	barvinok-uninstalled.pc \
	barvinok.pc \
	barvinok.pc.in \
	barvinok/set.h \
	barvinok/NTL.h \
	interface/isl.py.top

EXTRA_DIST = \
    LICENSE \
    ChangeLog \
    $(TESTFILES) \
    latte2polylib.pl \
    basis_reduction_templ.c \
    cdd94e-test \
    polysign_cdd_template.cc \
    barvinok/NTL.h.broken \
    barvinok/NTL.h.normal \
    barvinok/set.h.broken \
    barvinok/set.h.normal \
    config_post.h \
    doc/isl.tex \
    doc/Internal.tex \
    doc/applications.tex \
    doc/barvinok.tex \
    doc/polymake.tex \
    doc/reports.tex \
    doc/barvinok.bib \
    doc/barvinok.gdf \
    doc/chicago.bst \
    doc/chicago.sty \
    doc/glosstex.ist \
    doc/mydefs.sty \
    interface/all_barvinok.h \
    interface/isl.py.top.no_pet \
    interface/isl.py.top.pet \
    polymake/Makefile.in \
    polymake/README \
    polymake/autogen.sh \
    polymake/configure.in \
    polymake/convert.cc \
    polymake/convert.h \
    polymake/h_star_vector.cc \
    polymake/lattice_points.cc

ACLOCAL_AMFLAGS = -I m4

install-data-local:
	@test -z "$(pkgconfig_libdir)" || $(mkdir_p) "$(DESTDIR)$(pkgconfig_libdir)"
	$(INSTALL_DATA) $(pkgconfig_libfile) "$(DESTDIR)$(pkgconfig_libdir)/$(pkgconfig_libfile)"

uninstall-local:
	rm -f "$(DESTDIR)$(pkgconfig_libdir)/$(pkgconfig_libfile)"

dist-hook: isl.py
	cp isl.py $(distdir)/
	(cd $(distdir)/polymake; \
	    ./autogen.sh; rm -rf autom4te.cache)
	(cd doc; make barvinok.pdf)
	cp doc/barvinok.pdf $(distdir)/doc/
	if test -f $(top_srcdir)/.git/HEAD; then \
	    echo @GIT_HEAD_VERSION@ > $(distdir)/GIT_HEAD_ID; \
	else \
	    echo $(GIT_HEAD_ID) > $(distdir)/GIT_HEAD_ID; \
	fi

dist-git: dist
	mv $(distdir).tar.gz @GIT_HEAD_VERSION@.tar.gz

TESTS = testlib check_enumerate.sh check_enumerate_e.sh check_test.sh \
	check_lexmin.sh check_approx.sh check_pwqp.sh check_euler.sh \
	check_iscc.sh check_union.sh

version.h: @GIT_HEAD@
	echo '#define GIT_HEAD_ID "'@GIT_HEAD_VERSION@'"' > $@
