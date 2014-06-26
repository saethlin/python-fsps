#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tools for working with the FSPS filter set.
"""

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

__all__ = ["find_filter", "FILTERS"]

import os
import numpy as np

# Cache for $SPS_HOME/data/magsun.dat parsed by numpy
MSUN_TABLE = None

# Cache for $SPS_HOME/data/filter_lambda_eff.dat parsed by numpy
LAMBDA_EFF_TABLE = None


class Filter(object):

    def __init__(self, index, name, fullname):
        self.index = index - 1
        self.name = name.lower()
        self.fullname = fullname

    def __str__(self):
        return "<Filter({0})>".format(self.name)

    def __repr__(self):
        return "<Filter({0})>".format(self.name)

    @property
    def msun_ab(self):
        """Solar absolute magnitude in Filter, AB zeropoint."""
        # if self._msun_ab is None:
        if MSUN_TABLE is None:
            self._load_msun_table()
        return float(MSUN_TABLE[self.index, 1])

    @property
    def msun_vega(self):
        """Solar absolute magnitude in Filter, VEGAMAG zeropoint."""
        if MSUN_TABLE is None:
            self._load_msun_table()
        return float(MSUN_TABLE[self.index, 2])

    @property
    def lambda_eff(self):
        """Effective wavelength of Filter, in Angstroms."""
        if LAMBDA_EFF_TABLE is None:
            self._load_lambda_eff_table()
        return float(LAMBDA_EFF_TABLE[self.index, 1])

    def _load_msun_table(self):
        global MSUN_TABLE
        MSUN_TABLE = np.loadtxt(
            os.path.expandvars("$SPS_HOME/data/magsun.dat"))

    def _load_lambda_eff_table(self):
        global LAMBDA_EFF_TABLE
        LAMBDA_EFF_TABLE = np.loadtxt(
            os.path.expandvars("$SPS_HOME/data/filter_lambda_eff.dat"))


FILTERS = [(1, "V", "Johnson V (from Bessell 1990 via M. Blanton) - this "
            "defines V=0 for the Vega system"),
           (2, "U", "Johnson U (from Bessell 1990 via M. Blanton)"),
           (3, "B", "Johnson B (from Bessell 1990 via M. Blanton)"),
           (4, "Buser_B2", "Johnson B (from BC03. This is the B2 filter from "
            "Buser)"),
           (5, "Cousins_R", "Cousins R (from Bessell 1990 via M. Blanton)"),
           (6, "Cousins_I", "Cousins I (from Bessell 1990 via M. Blanton)"),
           (7, "CFHT_B", "CFHT B-band (from Blanton's kcorrect)"),
           (8, "CFHT_R", "CFHT R-band (from Blanton's kcorrect)"),
           (9, "CFHT_I", "CFHT I-band (from Blanton's kcorrect)"),
           (10, "2MASS_J", "2MASS J filter (total response w/atm)"),
           (11, "2MASS_H", "2MASS H filter (total response w/atm))"),
           (12, "2MASS_Ks", "2MASS Ks filter (total response w/atm)"),
           (13, "SDSS_u", "SDSS Camera u Response Function, airmass = 1.3 "
                "(June 2001)"),
           (14, "SDSS_g", "SDSS Camera g Response Function, airmass = 1.3 "
                "(June 2001)"),
           (15, "SDSS_r", "SDSS Camera r Response Function, airmass = 1.3 "
                "(June 2001)"),
           (16, "SDSS_i", "SDSS Camera i Response Function, airmass = 1.3 "
                "(June 2001)"),
           (17, "SDSS_z", "SDSS Camera z Response Function, airmass = 1.3 "
                "(June 2001)"),
           (18, "WFPC2_F255W", "HST WFPC2 F255W "
               "(http://acs.pha.jhu.edu/instrument/photometry/)"),
           (19, "WFPC2_F300W", "HST WFPC2 F300W "
               "(http://acs.pha.jhu.edu/instrument/photometry/)"),
           (20, "WFPC2_F336W", "HST WFPC2 F336W "
               "(http://acs.pha.jhu.edu/instrument/photometry/)"),
           (21, "WFPC2_F439W", "HST WFPC2 F439W "
               "(http://acs.pha.jhu.edu/instrument/photometry/)"),
           (22, "WFPC2_F450W", "HST WFPC2 F450W "
               "(http://acs.pha.jhu.edu/instrument/photometry/)"),
           (23, "WFPC2_F555W", "HST WFPC2 F555W "
               "(http://acs.pha.jhu.edu/instrument/photometry/)"),
           (24, "WFPC2_F606W", "HST WFPC2 F606W "
               "(http://acs.pha.jhu.edu/instrument/photometry/)"),
           (25, "WFPC2_F814W", "HST WFPC2 F814W "
               "(http://acs.pha.jhu.edu/instrument/photometry/)"),
           (26, "WFPC2_F850LP", "HST WFPC2 F850LP "
               "(http://acs.pha.jhu.edu/instrument/photometry/)"),
           (27, "WFC_ACS_F435W", "HST WFC ACS F435W "
               "(http://acs.pha.jhu.edu/instrument/photometry/)"),
           (28, "WFC_ACS_F475W", "HST ACS F475W "
               "(http://acs.pha.jhu.edu/instrument/photometry/)"),
           (29, "WFC_ACS_F555W", "HST ACS F555W "
                "(http://acs.pha.jhu.edu/instrument/photometry/"),
           (30, "WFC_ACS_F606W", "HST WFC ACS F606W "
                "(http://acs.pha.jhu.edu/instrument/photometry/)"),
           (31, "WFC_ACS_F625W", "HST ACS F625W "
                "(http://acs.pha.jhu.edu/instrument/photometry/)"),
           (32, "WFC_ACS_F775W", "HST WFC ACS F775W "
                "(http://acs.pha.jhu.edu/instrument/photometry/)"),
           (33, "WFC_ACS_F814W", "HST WFC ACS F814W "
                "(http://acs.pha.jhu.edu/instrument/photometry/)"),
           (34, "WFC_ACS_F850LP", "WFC ACS F850LP "
                "(http://acs.pha.jhu.edu/instrument/photometry/)"),
           (35, "WFC3_UVIS_F218W", "HST WFC3 UVIS F218W "
                "(http://www.stsci.edu/~WFC3/UVIS/SystemThroughput/) Chip #1"),
           (36, "WFC3_UVIS_F225W", "HST WFC3 UVIS F225W "
                "(http://www.stsci.edu/~WFC3/UVIS/SystemThroughput/) Chip #1"),
           (37, "WFC3_UVIS_F275W", "HST WFC3 UVIS F275W "
                "(http://www.stsci.edu/~WFC3/UVIS/SystemThroughput/) Chip #1"),
           (38, "WFC3_UVIS_F336W", "HST WFC3 UVIS F336W "
                "(http://www.stsci.edu/~WFC3/UVIS/SystemThroughput/) Chip #1"),
           (39, "WFC3_UVIS_F390W", "HST WFC3 UVIS F390W "
                "(http://www.stsci.edu/~WFC3/UVIS/SystemThroughput/) Chip #1"),
           (40, "WFC3_UVIS_F438W", "HST WFC3 UVIS F438W "
                "(http://www.stsci.edu/~WFC3/UVIS/SystemThroughput/) Chip #1"),
           (41, "WFC3_UVIS_F475W", "HST WFC3 UVIS F475W "
                "(http://www.stsci.edu/~WFC3/UVIS/SystemThroughput/) Chip #1"),
           (42, "WFC3_UVIS_F555W", "HST WFC3 UVIS F555W "
                "(http://www.stsci.edu/~WFC3/UVIS/SystemThroughput/) Chip #1"),
           (43, "WFC3_UVIS_F606W", "HST WFC3 UVIS F606W "
                "(http://www.stsci.edu/~WFC3/UVIS/SystemThroughput/) Chip #1"),
           (44, "WFC3_UVIS_F775W", "HST WFC3 UVIS F775W "
                "(http://www.stsci.edu/~WFC3/UVIS/SystemThroughput/) Chip #1"),
           (45, "WFC3_UVIS_F814W", "HST WFC3 UVIS F814W "
                "(http://www.stsci.edu/~WFC3/UVIS/SystemThroughput/) Chip #1"),
           (46, "WFC3_UVIS_F850LP", "HST WFC3 UVIS F850LP "
                "(http://www.stsci.edu/~WFC3/UVIS/SystemThroughput/) Chip #1"),
           (47, "WFC3_IR_F098M", "HST WFC3 IR F098M "
                "(http://www.stsci.edu/~WFC3/UVIS/SystemThroughput/)"),
           (48, "WFC3_IR_F105W", "HST WFC3 IR F105W "
                "(http://www.stsci.edu/~WFC3/UVIS/SystemThroughput/)"),
           (49, "WFC3_IR_F110W", "HST WFC3 IR F110W "
                "(http://www.stsci.edu/~WFC3/UVIS/SystemThroughput/)"),
           (50, "WFC3_IR_F125W", "HST WFC3 IR F125W "
                "(http://www.stsci.edu/~WFC3/UVIS/SystemThroughput/)"),
           (51, "WFC3_IR_F140W", "HST WFC3 IR F140W "
                "(http://www.stsci.edu/~WFC3/UVIS/SystemThroughput/)"),
           (52, "WFC3_IR_F160W", "HST WFC3 IR F160W "
                "(http://www.stsci.edu/~WFC3/UVIS/SystemThroughput/)"),
           (53, "IRAC_1", "Spitzer IRAC Channel 1 (3.6um)"),
           (54, "IRAC_2", "Spitzer IRAC Channel 2 (4.5um)"),
           (55, "IRAC_3", "Spitzer IRAC Channel 3 (5.8um)"),
           (56, "IRAC_4", "Spitzer IRAC Channel 4 (8.0um)"),
           (57, "ISAAC_Ks", "ISAAC Ks"),
           (58, "FORS_V", "FORS V"),
           (59, "FORS_R", "FORS R"),
           (60, "NICMOS_F110W", "HST NICMOS F110W"),
           (61, "NICMOS_F160W", "HST NICMOS F160W"),
           (62, "GALEX_FUV", "GALEX FUV"),
           (63, "GALEX_NUV", "GALEX NUV"),
           (64, "DES_g", "DES g (from Huan Lin, for DES camera)"),
           (65, "DES_r", "DES r (from Huan Lin, for DES camera)"),
           (66, "DES_i", "DES i (from Huan Lin, for DES camera)"),
           (67, "DES_z", "DES z (from Huan Lin, for DES camera)"),
           (68, "DES_Y", "DES Y (from Huan Lin, for DES camera)"),
           (69, "WFCAM_Z", "WFCAM Z (from Hewett et al. 2006, via A. Smith)"),
           (70, "WFCAM_Y", "WFCAM Y (from Hewett et al. 2006, via A. Smith)"),
           (71, "WFCAM_J", "WFCAM J (from Hewett et al. 2006, via A. Smith)"),
           (72, "WFCAM_H", "WFCAM H (from Hewett et al. 2006, via A. Smith)"),
           (73, "WFCAM_K", "WFCAM K (from Hewett et al. 2006, via A. Smith)"),
           (74, "Steidel_Un", "Steidel Un (via A. Shapley; see Steidel et al. "
                "2003)"),
           (75, "Steidel_G", "Steidel G  (via A. Shapley; see Steidel et al. "
                "2003)"),
           (76, "Steidel_Rs", "Steidel Rs (via A. Shapley; see Steidel et al. "
                "2003)"),
           (77, "Steidel_I", "Steidel I  (via A. Shapley; see Steidel et al. "
                "2003)"),
           (78, "MegaCam_u", "CFHT MegaCam u* "
                "(http://cadcwww.dao.nrc.ca/megapipe/docs/filters.html, "
                "Dec 2010)"),
           (79, "MegaCam_g", "CFHT MegaCam g' "
                "(http://cadcwww.dao.nrc.ca/megapipe/docs/filters.html)"),
           (80, "MegaCam_r", "CFHT MegaCam r' "
                "(http://cadcwww.dao.nrc.ca/megapipe/docs/filters.html)"),
           (81, "MegaCam_i", "CFHT MegaCam i' "
                "(http://cadcwww.dao.nrc.ca/megapipe/docs/filters.html)"),
           (82, "MegaCam_z", "CFHT MegaCam z' "
                "(http://cadcwww.dao.nrc.ca/megapipe/docs/filters.html)"),
           (83, "WISE_W1", "3.4um WISE W1 "
                "(http://www.astro.ucla.edu/~wright/WISE/passbands.html)"),
           (84, "WISE_W2", "4.6um WISE W2 "
                "(http://www.astro.ucla.edu/~wright/WISE/passbands.html)"),
           (85, "WISE_W3", "12um WISE W3 "
                "(http://www.astro.ucla.edu/~wright/WISE/passbands.html)"),
           (86, "WISE_W4", "22um WISE W4 22um "
                "(http://www.astro.ucla.edu/~wright/WISE/passbands.html)"),
           (87, "UVOT_W2", "UVOT W2 (from Erik Hoversten, 2011)"),
           (88, "UVOT_M2", "UVOT M2 (from Erik Hoversten, 2011)"),
           (89, "UVOT_W1", "UVOT W1 (from Erik Hoversten, 2011)"),
           (90, "MIPS_24", "Spitzer MIPS 24um"),
           (91, "MIPS_70", "Spitzer MIPS 70um"),
           (92, "MIPS_160", "Spitzer MIPS 160um"),
           (93, "SCUBA_450WB", "JCMT SCUBA 450WB "
            "(www.jach.hawaii.edu/JCMT/continuum/background/background.html)"),
           (94, "SCUBA_850WB", "JCMT SCUBA 850WB"),
           (95, "PACS_70", "Herschel PACS 70um"),
           (96, "PACS_100", "Herschel PACS 100um"),
           (97, "PACS_160", "Herschel PACS 160um"),
           (98, "SPIRE_250", "Herschel SPIRE 250um"),
           (99, "SPIRE_350", "Herschel SPIRE 350um"),
           (100, "SPIRE_500", "Herschel SPIRE 500um"),
           (101, "IRAS_12", "IRAS 12um"),
           (102, "IRAS_25", "IRAS 25um"),
           (103, "IRAS_60", "IRAS 60um"),
           (104, "IRAS_100", "IRAS 100um"),
           (105, "Bessell_L", "Bessell & Brett (1988) L band"),
           (106, "Bessell_LP", "Bessell & Brett (1988) L' band"),
           (107, "Bessell_M", "Bessell & Brett (1988) M band"),
           (108, "Stromgren_u", "Stromgren u (Bessell 2011)"),
           (109, "Stromgren_v", "Stromgren v (Bessell 2011)"),
           (110, "Stromgren_b", "Stromgren b (Bessell 2011)"),
           (111, "Stromgren_y", "Stromgren y (Bessell 2011)"),
           (112, "1500A", "Idealized 1500A bandpass with 15% bandwidth, "
            "FWHM = 225A from M. Dickinson"),
           (113, "2300A", "Idealized 2300A bandpass with 15% bandwidth, "
            "FWHM = 345A from M. Dickinson"),
           (114, "2800A", "Idealized 2800A bandpass with 15% bandwidth, "
            "FWHM = 420A from M. Dickinson"),
           (115, "JWST_F070W",
            "(http://www.stsci.edu/jwst/instruments/nircam/instrumentdesign/filters/)"),
           (116, "JWST_F090W",
            "(http://www.stsci.edu/jwst/instruments/nircam/instrumentdesign/filters/)"),
           (117, "JWST_F115W",
            "(http://www.stsci.edu/jwst/instruments/nircam/instrumentdesign/filters/)"),
           (118, "JWST_F150W",
            "(http://www.stsci.edu/jwst/instruments/nircam/instrumentdesign/filters/)"),
           (119, "JWST_F200W",
            "(http://www.stsci.edu/jwst/instruments/nircam/instrumentdesign/filters/)"),
           (120, "JWST_F277W",
            "(http://www.stsci.edu/jwst/instruments/nircam/instrumentdesign/filters/)"),
           (121, "JWST_F356W",
            "(http://www.stsci.edu/jwst/instruments/nircam/instrumentdesign/filters/)"),
           (122, "JWST_F444W",
            "(http://www.stsci.edu/jwst/instruments/nircam/instrumentdesign/filters/)")]

FILTERS = dict([(f[1].lower(), Filter(*f)) for f in FILTERS])


def find_filter(band):
    """
    Find the FSPS name for a filter.

    Usage:

    ::

        >>> import fsps
        >>> fsps.find_filter("F555W")
        ['wfpc2_f555w', 'wfc_acs_f555w']

    :param band:
        Something like the name of the band.

    """
    b = band.lower()
    possible = []
    for k in FILTERS.keys():
        if b in k:
            possible.append(k)
    return possible
