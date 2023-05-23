# Test Plan

This document describes the tests that this project has to pass in order to be considered complete. 
It will provide a detailed list of the tests that have been performed and their results compared to what was expected. It will also describe how to reproduce those tests and particularly reproduce the bugs in order to help fixing them.

### Bug impact

The bugs of the software have been classified in three categories:

- **Critical**: The bug prevents the software from working properly. It is a showstopper and must be fixed before the software can be released.
- **Major**: The bug prevents the software from working properly in some cases. It is not a showstopper but must be fixed before the software can be released.
- **Minor**: The bug does not prevent the software from working properly but it is still a bug and should be fixed before the software can be released.

### Quality
The quality of the software is evaluated using the following metrics:
- **Correctness**: The software should not crash and should not produce half full or half empty tanks.
- **Close to the input formula**: The software should find a solution that is as close as possible to the input formula.
- **Minimum number of steps**: The software should find the solution in the minimum number of steps.
- **Speed**: The software should find the solution as fast as possible.

### Test Cases
##### Test for Correctness:
- **Description**: Verify that the software does not crash and maintains the fullness of tanks.
- **Procedure**: 
    - Run the software with various inputs and combinations of tanks.
    - Monitor for any crashes or errors.
    - Ensure that no tanks are left half full or half empty.
- **Expected Result**: The software runs without crashing, and all tanks are either completely full or completely empty.

##### Test for Close to Input Formula:
- **Description**: Validate that the software produces a blend that closely matches the provided input formula.
- **Procedure**:
    - Provide a known input formula with specific proportions of wines.
    - Example Input Formula: 50% Wine A, 30% Wine B, 20% Wine C.
    - Run the software and retrieve the resulting blend.
    - Compare the proportions of the resulting blend with the input formula.
- **Expected Result**: The resulting blend proportions closely resemble the input formula within an acceptable margin of error.

##### Test for Minimum Number of Steps:
- **Description**: Determine if the software achieves the desired blend using the minimum number of steps.
- **Procedure**:
    - Provide a large set of available wines and a complex input formula.
    - Run the software and track the number of steps taken to achieve the blend.
- **Expected Result**: The software finds the blend using the fewest possible steps based on the available wines and input formula.

##### Test for Speed:
- **Description**: Evaluate the speed of the software in producing the desired blend.
- **Procedure**:
    - Provide a moderate-sized set of available wines and a standard input formula.
    - Measure the time it takes for the software to compute the blend.
- **Expected Result**: The software computes the blend within a reasonable timeframe, considering the size of the available wines and the complexity of the input formula.

### Bug Reproduction
To reproduce any encountered bugs and assist in resolving them, follow these steps:

- Document the steps leading up to the bug, including the specific inputs, available wines, and the expected outcome.
- Repeat the steps multiple times to ensure the bug is consistent.
- Record any error messages, crashes, or unexpected behaviors.
- Provide the gathered information, including the steps to reproduce the bug and the observed behavior, to the development team for further investigation and resolution.
- By following this test plan, we can ensure that the software for Krug Champagne's winery meets the defined quality metrics and resolves any encountered bugs before its release.