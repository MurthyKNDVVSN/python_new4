# Match Statement
# it is like switch in java
# match the op and execute
# python  > 3.10
from unittest import case

BROWSER_NAME = input(" ENTERBTHE BROWSER NAME:\n")
match BROWSER_NAME:
    case "FIREFOX":
        print("Starting FIREFOX")
    case "CHROME":
        print("Starting CHROME")
    case "SAFARI":
        print("Starting SAFARI")
    case "EDGE":
        print("Starting EDGE")
    case "_":
        print("Browser not found")
