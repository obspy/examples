#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import obspy.core

st = obspy.core.read("BW.BGLD.__.EHE.D.2008.001.first_10_percent")
st[0].data = st[0].data.astype('float32')

st.write("float.mseed",format="MSEED",reclen=512,byteorder=0)

s = open("float.mseed","rb").read()
data = np.fromstring(s[56:512],"<f4")

np.testing.assert_array_equal(data, st[0].data[:114])

