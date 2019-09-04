#################### INFO ####################
# The features are to be tested are defined as a variables in device_info.py
# If the snapshot names are not defined when the script is run it will use the default values specified in the script

# To profile the baseline of the network state:
#robot -i connORbase -d 04_09-19 --variable baseline:./04_09-19/initial_snapshot profiling.robot
# To profile the current state and compare it with the baseline state
#robot -i connORcurrORcomp -d 04_09-19 --variable baseline:./04_09-19/initial_snapshot --variable current:./04_09-19/initial_snapshot profiling.robot

# Comparing of muliple itmes doesnt work, think need to do individually


# Loads external libraries and files that provide the keywords and variables used in the test cases (similar to import in Python).
*** Settings ***
Library         ats.robot.pyATSRobot
Library         genie.libs.robot.GenieRobot
Variables       device_info.py			                # File containing variables which can be used directly in the test cases

# Defines local variables that will be used in the test cases
*** Variables ***
${testbed}      testbed.yml
${baseline}    ./initial_snapshot		    # Default used unless overridden by dash argument at runtime
${current}    ./current_snapshot		    # Default used unless overridden by dash argument at runtime

# These are the actions or tests performed. Can have multiple test cases with keywords used to decide what is done.
*** Test Cases ***
Connect to all devices
    [tags]      conn
    use genie testbed "${testbed}"
    FOR     ${name}      IN      @{devices}
        connect to device "${name}"
    END

Baseline snapshot of the state of the specified features
    [tags]      base
    FOR     ${name}      IN      @{devices}
        Profile the system for "${features}" on devices "${name}" as "${baseline}"
    END

Snapshot of current state of the specified features
    [tags]      curr
    FOR     ${name}      IN      @{devices}
        Profile the system for "${features}" on devices "${name}" as "${current}"
    END

Compare the baseline and current snapshots
    [tags]      comp
    FOR     ${name}      IN      @{devices}
        Compare profile "${baseline}" with "${current}" on devices "${devices}"
    END