import crtm_interface
isis='amsua_n15'
obstype='amsua'
crtm_coeffs_path = '/scratch3/BMC/gsienkf/whitaker/gsi/EXP-enkflinhx/fix/crtm-2.2.3/'
init_pass=1
mype_diaghdr=2
mype=3
nchanl=7
crtm_interface.crtm_initialize(init_pass,mype_diaghdr,mype,nchanl,isis,obstype,crtm_coeffs_path)