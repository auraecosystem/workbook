* ================================================
* File: process_customers.prg
* Language: Visual FoxPro / xBase (dBASE, Clipper)
* ================================================

CLEAR
SET TALK OFF

LOCAL cCity, nCount
cCity = "New York"
nCount = 0

* Open the database table
IF FILE("customers.dbf")
    USE customers IN 0 AGAIN ALIAS cust
    SELECT cust
    
    ? "Active Customers in " + cCity
    ? "----------------------------------------"
    
    * Iterate through records matching criteria
    SCAN FOR UPPER(City) == UPPER(cCity) AND Active = .T.
        ? "ID: " + TRANSFORM(CustID) + " | Name: " + ALLTRIM(FirstName) + " " + ALLTRIM(LastName)
        nCount = nCount + 1
    ENDSCAN
    
    ? "----------------------------------------"
    ? "Total records processed: " + TRANSFORM(nCount)
    
    CLOSE DATABASES
ELSE
    ? "Error: customers.dbf table not found."
ENDIF

RETURN
