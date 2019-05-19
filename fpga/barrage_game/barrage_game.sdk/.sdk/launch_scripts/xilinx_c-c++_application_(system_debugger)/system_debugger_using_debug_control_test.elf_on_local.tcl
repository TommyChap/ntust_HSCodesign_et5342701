connect -url tcp:127.0.0.1:3121
source E:/M10702114/ntust_HSCodesign_et5342701/fpga/barrage_game/barrage_game.sdk/system_wrapper_hw_platform_0/ps7_init.tcl
targets -set -nocase -filter {name =~"APU*" && jtag_cable_name =~ "Digilent Zed 210248525235"} -index 0
loadhw E:/M10702114/ntust_HSCodesign_et5342701/fpga/barrage_game/barrage_game.sdk/system_wrapper_hw_platform_0/system.hdf
targets -set -nocase -filter {name =~"APU*" && jtag_cable_name =~ "Digilent Zed 210248525235"} -index 0
stop
ps7_init
ps7_post_config
targets -set -nocase -filter {name =~ "ARM*#0" && jtag_cable_name =~ "Digilent Zed 210248525235"} -index 0
rst -processor
targets -set -nocase -filter {name =~ "ARM*#0" && jtag_cable_name =~ "Digilent Zed 210248525235"} -index 0
dow E:/M10702114/ntust_HSCodesign_et5342701/fpga/barrage_game/barrage_game.sdk/Control_test/Debug/Control_test.elf
targets -set -nocase -filter {name =~ "ARM*#0" && jtag_cable_name =~ "Digilent Zed 210248525235"} -index 0
con
