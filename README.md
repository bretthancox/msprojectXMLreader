# msprojectXMLreader
A project for reading the XML of project files and extracting key data

Scope:
  - CURRENT: 
      - Read an MS Project file saved as XML, convert to JSON, and extract hard-coded key/value pairs to save in a file
  - FUTURE: 
      - Replace save to file with save to CouchDB
      - Replace hard-coded key/value pairs with config file
      - Automate file selection so that the code will run on a directory and act on any new files
      - Track and trend analysis of values in CouchDB
          - Accuracy of initial estimating
          - Date drifting
          - Disruptive tasks added within X days of start date
