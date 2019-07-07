# Threat Model for <company> DevSecOps Infrastructure

## Project: Project Name
## Project ID: 6

[Data Sensitivity and Exposure] <br />
01: How do you classify the data handled by the application? (sensitivity): classified <br />
02: Where does sensitive data enter and leave the application?: somewhere <br />
03: How is it secured while in transit and at rest?: somehow <br />
04: What resources are used to store this data?: something <br />
05: What type of encryption is used and how are encryption keys secured?: TLS <br />
06: What information might this feature expose to Web sites or other parties, and for what purposes is that exposure necessary?: sure <br />
07: How does this specification deal with personal information or personally-identifiable information or information derived thereof?: somehow <br />

[Authentication and Configuration] <br />
08: Does this project requires internal authentication? (passwords): yes <br />
09: Does this project requires externenal authentication? (third party): yes <br />
10: Do you have any type of passwords inside the software: yes <br />
11: What information from the underlying platform, e.g. configuration data, is exposed by this specification to an origin?: None <br />
12: Does this specification introduce new state for an origin that persists across browsing sessions?: yes <br />

[Dependencies] <br />
13: List third party dependencies: None <br />

[Additional Applications] <br />
14: Does this project interacts with databases? (sql, non-sql): yes <br />
15: If yes, is this database SQL based?: yes <br />
16: Does this specification enable new script execution/loading mechanisms?: yes <br />

[Regression Testing] <br />
17: Do you have a Dockerfile available: yes <br />
18: Do you have unit tests configured for this application: yes <br />
19: Does this application requieres specific hardware: yes <br />
20: Do you need additional support to develop regression tests: yes <br />
