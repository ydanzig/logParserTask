# logParserTask
Log parser task

Write a program that summaries Warning/Error number according to the attached file (ibdiagnet_out.txt)

 

 

Example of the table:

Summary

-I- Stage                               Warnings   Errors     Comment

-I- Discovery                           3          0

-I- Lids Check                          0          0

-I- Links Check                         0          0

-I- Subnet Manager                      0          0

-I- Port Counters                       0          0

-I- Nodes Information                   16         0

-I- Speed / Width checks                0          15

-I- Virtualization                      0          0

-I- Partition Keys                      0          0

-I- Temperature Sensing                 0          0

-I- Create IBNetDiscover File           0          0

 

 

 

General flow of the program:

Load/read the input file.
Parse table.
Print results in the follow format ( for section with error/warnings messages only).
Example of output:

 

“Nodes Information section has 16 Warnings and 0 Errors”

“Speed / Width checks section has 0 Warnings and 15 Errors”
