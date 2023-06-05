| N°  | Test                                     | Expected                 |  Result                    | Comment                                             | Severity | Fixed |
|-----|------------------------------------------|--------------------------|----------------------------|-----------------------------------------------------|----------|-------|
|**1**| test_level_negative (moving -10)         |ValueError                | 20                         | The movement was allowed when it souldn't have been | minor    |&check;|
|**2**| moving liquid t1(10/30)t2(0/30)t3(20/30) |t1(0/30)t2(0/30)t3(30/30) | t1(0/30)t2(10/30)t3(30/30) | Multiple tanks are updated at the same time         | major    |&check;|
|**3**| floating point precision error           | 123                      | 122.9999999999             | Some value have a decimal point error               | major    |&check;|
|**4**| Unsolved cases                           | Solved cases             | Unsolved cases             | Some cases that can and should be solved are not    | major    |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |
|     |                                          |                          |                            |                                                     |          |       |

Additional comments:
- Test number 3  is due to the way floating point numbers are stored in the computer. The fix for this is, for now to use a python library that handles this problem. We also use a margin of error 'EPSILON' to counteract this error. If we deem necessary in the future, we can implement our own solution but for now it is not a priority. 