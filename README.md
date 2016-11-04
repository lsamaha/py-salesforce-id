# py-salesforce-id

## About

A simple helper function for Salesforce integrators working in Python who are encountering short (15 digit Salesforce IDs).
This project implements Salesforce algorithm for converting the short form 15 character ID to a long form 18 character ID.
The history of the long form ID has its basis in case-insensitive data storage performed by some external systems.
The last 3 digits serve as a check-digit as explained [here](http://salesforce.stackexchange.com/questions/27686/how-can-i-convert-a-15-char-id-value-into-an-18-char-id-value):
The algorithm is available in the Salesforce platform and has been implelented in many other languages for
integration work. This is example is for Python integrations.

## Example

```Python
from salesforce import tolongid

shortid = '001A0000006Vm9r'
longid = tolongid(shortid) # 001A0000006Vm9rIAC
```
