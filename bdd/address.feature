Scenario Outline: Add new address
  Given an address list
  Given an address with <first_name>, <middle_name> and <last_name>
  When I add the address to the list
  Then the new address list is equal to old address list with the added address


  Examples:
  | first_name | middle_name | last_name |
  | FirstName1 | MidName1    | LastName1 |
  | FirstName2 | MidName2    | LastName2 |