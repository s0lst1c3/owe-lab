import os

with open('wireshark_version_number') as fd:
    wireshark_version = fd.read().strip()

wireshark_deps = 'dependencies/wireshark.txt'
wireshark_tar = 'wireshark-{}.tar.xz'.format(wireshark_version)
wireshark_url = 'https://1.na.dl.wireshark.org/src/{}'.format(wireshark_tar)
wireshark_dir = 'wireshark-{}'.format(wireshark_version)
wireshark_build_dir = 'wireshark-build'
wireshark_bin = '{}/run/wireshark'.format(wireshark_build_dir)
wireshark_cmake_options_file = '{}/CMakeOptions.txt'.format(wireshark_dir)
wireshark_cmake_options_file_bak = '{}.bak'.format(wireshark_cmake_options_file)

hostap_owe_dir = 'hostap-owe'
hostap_owe_hostapd_dir = os.path.join(hostap_owe_dir, 'hostapd')
hostap_owe_hostapd_defconfig = os.path.join(hostap_owe_hostapd_dir, 'defconfig')
hostap_owe_hostapd_dotconfig = os.path.join(hostap_owe_hostapd_dir, '.config')
hostap_owe_hostapd_bin = os.path.join(hostap_owe_hostapd_dir, 'hostapd')
hostap_owe_wpa_supplicant_dir = os.path.join(hostap_owe_dir, 'wpa_supplicant')
hostap_owe_wpa_supplicant_defconfig = os.path.join(hostap_owe_wpa_supplicant_dir, 'defconfig')
hostap_owe_wpa_supplicant_dotconfig = os.path.join(hostap_owe_wpa_supplicant_dir, '.config')
hostap_owe_wpa_supplicant_bin = os.path.join(hostap_owe_wpa_supplicant_dir, 'wpa_supplicant')
