# Nott-Your-Marks
Calculates the average marks for your modules

# Installation
``` sh
git clone https://github.com/ecyht2/Nott-Your-Marks.git
```

# Usage
**Note:** When inputing module codes the **space** must be there between your course and the number.
## Command Line
``` sh
python3 nott-your-marks.py
```
or

``` sh
./nott-your-marks.py
```

## CSV
Nott Your Marks also supports reading data from a csv file. 

Example csv file:

``` csv
EEEE 1042,78
EEEE 1027,51
EEEE 1028,70
EEEE 1029,87
EEEE 1030,92
EEEE 1043,71
```

# TODO
  * [ ] Change the credits into a database using sqlite3
  * [x] Enable csv file reading support
  * [ ] Make a GUI
  * [ ] Add feature to list course modules
  * [ ] Add support for inputting data using argv
  * [ ] Scrape course info from [Curriculum Catalogue](https://campus.nottingham.ac.uk/psc/csprd_pub/EMPLOYEE/SA/c/UN_PROG_AND_MOD_EXTRACT.UN_PAM_CRSE_EXTRCT.GBL "Curriculum Catalogue")
