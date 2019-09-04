# genie_scripts
Contains genie scripts created for testing purposes. Is only a beginning and very simple, need a lot more work.

1. **version_report**<br/>
Collects OS version and SN from NXOS, IOS and IOSXE and prints to screen and/or saves to CSV.<br/>
When run with no flags will do both and save to a file called *version_report* in home directory.<br/>
Use **table** for Table only, **csv** for CSV only, **-l** to change location, **-f** to change filename and **-h** for help

2. **robot_network_state**<br/>
*-ospf-int-report.robot:* Checks the state of OSPF and interfaces against an expected number. The devices and expected numbers are in a dictionary that is made into lists in python then fed into a for-loop in robot.<br/>
*-profiling.robot:* Profiles baseline, current state and compares them. Tags are used to run only specific test cases. Comparing of muliple items doesnt work, need to investigate.<br/>

