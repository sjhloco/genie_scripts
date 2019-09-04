# Loads external libraries and files that provide the keywords and variables used in the test cases (similar to import in Python).
*** Settings ***
Library         ats.robot.pyATSRobot
Library         genie.libs.robot.GenieRobot
Library         unicon.robot.UniconRobot                 # This is required to run execute cmds
Variables       device_info.py			                # File containing variables which can be used directly in the test cases

# Defines local variables that will be used in the test cases
*** Variables ***
${testbed}      testbed.yml				                # The testbed file will be represented by this variable in test cases

# These are the actions or tests performed. Can have multiple test cases with keywords used to decide what is done.
*** Test Cases ***
Connect           # Initializes the pyATS/Genie Testbed and connect. !! This way the connect is a test !!
    use genie testbed "${testbed}"
    FOR     ${name}      IN      @{devices}
        connect to device "${name}"
    END

Verify the counts of 'up' Interfaces         # This is the name of the test that will show in the summary and report
    FOR     ${name}     ${int_cnt}      IN ZIP      ${devices}     ${up_int}
        verify count "${int_cnt}" "interface up" on device "${name}"
    END

Verify the counts of ospf 'full' neighbors
    FOR     ${name}     ${ospf_cnt}      IN ZIP      ${devices}     ${ospf_neigh}
        verify count "${ospf_cnt}" "ospf neighbors" on device "${name}"
    END

# Verify the counts of BGP 'established' neighbors
# Doesnt work, on CSR doesnt see any neighors and xnos doesnt read data properly.
#     FOR     ${name}     ${bgp_cnt}      IN ZIP      ${devices}     ${bgp_neigh}
#         verify count "${bgp_cnt}" "bgp neighbors" on device "${name}"
#     END

# Custom high-level keywords created by combining existing keywords together.
*** Keywords ***
